import bcrypt
import sqlite3
import jwt
from datetime import datetime, timedelta
from config import JWT_SECRET


def generate_token(user_email, subscribed, plan):
    try:
        payload = {
            "email": user_email,
            "subscribed": subscribed,
            "plan": plan,
            "exp": datetime.utcnow() + timedelta(days=7)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
        return token
    except Exception as e:
        print(f"❌ Error generating token: {e}")
        return None


def verify_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        print("⚠️ Token expired")
        return None
    except jwt.InvalidTokenError:
        print("⚠️ Invalid token")
        return None
    except Exception as e:
        print(f"❌ Token verification error: {e}")
        return None


def create_user_table():
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                password TEXT,
                usage_count INTEGER DEFAULT 0,
                subscribed INTEGER DEFAULT 0,
                plan TEXT DEFAULT 'free'
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"❌ Error creating users table: {e}")
    finally:
        conn.close()


def add_user(email, password):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        c.execute("""
            INSERT INTO users (email, password, usage_count, subscribed, plan)
            VALUES (?, ?, ?, ?, ?)
        """, (email, hashed_pw, 0, 0, "free"))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"⚠️ User with email {email} already exists")
        return False
    except Exception as e:
        print(f"❌ Error adding user: {e}")
        return False
    finally:
        conn.close()


def authenticate_user(email, password):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE email=?", (email,))
        result = c.fetchone()
        if result and bcrypt.checkpw(password.encode(), result[0].encode()):
            return True
        return False
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        return False
    finally:
        conn.close()


def get_user(email):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT usage_count, subscribed, plan FROM users WHERE email=?", (email,))
        result = c.fetchone()
        return result if result else None
    except Exception as e:
        print(f"❌ Error fetching user: {e}")
        return None
    finally:
        conn.close()


def update_usage(email):
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("UPDATE users SET usage_count = usage_count + 1 WHERE email=?", (email,))
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error updating usage: {e}")
        return False
    finally:
        conn.close()


def set_subscribed(email, status=True):
    """
    Update the subscribed status for a user.
    status: True = subscribed, False = not subscribed
    """
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("UPDATE users SET subscribed=? WHERE email=?", (1 if status else 0, email))
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error setting subscription: {e}")
        return False
    finally:
        conn.close()


def update_user_plan(email, plan):
    """
    Update the user's plan. This sets subscribed = 1 for paid plans and 0 for free plan.
    """
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        subscribed_value = 0 if plan.lower() == "free" else 1
        c.execute("UPDATE users SET plan=?, subscribed=? WHERE email=?", (plan, subscribed_value, email))
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error updating user plan: {e}")
        return False
    finally:
        conn.close()


def create_payments_table():
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                gateway TEXT,
                amount INTEGER,
                status TEXT,
                plan TEXT,
                subscription_id TEXT,
                order_id TEXT,
                payment_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"❌ Error creating payments table: {e}")
    finally:
        conn.close()


def add_payment_record(email, gateway, amount, status, plan=None, subscription_id=None, order_id=None, payment_id=None):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO payments (email, gateway, amount, status, plan, subscription_id, order_id, payment_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (email, gateway, amount, status, plan, subscription_id, order_id, payment_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error adding payment record: {e}")
        return False
    finally:
        conn.close()