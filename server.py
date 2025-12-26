import os
import json
import hmac
import hashlib
import uuid
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import stripe
import razorpay
from time import time
from config import (
    STRIPE_SECRET_KEY, STRIPE_PRICE_IDS,
    RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY,
    FRONTEND_DOMAIN, BACKEND_URL, PLAN_PRICES, JWT_SECRET
)
import time

from tools import get_user, create_payments_table, add_payment_record, generate_token, verify_token, set_subscribed, update_user_plan

# Init DB
create_payments_table()

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:8501"}}, supports_credentials=True)  # allow cross-origin from Streamlit
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # allow cross-origin from Streamlit

# Stripe setup
stripe.api_key = STRIPE_SECRET_KEY

# Razorpay client
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY))


# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "timestamp": time.time()})


@app.route('/generate-token', methods=['POST'])
def generate_token_route():
    data = request.get_json()
    email = data.get("email")
    subscribed = data.get("subscribed", False)
    plan = data.get("plan", "free")
    token = generate_token(email, subscribed, plan)
    return jsonify({"token": token})


# Stripe Checkout
@app.route('/create-checkout-session', methods=['POST'])   # 🔥 fixed endpoint name
def create_checkout_session():
    try:
        data = request.get_json()
        plan = data.get("plan")

        if plan not in STRIPE_PRICE_IDS:
            return jsonify({"error": "Invalid plan"}), 400

        session = stripe.checkout.Session.create(
            line_items=[{'price': STRIPE_PRICE_IDS[plan], 'quantity': 1}],
            mode='subscription',
            success_url=f"{FRONTEND_DOMAIN}/pages/payment_success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{FRONTEND_DOMAIN}/pages/payment_cancelled"
        )
        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400




