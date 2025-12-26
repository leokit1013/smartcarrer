import streamlit as st
import requests
import sqlite3
import re
from server import *
from tools import create_user_table, add_user, get_cookie_manager, authenticate_user, get_user, hide_streamlit_ui, show_login_page
# from streamlit_extras.switch_page_button import switch_page
from config import BACKEND_URL, FRONTEND_DOMAIN, COOKIE_SECRET_KEY, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
import os, time
from streamlit_oauth import OAuth2Component

st.set_page_config(
    page_title="Login",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)


print("FRONTEND_DOMAIN in login:", FRONTEND_DOMAIN)
print("BACKEND_URL in login:", BACKEND_URL)

show_login_page()
hide_streamlit_ui()

create_user_table()


if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "Login"
    
auth_mode = st.session_state["auth_mode"]


# cookies = get_cookie_manager()

# if "token" not in st.session_state:
#     st.session_state["token"] = cookies.get("token")
# if "email" not in st.session_state:
#     st.session_state["email"] = cookies.get("email")


# --- Initialize cookies only once ---
if "cookie_manager" not in st.session_state:
    cookies = get_cookie_manager()
    st.session_state["cookie_manager"] = cookies
    st.session_state["cookies_initialized"] = True
else:
    cookies = st.session_state["cookie_manager"]

# --- Always have a cookies reference safely ---
if cookies is None:
    cookies = get_cookie_manager()
    st.session_state["cookie_manager"] = cookies

# --- Read token/email from cookies if not already in session ---
if "token" not in st.session_state:
    st.session_state["token"] = cookies.get("token")
if "email" not in st.session_state:
    st.session_state["email"] = cookies.get("email")

    
# --- Validate token only once per session ---
if st.session_state.get("token") and "token_validated" not in st.session_state:
    try:
        res = requests.post(
            f"{BACKEND_URL}/validate-token",
            json={"token": st.session_state["token"]},
            timeout=5
        )

        if res.status_code == 200:
            st.session_state["token_validated"] = True
            st.switch_page("pages/Home.py")
            st.stop()  # ✅ Critical: stop rerun after redirect

        else:
            # Invalid token → clear everything
            st.session_state["token_validated"] = False
            st.session_state["token"] = None
            st.session_state["email"] = None
            cookies["token"] = ""
            cookies["email"] = ""
            cookies.save()

    except Exception as e:
        st.warning(f"⚠️ Token validation failed: {e}")



# --- Validation Helpers ---
# --- Validation Helpers ---
def valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valid_password(password: str) -> bool:
    return len(password) >= 6

# --- Login Card UI ---
st.markdown("<div class='login-icon'>🔒</div>", unsafe_allow_html=True)
st.markdown("<div class='login-title'>LeoKit Career Tools</div>", unsafe_allow_html=True)
st.markdown("<div class='login-subtitle'>Unlock Your Future with Smarter Career Choices</div>", unsafe_allow_html=True)



# --- Layout using columns ---
col1, col2 = st.columns(2, gap="small")

with col1:
    st.markdown("""
    <div style="display:flex; justify-content:center; align-items:center; height:100%;">
        <img src='https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80' 
             style="width:100%; max-width:400px; height:auto; object-fit:cover; border-radius:8px;">
    </div>
    """, unsafe_allow_html=True)
