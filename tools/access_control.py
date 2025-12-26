import os
import requests
import streamlit as st
import google.generativeai as genai
from config import COOKIE_SECRET_KEY, BACKEND_URL, PLAN_LIMITS
from .cookie_controller import EncryptedCookieManager
from .auth_utils import get_user

def get_cookie_manager():
    cookies = EncryptedCookieManager(prefix="smartcareer_", password=COOKIE_SECRET_KEY)
    if not cookies.ready():
        st.stop()
    return cookies

def enforce_auth_and_session_mgmt():
    """
    Auth + session management guard for protected pages like Home.py
    Redirects to Login.py if:
      - No token/email found
      - Token invalid
      - Backend unreachable
    """
    # --- Get cookie manager safely ---
    cookies = st.session_state.get("cookie_manager")
    if cookies is None:
        cookies = get_cookie_manager()
        st.session_state["cookie_manager"] = cookies

    # --- Try restoring session ---
    token = st.session_state.get("token") or cookies.get("token")
    email = st.session_state.get("email") or cookies.get("email")

    if not token or not email:
        st.switch_page("pages/Login.py")
        st.stop()

    # --- Validate token only if not done before ---
    if "token_validated" not in st.session_state:
        try:
            res = requests.post(
                f"{BACKEND_URL}/validate-token",
                json={"token": token},
                timeout=5
            )

            if res.status_code == 200:
                st.session_state["token_validated"] = True
                st.session_state["token"] = token
                st.session_state["email"] = email
            else:
                # Token invalid — clear and go to Login
                cookies["token"] = ""
                cookies["email"] = ""
                cookies.save()
                st.session_state.clear()
                st.switch_page("pages/Login.py")
                st.stop()

        except Exception as e:
            st.warning(f"⚠️ Server unreachable: {e}")
            st.stop()

    return True


# def calculate_usage(update_usage_fn, free_limit=7):
#     # Ensure session defaults
#     st.session_state.setdefault("usage_count", 0)
#     st.session_state.setdefault("subscribed", False)
#     st.session_state.setdefault("active_plan", "free")

#     # Get correct plan limit
#     active_plan = st.session_state["active_plan"]
#     plan_limit = PLAN_LIMITS.get(active_plan, PLAN_LIMITS["free"])

#     # Check limit
#     if st.session_state["usage_count"] >= plan_limit:
#         st.warning(f"🚨 You’ve reached the limit for your **{active_plan}** plan ({plan_limit} requests).")

#         if st.button("Upgrade Plan 💳"):
#             try:
#                 st.switch_page("pages/payment.py")  # works only if supported
#             except:
#                 st.rerun()

#         st.stop()

#     # Track usage (only once)
#     update_usage_fn(st.session_state.get("email"))
#     st.session_state["usage_count"] += 1




