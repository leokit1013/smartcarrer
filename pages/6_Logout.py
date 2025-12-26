import streamlit as st
import time
from tools import set_page_config_ui, hide_streamlit_ui, show_custom_loader, render_sidebar, hide_url_path, get_cookie_manager
# Apply global UI
set_page_config_ui("Logout", "✨")
hide_streamlit_ui()
# hide_url_path()
# show_custom_loader()
# Inject navigation
render_sidebar()
# --- Setup cookies manager ---
cookies = get_cookie_manager()

# --- Clear session state ---
# --- Clear Session ---
for key in ["token", "email", "plan", "usage_count", "subscribed", "oauth2", "_redirecting"]:
    st.session_state.pop(key, None)

# --- Clear Google Auth ---
st.session_state["google_logged_in"] = False

# --- Clear cookies ---
cookies["token"] = ""
cookies["email"] = ""
cookies.save()   # 🔑 must call to persist removal

# --- UI ---
st.success("✅ You have been logged out successfully.")
st.info("Redirecting you to login page...")
time.sleep(1)
st.switch_page("landing.py")