with col2:

    # Tabs for Login/Signup
    tab_col1, tab_col2 = st.columns(2)
    with tab_col1:
        if st.button("Login", key="login_tab", use_container_width=True, type="secondary" if auth_mode == "Sign Up" else "primary"):
            st.session_state["auth_mode"] = "Login"
            st.rerun()
    with tab_col2:
        if st.button("Sign Up", key="signup_tab", use_container_width=True, type="secondary" if auth_mode == "Login" else "primary"):
            st.session_state["auth_mode"] = "Sign Up"
            st.rerun()

    email = st.text_input("Email Address", placeholder="you@example.com")
    password = st.text_input("Password", type="password", placeholder="Enter your password (min 6 characters)")


    confirm_password = None
    if auth_mode == "Sign Up":
        confirm_password = st.text_input("✅ Confirm Password", type="password", placeholder="Re-enter your password")

    if st.button("" + ("Login" if auth_mode == "Login" else "Create Account"), use_container_width=True):
    # submit_btn_text = "Sign In" if auth_mode == "Login" else "Create Account"
    # if st.button(submit_btn_text, use_container_width=True, key="submit_btn"):
        if not valid_email(email):
            st.error("❌ Please enter a valid email address.")
            st.stop()
        elif not valid_password(password):
            st.error("❌ Password must be at least 6 characters long.")
            st.stop()
        elif auth_mode == "Sign Up" and password != confirm_password:
            st.error("❌ Passwords do not match.")
            st.stop()
 
        # --- SIGNUP FLOW ---
        if auth_mode == "Sign Up":
            try:
                success = add_user(email, password)  # returns True or False

                if not success:
                    st.error("⚠️ Email already registered.")
                    st.stop()

                st.success("🎉 Account created successfully! Redirecting to Home...")

                # set session values
                st.session_state.update({
                    "email": email,
                    "usage_count": 0,
                    "subscribed": False,
                    "plan": "free",
                    "active_plan": "free",
                    "token_validated": True
                })

                res = requests.post(f"{BACKEND_URL}/generate-token", json={
                    "email": email,
                    "subscribed": False
                })

                if res.status_code == 200:
                    st.session_state["token"] = res.json()["token"]
                    cookies["token"] = st.session_state["token"]
                    cookies["email"] = st.session_state["email"]
                    cookies.save()
                    time.sleep(1)
                    st.switch_page("pages/Home.py")
                else:
                    st.error("⚠️ Signup succeeded but token generation failed.")
                    st.stop()

            except sqlite3.IntegrityError:
                st.error("⚠️ Email already registered.")
                st.stop()
            except Exception as e:
                st.error(f"⚠️ Unexpected error: {e}")
                st.stop()
        
        # --- LOGIN FLOW ---
        else:
            if authenticate_user(email, password):
                usage, subscribed, plan = get_user(email)
                st.session_state.update({
                    "email": email,
                    "usage_count": usage,
                    "subscribed": bool(subscribed),
                    "plan": plan,
                    "active_plan": "free",
                    "token_validated": True
                })

                res = requests.post(f"{BACKEND_URL}/generate-token", json={
                    "email": email,
                    "subscribed": bool(subscribed)
                })
                if res.status_code == 200:
                    st.session_state["token"] = res.json()["token"]
                    cookies["token"] = st.session_state["token"]
                    cookies["email"] = st.session_state["email"]
                    cookies.save()
                    time.sleep(1)
                    st.switch_page("pages/Home.py")
                else:
                    st.error("⚠️ Login succeeded but token generation failed.")
                    st.stop()
            else:
                st.error("❌ Invalid credentials.")
                st.stop()


    # --- GOOGLE OAUTH (Only show for Login mode) ---
    if auth_mode == "Login":
        st.markdown('<div class="divider">OR</div>', unsafe_allow_html=True)

        google_client_id = GOOGLE_CLIENT_ID
        google_client_secret = GOOGLE_CLIENT_SECRET
        # redirect_uri = f"{FRONTEND_DOMAIN}"
        redirect_uri = FRONTEND_DOMAIN.rstrip("/")

        # ✅ Ensure cookies are available
        if "cookie_manager" not in st.session_state:
            st.session_state["cookie_manager"] = get_cookie_manager()

        cookies = st.session_state["cookie_manager"] 
        
        # --- Initialize Google session state safely ---
        if "google_logged_in" not in st.session_state:
            st.session_state["google_logged_in"] = False
        
        query_params = st.query_params
        is_oauth_callback = "code" in query_params or "error" in query_params
            

        # Always (re)create the OAuth2 object safely
        if "oauth2" not in st.session_state:
            try:
                st.session_state["oauth2"] = OAuth2Component(
                    client_id=google_client_id,
                    client_secret=google_client_secret,
                    authorize_endpoint="https://accounts.google.com/o/oauth2/auth",
                    token_endpoint="https://oauth2.googleapis.com/token",
                    refresh_token_endpoint="https://oauth2.googleapis.com/token",
                    revoke_token_endpoint="https://oauth2.googleapis.com/revoke",
                )
                st.session_state["oauth_initialized"] = True
            except Exception as e:
                st.error(f"⚠️ Failed to initialize Google OAuth: {e}")

        oauth2 = st.session_state.get("oauth2", None)


        result = None
        if oauth2:   
            try:
                if "error" in query_params:
                    error = query_params.get("error")
                    if error == "access_denied":
                        st.warning("⚠️ Google login cancelled. Please try again if you want to continue.")
                    else:
                        st.error(f"⚠️ OAuth error: {error}")
                    
                    # Clear query params
                    st.query_params.clear()
                    if st.button("🔄 Try Again", key="oauth_retry"):
                        st.rerun()
                
                # Show button only if not in callback state
                elif not is_oauth_callback:
                    result = oauth2.authorize_button(
                        "Continue with Google",
                        redirect_uri=redirect_uri,
                        scope="openid email profile",
                        key="google_login_button",
                        use_container_width=True,
                        icon="https://cdn-icons-png.flaticon.com/512/281/281764.png",
                    )
                
                # Handle callback
                else:
                    # OAuth callback is being processed
                    result = oauth2.authorize_button(
                        "Continue with Google",
                        redirect_uri=redirect_uri,
                        scope="openid email profile",
                        key="google_login_button_callback",
                        use_container_width=True,
                        icon="https://cdn-icons-png.flaticon.com/512/281/281764.png",
                    )

            except Exception as e:
                error_msg = str(e)
                
                # ✅ Handle state mismatch error gracefully
                if "STATE" in error_msg and "DOES NOT MATCH" in error_msg:
                    st.warning("⚠️ Your login session expired. Please try again.")
                    
                    # Clear OAuth state
                    if "oauth2" in st.session_state:
                        del st.session_state["oauth2"]
                    if "oauth_initialized" in st.session_state:
                        del st.session_state["oauth_initialized"]
                    
                    # Clear query params
                    st.query_params.clear()
                    
                    if st.button("🔄 Restart Google Login", key="restart_oauth"):
                        st.rerun()
                        
                elif "OUT OF DATE" in error_msg:
                    st.info("⚠️ OAuth session timed out. Click below to restart.")
                    
                    # Clear OAuth state
                    if "oauth2" in st.session_state:
                        del st.session_state["oauth2"]
                    
                    # Clear query params
                    st.query_params.clear()
                    
                    if st.button("🔄 Restart Google Login", key="restart_oauth_timeout"):
                        st.rerun()
                        
                else:
                    st.error(f"⚠️ Google OAuth error: {error_msg}")
                    st.info("💡 Try refreshing the page or clearing your browser cache.")
                
                result = None

        # --- Handle OAuth response ---
        if result and "token" in result:
            access_token = result.get("token", {}).get("access_token") or result.get("access_token")
            if access_token:
                try:
                        
                    user_info_response = requests.get(
                        "https://www.googleapis.com/oauth2/v1/userinfo",
                        headers={"Authorization": f"Bearer {access_token}"},
                        timeout=10
                    )


                    if user_info_response.status_code != 200:
                        st.error(f"⚠️ Google API returned status {user_info_response.status_code}")
                        st.query_params.clear()
                        st.stop()
                    
                    user_info = user_info_response.json()
                    google_email = user_info.get("email")
                    
                    if google_email:
                        user = get_user(google_email)
                        if not user:
                            add_user(google_email, password="google_oauth")

                        usage, subscribed, plan = get_user(google_email) or (0, False, "free")
                        st.session_state.update({
                            "email": google_email,
                            "usage_count": usage,
                            "subscribed": bool(subscribed),
                            "plan": plan,
                            "active_plan": "free",
                            "token_validated": True,
                            "google_logged_in": True
                        })

                        res = requests.post(f"{BACKEND_URL}/generate-token", json={
                            "email": google_email,
                            "subscribed": bool(subscribed)
                        })
                        if res.status_code == 200:
                            st.session_state["token"] = res.json()["token"]
                            cookies["token"] = st.session_state["token"]
                            cookies["email"] = st.session_state["email"]
                            cookies.save()

                            st.success("✅ Google login successful! Redirecting...")
                            time.sleep(1)
                            st.switch_page("pages/Home.py")
                        else:
                            st.error("⚠️ Token generation failed.")

                except requests.exceptions.Timeout:
                    st.error("⚠️ Connection timeout. Please check your internet.")
                    st.query_params.clear()
                except requests.exceptions.RequestException as e:
                    st.error(f"⚠️ Network error: {str(e)}")
                    st.query_params.clear()
                except Exception as e:
                    import traceback
                    st.error(f"⚠️ Error: {type(e).__name__}: {str(e)}")
                    with st.expander("🐛 Full Error Details"):
                        st.code(traceback.format_exc())
                    st.query_params.clear()
                    if "oauth2" in st.session_state:
                        del st.session_state["oauth2"]
        
st.markdown("</div>", unsafe_allow_html=True)