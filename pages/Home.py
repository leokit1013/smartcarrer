from import_python_packages import *
from tools import (
    update_usage, resume_builder_ui, get_user, set_page_config_ui, 
    hide_streamlit_ui, render_sidebar, hide_url_path, calculate_usage, 
    enforce_auth_and_session_mgmt, get_gemini_model, show_home_page_ui
)
from config import BACKEND_URL

# Apply global UI
set_page_config_ui("Smart Career Tools", "🏠")

# Inject SmartCareer.in branded CSS
show_home_page_ui()

hide_streamlit_ui()
auth_ok = enforce_auth_and_session_mgmt()
if not auth_ok:
    st.stop()
render_sidebar()

model = get_gemini_model()

# --- Sync user state from DB ---
if "usage_count" not in st.session_state or "subscribed" not in st.session_state:
    user_info = get_user(st.session_state.email)
    if user_info:
        st.session_state.usage_count = user_info[0]
        st.session_state.subscribed = bool(user_info[1])
    else:
        st.error("User not found. Please login again.")
        st.switch_page("pages/Login.py")

# --- Gatekeeper Function ---
def usage_gate():
    if st.session_state.subscribed:
        return True
    elif st.session_state.usage_count < 2:  # free usage limit
        update_usage(st.session_state.email)
        st.session_state.usage_count += 1
        return True
    else:
        return False

def navigate_with_check(page_path):
    if usage_gate():
        st.switch_page(page_path)
    else:
        st.warning("⚠️ You've used your 2 free accesses. Please subscribe to continue.")
        st.switch_page("pages/payment.py")

resume_builder_ui()

# --- Hero Section ---
username = st.session_state.email.split('@')[0].title()
st.markdown(f"""
<div class="hero-banner">
    <div class="welcome-badge">👋 Welcome Back, {username}!</div>
    <div class="hero-title">Smart Career Tools</div>
    <div class="hero-subtitle">Your AI-powered suite for career growth and professional success</div>
    <div class="stats-bar">
        <div class="stat-item">
            <div class="stat-value">4</div>
            <div class="stat-label">Powerful Tools</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{st.session_state.usage_count}</div>
            <div class="stat-label">Tools Used</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">{'∞' if st.session_state.subscribed else '2'}</div>
            <div class="stat-label">Access Limit</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Section Title ---
st.markdown('<div class="section-title">🚀 Choose Your Tool</div>', unsafe_allow_html=True)

# --- Tool Cards ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">📝</div>
        <div class="tool-title">Create Resume From Scratch</div>
        <div class="tool-desc">Craft professional resumes from zero using AI-enhanced insights and smart suggestions.</div>
        <div class="tool-btn">
    """, unsafe_allow_html=True)
    if st.button("🚀 Start Creating", key="tool1", use_container_width=True):
        navigate_with_check("pages/1_Create_Resume_From_Scratch.py")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">✨</div>
        <div class="tool-title">Enhance Existing Resume</div>
        <div class="tool-desc">Improve your existing resume for better ATS ranking and professional appeal.</div>
        <div class="tool-btn">
    """, unsafe_allow_html=True)
    if st.button("⚡ Enhance Now", key="tool2", use_container_width=True):
        navigate_with_check("pages/2_Enhance_Existing_Resume.py")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">🛠</div>
        <div class="tool-title">Check & Fix Against JD</div>
        <div class="tool-desc">Optimize your resume against a specific job description for maximum impact.</div>
        <div class="tool-btn">
    """, unsafe_allow_html=True)
    if st.button("🔍 Match to JD", key="tool3", use_container_width=True):
        navigate_with_check("pages/3_Check_And_Fix_Against_JD.py")
    st.markdown("</div></div>", unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">🎨</div>
        <div class="tool-title">Resume Templates</div>
        <div class="tool-desc">Browse and apply professional resume templates to give your CV a polished look.</div>
        <div class="tool-btn">
    """, unsafe_allow_html=True)
    if st.button("📑 Choose Template", key="tool4", use_container_width=True):
        navigate_with_check("pages/7_Resume_Builder.py")
    st.markdown("</div></div>", unsafe_allow_html=True)

# --- Features Section ---
st.markdown("""
<div class="features-section">
    <div class="section-title" style="margin-top: 0;">✨ Why Choose SmartCareer.in?</div>
    <div class="feature-grid">
        <div class="feature-item">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered</div>
            <div class="feature-desc">Advanced AI algorithms optimize your resume for maximum impact</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">ATS Optimized</div>
            <div class="feature-desc">Pass through Applicant Tracking Systems with confidence</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Lightning Fast</div>
            <div class="feature-desc">Generate professional resumes in seconds, not hours</div>
        </div>
        <div class="feature-item">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Secure & Private</div>
            <div class="feature-desc">Your data is encrypted and never shared with third parties</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- CTA Section ---
if not st.session_state.subscribed:
    st.markdown("""
    <div class="cta-section">
        <div class="cta-title">🚀 Ready to Supercharge Your Career?</div>
        <div class="cta-subtitle">Upgrade to Premium and unlock unlimited access to all tools</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💎 Upgrade to Premium", use_container_width=True, type="primary"):
            st.switch_page("pages/payment.py")

# --- Footer ---
st.markdown("""
<div class="footer">
    <div class="footer-title">SmartCareer.in</div>
    <p style="font-size: 1.1rem; margin: 1rem 0;">Empowering professionals to achieve their career goals</p>
    <div class="footer-links">
        <a href="https://smartcareer.in/about" class="footer-link" target="_blank">About Us</a>
        <a href="https://smartcareer.in/privacy" class="footer-link" target="_blank">Privacy Policy</a>
        <a href="https://smartcareer.in/terms" class="footer-link" target="_blank">Terms of Service</a>
        <a href="https://smartcareer.in/contact" class="footer-link" target="_blank">Contact</a>
    </div>
    <p style="font-size: 0.85rem; color: #9CA3AF; margin-top: 2rem;">
        © 2025 SmartCareer.in - All rights reserved
    </p>
</div>
""", unsafe_allow_html=True)