def calculate_usage(update_usage_fn, free_limit=7):
    """
    Robust usage tracker that persists across refreshes by reading/writing
    authoritative counters via get_user(email) and update_usage_fn(email).

    Assumptions about external functions:
      - get_user(email) -> (usage_count:int, subscribed:bool, plan_name:str)
      - update_usage_fn(email) -> increments usage server-side and (optionally) returns updated usage
    """

    # --- Safe defaults in session ---
    st.session_state.setdefault("usage_tracked_this_page", False)
    st.session_state.setdefault("active_plan", "free")
    st.session_state.setdefault("usage_count", 0)
    st.session_state.setdefault("subscribed", False)

    # Try to import nicer page switch helper if available
    try:
        from streamlit_extras.switch_page_button import switch_page as _switch_page
    except Exception:
        _switch_page = None

    # --- Step 1: load persisted state for logged-in user (email must be set in session) ---
    email = st.session_state.get("email")
    if email:
        try:
            persisted_usage, persisted_subscribed, persisted_plan = get_user(email)
            # If get_user returns None or invalid values, coerce to safe defaults
            persisted_usage = int(persisted_usage or 0)
            persisted_subscribed = bool(persisted_subscribed)
            persisted_plan = str(persisted_plan or "free")
        except Exception as e:
            # If DB read fails, show a gentle warning and continue with session values
            st.warning(f"Warning: failed to load persisted usage ({e}) — using session values.")
            persisted_usage, persisted_subscribed, persisted_plan = (
                st.session_state.get("usage_count", 0),
                st.session_state.get("subscribed", False),
                st.session_state.get("active_plan", "free"),
            )

        # Overwrite session with authoritative persisted values (keeps across refresh)
        st.session_state["usage_count"] = persisted_usage
        st.session_state["subscribed"] = persisted_subscribed
        st.session_state["active_plan"] = persisted_plan

    else:
        # No email -> anonymous: keep in-session values only (cannot persist)
        st.session_state.setdefault("usage_count", 0)
        st.session_state.setdefault("subscribed", False)
        st.session_state.setdefault("active_plan", "free")

    # --- Step 2: determine plan limit from mapping (fallback to free_limit) ---
    active_plan = st.session_state.get("active_plan", "free")
    plan_limit = PLAN_LIMITS.get(active_plan, PLAN_LIMITS.get("free", free_limit))

    # --- Step 3: If usage already at/over limit, show upgrade UI and block further use ---
    if st.session_state.get("usage_count", 0) >= plan_limit:
        usage_display = st.session_state.get("usage_count", 0)
        plan_display = active_plan.upper()

        st.markdown(f"""
        <style>
        .limit-box {{
            background: linear-gradient(135deg, #fff5f5, #ffe4e6);
            padding: 2rem;
            border-radius: 12px;
            border-left: 6px solid #ef4444;
            box-shadow: 0 6px 16px rgba(239,68,68,0.12);
            text-align: center;
        }}
        .limit-title {{ color: #dc2626; font-size: 1.6rem; margin-bottom: 0.6rem; font-weight:700; }}
        .limit-text {{ color: #374151; font-size: 1rem; }}
        .limit-subtext {{ color: #6b7280; margin-top: 0.6rem; }}
        </style>
        <div class="limit-box">
            <div class="limit-title">🚨 Usage Limit Reached</div>
            <div class="limit-text">
                You've used <strong style="color:#ef4444;">{usage_display}/{plan_limit}</strong> requests on your <strong>{plan_display}</strong> plan.
            </div>
            <div class="limit-subtext">Upgrade now to continue using SmartCareer.in!</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            upgrade_clicked = st.button("💎 Upgrade Plan", use_container_width=True)

        if upgrade_clicked:
            # Try the nicer helper first, fallback to available navigation method
            if _switch_page is not None:
                try:
                    _switch_page("payment")  # pass page title / filename (without .py)
                except Exception as e:
                    st.error(f"Navigation helper failed: {e}")
                    st.experimental_set_query_params(page="payment")
                    st.experimental_rerun()
            else:
                # Try Streamlit's builtin switch_page (if available)
                try:
                    st.switch_page("payment")
                except Exception:
                    # Fallback to query param + rerun
                    st.experimental_set_query_params(page="payment")
                    st.experimental_rerun()

        # Block execution beyond this point (user must upgrade)
        st.stop()

    # --- Step 4: If not yet tracked for this page, increment usage and persist (for logged-in users) ---
    if not st.session_state.get("usage_tracked_this_page", False):
        if email:
            # Prefer update_usage_fn to be authoritative (server increments and persists)
            try:
                update_result = update_usage_fn(email)
                # If update_usage_fn returns the new usage (common pattern), use it.
                if isinstance(update_result, (int, float, str)):
                    # numeric return -> treat as usage_count
                    try:
                        new_usage = int(update_result)
                    except Exception:
                        new_usage = st.session_state.get("usage_count", 0) + 1
                elif isinstance(update_result, dict):
                    # optional dict return: {"usage": X, "plan": "...", "subscribed": True}
                    new_usage = int(update_result.get("usage", st.session_state.get("usage_count", 0) + 1))
                    # update plan/subscribed if provided
                    if "plan" in update_result:
                        st.session_state["active_plan"] = update_result.get("plan") or st.session_state["active_plan"]
                    if "subscribed" in update_result:
                        st.session_state["subscribed"] = bool(update_result.get("subscribed"))
                else:
                    # Unknown return -> safe fallback increment
                    new_usage = st.session_state.get("usage_count", 0) + 1
            except Exception as e:
                # Backend failed; best-effort: increment session counter but warn
                st.warning(f"Usage update failed (will retry next run): {e}")
                new_usage = min(st.session_state.get("usage_count", 0) + 1, plan_limit)

            # After update, re-read authoritative values from get_user (if possible)
            try:
                persisted_usage, persisted_subscribed, persisted_plan = get_user(email)
                persisted_usage = int(persisted_usage or new_usage)
                persisted_subscribed = bool(persisted_subscribed)
                persisted_plan = str(persisted_plan or st.session_state.get("active_plan", "free"))
            except Exception:
                # if re-read fails, fall back to new_usage
                persisted_usage, persisted_subscribed, persisted_plan = new_usage, st.session_state.get("subscribed", False), st.session_state.get("active_plan", "free")

            # Cap usage at plan_limit and write back to session
            st.session_state["usage_count"] = min(persisted_usage, plan_limit)
            st.session_state["subscribed"] = persisted_subscribed
            st.session_state["active_plan"] = persisted_plan
            st.session_state["usage_tracked_this_page"] = True

        else:
            # Anonymous user -> session-only increment (no DB persistence possible)
            st.session_state["usage_count"] = min(st.session_state.get("usage_count", 0) + 1, plan_limit)
            st.session_state["usage_tracked_this_page"] = True

    # --- Step 5: return summary for UI if caller wants to render it ---
    return {
        "usage_count": st.session_state["usage_count"],
        "plan_limit": plan_limit,
        "active_plan": st.session_state["active_plan"],
        "subscribed": st.session_state["subscribed"],
    }
            
def get_gemini_model():
    """
    Initialize and return a configured Gemini model client.
    Reads all settings from .env file.
    """

    # Required key
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in .env file or environment variables.")
    genai.configure(api_key=GOOGLE_API_KEY)

    # Optional settings from .env (with safe defaults)
    model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")
    temperature = float(os.getenv("GEMINI_TEMPERATURE", 0.7))
    top_p = float(os.getenv("GEMINI_TOP_P", 0.95))
    top_k = int(os.getenv("GEMINI_TOP_K", 40))
    max_output_tokens = int(os.getenv("GEMINI_MAX_OUTPUT_TOKENS", 8192))

    # Create and return model
    model = genai.GenerativeModel(
        model_name,
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_output_tokens,
            "response_mime_type": "text/plain",
        },
    )

    return model