# Stripe Webhook
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
@app.route('/webhook/stripe', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('stripe-signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        return jsonify({"error": "Invalid Stripe signature"}), 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_email')
        subscription_id = session.get('subscription')
        amount_total = session.get('amount_total', 0)

        # If using price_id-based plans
        line_items = session.get('display_items') or session.get('line_items')
        price_id = None
        if line_items:
            price_id = line_items[0].get('price', {}).get('id')

        # Fallback if plan can’t be determined
        plan = next((k for k, v in STRIPE_PRICE_IDS.items() if v == price_id), "unknown")

        print(f"✅ Stripe Payment Successful for {customer_email}, ₹{amount_total/100}, Plan: {plan}")

        # Save payment in DB
        add_payment_record(
            email=customer_email,
            gateway="stripe",
            amount=amount_total,
            status="completed",
            plan=plan,
            subscription_id=subscription_id
        )
            # After successful payment
        set_subscribed(customer_email)
        update_user_plan(customer_email, plan)  # NEW FUNCTION

        # ✅ Generate a new subscribed token
        if customer_email:
            token = generate_token(customer_email, subscribed=True, plan=plan)
            STREAMLIT_TOKENS[customer_email] = token
            print(f"🎟️ New token issued for {customer_email}")

    return jsonify({"status": "success"}), 200


# Razorpay Webhook
RAZORPAY_WEBHOOK_SECRET = os.getenv("RAZORPAY_WEBHOOK_SECRET", "")

@app.route('/webhook/razorpay', methods=['POST'])
def razorpay_webhook():
    payload = request.data
    received_signature = request.headers.get('X-Razorpay-Signature')

    generated_signature = hmac.new(
        bytes(RAZORPAY_WEBHOOK_SECRET, 'utf-8'),
        msg=payload,
        digestmod=hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(received_signature, generated_signature):
        return jsonify({"error": "Invalid Razorpay signature"}), 400

    webhook_data = json.loads(payload)
    event = webhook_data.get('event')

    if event == "payment.captured":
        payment_entity = webhook_data['payload']['payment']['entity']
        email = payment_entity.get("email", "unknown")
        amount = payment_entity.get("amount", 0)
        payment_id = payment_entity.get("id")
        order_id = payment_entity.get("order_id")

        print(f"✅ Razorpay Payment Captured: {email} - ₹{amount/100}")

        add_payment_record(
            email=email,
            gateway="razorpay",
            amount=amount,
            status="captured",
            payment_id=payment_id,
            order_id=order_id
        )

    return jsonify({"status": "success"}), 200

@app.route('/create-stripe-session', methods=['POST'])
def create_stripe_session():
    try:
        data = request.get_json()
        plan = data.get("plan")
        email = data.get("email")  # ✅ get email from frontend

        if plan not in STRIPE_PRICE_IDS:
            return jsonify({"error": "Invalid plan"}), 400

        session = stripe.checkout.Session.create(
            line_items=[{'price': STRIPE_PRICE_IDS[plan], 'quantity': 1}],
            mode='subscription',
            customer_email=email,              # ✅ force attach email
            customer_creation="always",        # ✅ always create customer object
            billing_address_collection="auto", # can also use "required"
            success_url=f"{FRONTEND_DOMAIN}/pages/payment_success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{FRONTEND_DOMAIN}/pages/payment_cancelled"
        )

        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---------------- STREAMLIT TOKEN BRIDGE ----------------
# Memory bridge (can use Redis/DB in prod)
STREAMLIT_TOKENS = {}

import hmac, hashlib
from flask import request, jsonify


@app.route('/get-razorpay-key', methods=['GET'])
def get_razorpay_key():
    """Return Razorpay public key for frontend"""
    return jsonify({"key": RAZORPAY_KEY_ID})
    
@app.route('/streamlit-set-token', methods=['POST'])
def streamlit_set_token():
    data = request.get_json()
    email = data.get("email")
    token = data.get("token")
    if not email or not token:
        return jsonify({"error": "Missing email or token"}), 400

    STREAMLIT_TOKENS[email] = token
    return jsonify({"success": True})


@app.route('/streamlit-get-token/<email>', methods=['GET'])
def streamlit_get_token(email):
    
    token = STREAMLIT_TOKENS.pop(email, None)
    print(f"🔑 Fetched token for {email}: {token}")
    if token:
        return jsonify({"token": token})
    else:
        return jsonify({"token": None}), 200


@app.route('/create-razorpay-order', methods=['POST'])
def create_razorpay_order():
    try:
        print("📥 Incoming Razorpay order request...")

        # Force JSON parse and validate
        data = request.get_json(force=True, silent=True)
        print("Parsed JSON:", data)

        if not data or "plan" not in data or "email" not in data:
            return jsonify({"error": "Missing required fields: plan, email"}), 400

        # Extract request values
        plan = data.get("plan", "free").lower().strip()
        email = data.get("email", "").strip()

        if not email:
            return jsonify({"error": "Invalid email"}), 400

        # --- Prevent duplicate subscription ---
        _, subscribed, current_plan = get_user(email)
        if subscribed and current_plan == plan:
            return jsonify({"error": f"User already subscribed to {plan} plan"}), 400

        # Validate plan
        if plan not in PLAN_PRICES:
            print(f"⚠️ Unknown plan '{plan}', falling back to 'basic'")
            plan = "free"

        amount_inr = PLAN_PRICES[plan]

        # Prevent zero-amount order creation (Razorpay rejects 0 value)
        if amount_inr <= 0:
            return jsonify({"error": "Free plan does not require payment"}), 400

        # Generate unique receipt id
        receipt_id = f"rcpt_{uuid.uuid4().hex[:15]}"

        # Create order with Razorpay
        order = razorpay_client.order.create({
            "amount": amount_inr * 100,  # in paisa
            "currency": "INR",
            "receipt": receipt_id,
            "payment_capture": 1
        })

        print(f"✅ Razorpay order created: {order['id']} | Plan: {plan} | Amount: ₹{amount_inr}")

        return jsonify({
            "order_id": order["id"],
            "razorpay_key": RAZORPAY_KEY_ID,
            "amount": amount_inr * 100,
            "currency": "INR",
            "plan": plan,
            "email": email
        }), 200

    except Exception as e:
        import traceback
        print("❌ Razorpay order creation failed:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500



@app.route("/verify-razorpay-payment", methods=["POST", "OPTIONS"])
def verify_razorpay_payment():
    # Handle CORS preflight request
    if request.method == "OPTIONS":
        print("🔄 Handling CORS preflight request")
        response = jsonify({"status": "ok"})
        return response, 200

    try:
        # Get JSON data from request
        data = request.get_json()
        print("🔎 Received verification request")
        print(f"🔎 Data: {data}")
        
        if not data:
            return jsonify({"success": False, "error": "No data received"}), 400
        
        # Extract required fields
        razorpay_payment_id = data.get("razorpay_payment_id")
        razorpay_order_id = data.get("razorpay_order_id")
        razorpay_signature = data.get("razorpay_signature")
        email = data.get("email")
        plan = (data.get("plan") or "basic").lower()  # default to basic if missing

        # Validate required fields
        if not all([razorpay_payment_id, razorpay_order_id, razorpay_signature, email, plan]):
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        # --- Signature Verification ---
        message = f"{razorpay_order_id}|{razorpay_payment_id}"
        expected_signature = hmac.new(
            RAZORPAY_SECRET_KEY.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(expected_signature, razorpay_signature):
            return jsonify({"success": False, "error": "Payment signature verification failed"}), 400

        print("✅ Payment signature verified successfully!")

        # --- Fetch payment details from Razorpay ---
        try:
            payment_info = razorpay_client.payment.fetch(razorpay_payment_id)
            payment_status = payment_info.get("status", "unknown")
            payment_amount = payment_info.get("amount", 0)
            
            if payment_status not in ["captured", "authorized", "settled"]:
                return jsonify({"success": False, "error": f"Payment not successful. Status: {payment_status}"}), 400

        except Exception as fetch_error:
            print(f"⚠️ Could not fetch payment from Razorpay: {fetch_error}")
            payment_amount = 0
            payment_status = "verified"

        # --- Save payment record ---
        try:
            add_payment_record(
                email=email,
                gateway="razorpay",
                amount=payment_amount,
                status="completed",
                payment_id=razorpay_payment_id,
                order_id=razorpay_order_id,
                plan=plan
            )
        except Exception as db_error:
            print(f"⚠️ Could not save payment record: {db_error}")

        # --- Update user subscription + plan in DB ---
        try:
            set_subscribed(email)
            update_user_plan(email, plan)  # make sure this commits to DB!

            # --- Generate fresh token with new plan ---
            new_token = generate_token(email, subscribed=True, plan=plan)

            # Store token (optional global cache for Streamlit)
            global STREAMLIT_TOKENS
            if "STREAMLIT_TOKENS" not in globals():
                STREAMLIT_TOKENS = {}
            STREAMLIT_TOKENS[email] = new_token

        except Exception as token_error:
            print(f"⚠️ Could not update subscription or generate token: {token_error}")
            return jsonify({"success": False, "error": "Payment verified but could not activate subscription"}), 500

        # ✅ Success response
        return jsonify({
            "success": True,
            "message": "Payment verified and subscription activated successfully!",
            "payment_id": razorpay_payment_id,
            "amount": payment_amount / 100,
            "plan": plan,
            "subscribed": True,
            "new_token": new_token   # 🔑 send back immediately
        }), 200

    except Exception as e:
        print(f"🚨 Critical error in payment verification: {str(e)}")
        import traceback; traceback.print_exc()
        
        return jsonify({"success": False, "error": f"Server error: {str(e)}"}), 500



# Updated token validation that checks for subscription updates
@app.route('/validate-token', methods=['POST'])
def validate_token():
    try:
        data = request.get_json()
        token = data.get("token")
        
        if not token:
            return jsonify({"valid": False, "error": "No token provided"}), 401
        
        user_data = verify_token(token)
        if not user_data:
            return jsonify({"valid": False}), 401

        email = user_data["email"]
        print(f"🔍 Data received: {user_data}...")

        get_db_usage_count, get_db_subscribed, get_db_plan = get_user(email)
        print("db_info", get_db_usage_count, get_db_subscribed, get_db_plan)
        # ✅ Instead of popping, just check
        if email in STREAMLIT_TOKENS:
            newer_token = STREAMLIT_TOKENS[email]
            newer_user_data = verify_token(newer_token)

            if newer_user_data and newer_user_data.get("subscribed"):
                print(f"🔄 Returning updated token for {email}")
                
                # Optionally: only delete after client ACK
                # del STREAMLIT_TOKENS[email]

                return jsonify({
                    "valid": True, 
                    "email": newer_user_data["email"], 
                    "subscribed": newer_user_data["subscribed"],
                    "plan": user_data["plan"],
                    "new_token": newer_token
                })

        # fallback
        return jsonify({
            "valid": True, 
            "email": user_data["email"], 
            "subscribed": get_db_subscribed,
            "plan": get_db_plan
        })

    except Exception as e:
        print(f"❌ Token validation error: {str(e)}")
        return jsonify({"valid": False, "error": "Server error"}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)  # Use debug=True for development