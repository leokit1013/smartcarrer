import streamlit as st
import hashlib
import time
def render_sidebar():
    """Centralized sidebar navigation"""
    with st.sidebar:
        st.title("📂 Navigation")
        st.page_link("pages/Home.py", label="🏠 Dashboard")
        st.page_link("pages/1_Create_Resume_From_Scratch.py", label="📝 Create Resume")
        st.page_link("pages/2_Enhance_Existing_Resume.py", label="✨ Enhance Resume")
        st.page_link("pages/3_Check_And_Fix_Against_JD.py", label="🛠 Fix Against JD")
        st.page_link("pages/7_Resume_Builder.py", label="🎨 Resume Templates")
        st.page_link("pages/payment.py", label="🚪 Payment")
        st.page_link("pages/6_Logout.py", label="🚪 Logout")
        # st.sidebar.page_link("pages/6_Logout.py", label="🚪 Logout")


def hide_url_path():
    """
    Hide URL paths in the browser tab for Streamlit multi-page apps.
    Keeps the URL clean while navigating between pages.
    """
    # Use JavaScript to remove the path from the URL without reloading
    st.markdown(
        """
        <script>
        if (window.history.replaceState) {
            window.history.replaceState(null, null, window.location.origin + window.location.pathname);
        }
        </script>
        """,    
        unsafe_allow_html=True
    )
        
def set_page_config_ui(page_title="AI Resume Pro", page_icon="static/favicon.png", layout="wide", initial_sidebar_state="expanded"):
    """
    Apply global UI settings across all pages.
    Includes: page config, hiding Streamlit UI, custom CSS.
    """

    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state
    )

def hide_streamlit_ui():
    # Inject CSS
    hide_st_style = """
        <style>
        /* Hide Streamlit default UI */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        
        /* Forcefully remove deploy + toolbar instantly */
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],

        
        /* Hide Streamlit’s built-in sidebar nav + collapse button */
        [data-testid="stSidebarNav"]  {display: block !important;} 
        [data-testid="stSidebarCollapseButton"]  {display: block !important;} 
        /* [data-testid="collapsedControl"]  {display: none !important;} */
        
        /* Hide deploy button */
        [data-testid="stDeployButton"] {display: none !important;}
        [data-testid="stAppDeployButton"] {display: none !important;}
 
        /* Hide "Press Enter to apply" helper text. This removes all inline helper <p> texts in inputs. */
        /* [data-testid="stMarkdownContainer"] p {display: none !important;} */
        
        /* Hide only the press-enter-to-apply helper text */
        div[data-testid="stTextInputInstructions"] {display: none !important;}

        /* Fix sidebar width so no flicker */
        section[data-testid="stSidebar"] {
            min-width: 250px !important;
            max-width: 250px !important;
        }
        </style>
         
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def show_login_page():
    
    # --- Steamlit login UI ---
    login_page_view = """
        <style>
        body {
            background: linear-gradient(135deg, #d9a7c7 0%, #fffcdc 100%);
            font-family: 'Segoe UI', sans-serif;
        }
        /* Center Card with Glass Effect */
        .login-card {
            max-width: 420px;
            margin: 60px auto;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            backdrop-filter: blur(12px);
            padding: 2rem 2.2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
            text-align: center;
            transition: all 0.3s ease-in-out;
        }

        .login-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);
        }
        .login-icon {
            font-size: 48px;
            background: linear-gradient(90deg, #8a4fff, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            text-align: center;   
        }
        .login-title {
            font-size: 1.6rem;
            font-weight: 700;
            color: #111;
            text-align: center;   
        }
        .login-subtitle {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1.5rem;
            text-align: center;   
        }
        .tab-container {
            display: flex;
            justify-content: center;
            margin-bottom: 1.5rem;
        }
        .tab-btn {
            flex: 1;
            padding: 10px;
            border: none;
            cursor: pointer;
            font-weight: 600;
            border-radius: 8px;
            margin: 0 5px;
            transition: all 0.2s ease;
        }
        .tab-active {
            background: #111;
            color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        .tab-inactive {
            background: #f1f1f1;
            color: #555;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 10px;
            
        }
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            padding: 12px;
            font-weight: bold;
            background: linear-gradient(90deg, #8a4fff, #4facfe);
            color: white;
            border: none;
            margin-top: 1rem;
            text-align: center;   
        }
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            color: #aaa;
            margin: 20px 0;
        }
        .divider::before, .divider::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #ddd;
        }
        .divider:not(:empty)::before { margin-right: 10px; }
        .divider:not(:empty)::after { margin-left: 10px; }
        .social-btns {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-btn {
            flex: 1;
            border: none;
            border-radius: 8px;
            padding: 10px;
            background: #fff;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            cursor: pointer;
            font-weight: 600;
        }
        

    .login-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        padding: 20px;
    }

    .login-container {
        display: flex;
        flex-wrap: wrap;
        max-width: 950px;
        width: 100%;
        background: white;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        overflow: hidden;
    }

    /* LEFT SIDE */
    .login-left {
        flex: 1;
        min-width: 300px;
        background: linear-gradient(135deg, #8a4fff, #4facfe);
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        text-align: center;
    }

    .login-left img {
        width: 100%;
        max-width: 300px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(255,255,255,0.25);
        margin-bottom: 1rem;
    }

    .login-left h2 {
        font-size: 1.6rem;
        margin-bottom: 0.5rem;
    }

    .login-left p {
        color: rgba(255,255,255,0.9);
        font-size: 0.95rem;
        max-width: 280px;
    }

    /* RIGHT SIDE */
    .login-right {
        flex: 1;
        min-width: 320px;
        background: #ffffff;
        padding: 2.5rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .login-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #111;
        margin-bottom: 0.25rem;
    }

    .login-subtext {
        color: #666;
        margin-bottom: 1.5rem;
    }

    /* --- Streamlit Inputs Styling --- */
    .stTextInput > div > div > input {
        border-radius: 8px !important;
        border: 1px solid #ccc !important;
        padding: 10px !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 8px;
        padding: 12px;
        font-weight: bold;
        background: linear-gradient(90deg, #8a4fff, #4facfe);
        color: white;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(79, 172, 254, 0.4);
    }

    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        color: #aaa;
        margin: 20px 0;
    }

    .divider::before, .divider::after {
        content: "";
        flex: 1;
        border-bottom: 1px solid #ddd;
    }

    .divider:not(:empty)::before { margin-right: 10px; }
    .divider:not(:empty)::after { margin-left: 10px; }


    /* Responsive */
    @media (max-width: 480px) {
        .login-card {
            margin: 30px 10px;
            padding: 1.5rem;
        }
        .login-container {
        flex-direction: column;
        }
        .login-title { font-size: 1.5rem; }
        .login-subtitle { font-size: 0.85rem; }
    }
        </style>
    """
    st.markdown(login_page_view, unsafe_allow_html=True)



def show_home_page_ui():
    # --- Steamlit Home UI ---
    home_page_view ="""

    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main Container */
        .main {
            background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
            padding: 0 !important;
        }
        
        .block-container {
            padding: 2rem 3rem !important;
            max-width: 1400px !important;
        }
        
        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 50%, #60A5FA 100%);
            padding: 3rem 2.5rem;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 3rem;
            box-shadow: 0 20px 60px rgba(30, 64, 175, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .hero-banner::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 15s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(-5%, -5%) scale(1.1); }
        }
        
        .welcome-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1.5rem;
            border-radius: 50px;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 1rem;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 900;
            margin: 1rem 0 0.75rem;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            letter-spacing: -1px;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            font-weight: 400;
            opacity: 0.95;
            margin-bottom: 2rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Stats Bar */
        .stats-bar {
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin-top: 2rem;
            position: relative;
            z-index: 1;
        }
        
        .stat-item {
            text-align: center;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 1.25rem 2rem;
            border-radius: 15px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            min-width: 140px;
            transition: all 0.3s ease;
        }
        
        .stat-item:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.3);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }
        
        .stat-value {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 0.25rem;
            color: white;
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            font-weight: 500;
        }
        
        /* Section Title */
        .section-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #1E40AF;
            text-align: center;
            margin: 3rem 0 2.5rem;
            position: relative;
        }
        
        .section-title::after {
            content: '';
            display: block;
            width: 100px;
            height: 4px;
            background: linear-gradient(90deg, #3B82F6, #60A5FA);
            margin: 1rem auto 0;
            border-radius: 2px;
        }
        
        /* Tool Cards */
        .tool-card {
            background: white;
            border-radius: 18px;
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 2px solid transparent;
            height: 100%;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }
        
        .tool-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #1E40AF, #3B82F6, #60A5FA);
            transform: scaleX(0);
            transition: transform 0.3s ease;
        }
        
        .tool-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(30, 64, 175, 0.15);
            border-color: #3B82F6;
        }
        
        .tool-card:hover::before {
            transform: scaleX(1);
        }
        
        .tool-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .tool-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 0.75rem;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .tool-desc {
            font-size: 0.95rem;
            color: #6B7280;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            flex-grow: 1;
        }
        
        .tool-btn {
            margin-top: auto;
        }
        
        /* Streamlit Button Styling */
        .stButton button {
            border-radius: 12px !important;
            font-weight: 600 !important;
            padding: 0.75rem 1.5rem !important;
            border: none !important;
            transition: all 0.3s ease !important;
            font-size: 0.95rem !important;
        }
        
        .tool-card .stButton button {
            background: linear-gradient(135deg, #1E40AF, #3B82F6) !important;
            color: white !important;
            width: 100% !important;
            box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3) !important;
        }
        
        .tool-card .stButton button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(30, 64, 175, 0.4) !important;
        }
        
        /* Features Section */
        .features-section {
            background: white;
            padding: 3rem 2.5rem;
            border-radius: 20px;
            margin: 4rem 0;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2.5rem;
        }
        
        .feature-item {
            text-align: center;
            padding: 2rem 1.5rem;
            background: linear-gradient(135deg, #F9FAFB, #F3F4F6);
            border-radius: 15px;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .feature-item:hover {
            transform: translateY(-5px);
            background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
            border-color: #3B82F6;
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15);
        }
        
        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .feature-title {
            font-size: 1.2rem;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 0.5rem;
        }
        
        .feature-desc {
            font-size: 0.95rem;
            color: #6B7280;
            line-height: 1.5;
        }
        
        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            padding: 3rem 2.5rem;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin: 4rem 0 3rem;
            box-shadow: 0 20px 60px rgba(16, 185, 129, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .cta-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
            animation: pulse 10s ease-in-out infinite;
        }
        
        .cta-title {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
        }
        
        .cta-subtitle {
            font-size: 1.2rem;
            opacity: 0.95;
            margin-bottom: 2rem;
            position: relative;
            z-index: 1;
        }
        
        .cta-section .stButton button {
            background: white !important;
            color: #059669 !important;
            font-size: 1.1rem !important;
            padding: 1rem 3rem !important;
            font-weight: 700 !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2) !important;
        }
        
        .cta-section .stButton button:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Footer */
        .footer {
            background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
            color: white;
            padding: 3rem 2.5rem 2rem;
            border-radius: 20px;
            text-align: center;
            margin-top: 4rem;
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.1);
        }
        
        .footer-title {
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #60A5FA, #3B82F6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .footer-link {
            color: #D1D5DB;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 0.5rem 1rem;
            border-radius: 8px;
        }
        
        .footer-link:hover {
            color: #60A5FA;
            background: rgba(96, 165, 250, 0.1);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .hero-subtitle {
                font-size: 1.1rem;
            }
            
            .stats-bar {
                flex-direction: column;
                gap: 1rem;
            }
            
            .stat-item {
                margin: 0 auto;
            }
            
            .section-title {
                font-size: 1.8rem;
            }
            
            .tool-title {
                font-size: 1.1rem;
                min-height: auto;
            }
            
            .cta-title {
                font-size: 2rem;
            }
            
            .footer-links {
                flex-direction: column;
                gap: 1rem;
            }
        }
        
        /* Loading Animation */
        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }
        
        /* Success/Warning Styling */
        .stAlert {
            border-radius: 12px !important;
            border-left: 4px solid !important;
            font-weight: 500 !important;
        }
    </style>
    """
       
    st.markdown(home_page_view, unsafe_allow_html=True)





def show_custom_loader(animation_gif=None, duration=1500):
    """
    Show loader once per page load with fade-out.
    Prevents reappearing on Streamlit reruns.
    """
    try:
        script_path = st.runtime.scriptrunner.get_script_run_ctx().script_path
        page_key = hashlib.md5(script_path.encode()).hexdigest()[:8]
    except Exception:
        page_key = "global"

    loader_key = f"loader_shown_{page_key}"

    # ✅ Show loader only once for this session + page
    if st.session_state.get(loader_key, False):
        return
    st.session_state[loader_key] = True

    overlay_id = f"smartcareer-loader-{page_key}"

    # ---------- Loader HTML (spinner or GIF) ----------
    if animation_gif:
        content = f'<img src="{animation_gif}" class="loader-image" alt="Loading...">'
    else:
        content = f'<div class="spinner"></div>'

    loader_html = f"""
    <style>
        #{overlay_id} {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background: rgba(255, 255, 255, 0.98);
            z-index: 999999;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: opacity 0.5s ease-out;
        }}
        #{overlay_id}.fade-out {{
            opacity: 0;
            pointer-events: none;
        }}
        .spinner {{
            border: 8px solid #E5E7EB;
            border-top: 8px solid #1E40AF;
            border-right: 8px solid #3B82F6;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            animation: spin 1s linear infinite;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>

    <div id="{overlay_id}">
        {content}
        <div style="margin-top:20px; color:#1E40AF; font-size:18px; font-weight:600;">
            Loading SmartCareer.in...
        </div>
    </div>

    <script>
        const overlay = document.getElementById('{overlay_id}');
        if (overlay) {{
            document.body.style.overflow = 'hidden';
            setTimeout(() => {{
                overlay.classList.add('fade-out');
                setTimeout(() => {{
                    overlay.remove();
                    document.body.style.overflow = '';
                }}, 600);
            }}, {duration});
        }}
    </script>
    """

    st.markdown(loader_html, unsafe_allow_html=True)
    time.sleep(duration / 1000)  # small pause before removing loader


       
"""
Modern Payment UI Functions
Add these functions to your tools.py or create a new file payment_ui_functions.py
"""

def inject_modern_payment_css():
    """
    Injects modern CSS for payment pages with glassmorphism, gradients, and animations.
    Call this at the top of your payment pages.
    """
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Main container styling */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1200px;
    }
    
    /* Modern card container */
    .payment-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        margin: 2rem 0;
        animation: slideUp 0.6s ease-out;
    }
    
    /* Glassmorphic plan cards */
    .plan-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .plan-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.15);
    }
    
    .plan-card.featured {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid #fbbf24;
        box-shadow: 0 8px 32px rgba(251, 191, 36, 0.4);
    }
    
    .plan-card.featured:hover {
        background: rgba(255, 255, 255, 1);
        box-shadow: 0 12px 48px rgba(251, 191, 36, 0.5);
    }
    
    /* Price styling */
    .price-tag {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 1rem 0;
    }
    
    .featured .price-tag {
        background: linear-gradient(135deg, #f59e0b 0%, #dc2626 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Feature list styling */
    .feature-item {
        display: flex;
        align-items: center;
        padding: 0.75rem 0;
        color: #1f2937;
        font-size: 1rem;
    }
    
    .feature-item::before {
        content: "✓";
        display: inline-block;
        width: 24px;
        height: 24px;
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        border-radius: 50%;
        text-align: center;
        line-height: 24px;
        margin-right: 12px;
        font-weight: bold;
    }
    
    /* Custom button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Featured plan button */
    .featured-button button {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%) !important;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.4) !important;
    }
    
    .featured-button button:hover {
        background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%) !important;
        box-shadow: 0 6px 25px rgba(251, 191, 36, 0.6) !important;
    }
    
    /* Radio button customization */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.9);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Success/Warning boxes */
    .stSuccess, .stWarning, .stInfo {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid;
        backdrop-filter: blur(10px);
    }
    
    /* Animations */
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    @keyframes shimmer {
        0% {
            background-position: -1000px 0;
        }
        100% {
            background-position: 1000px 0;
        }
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
    }
    
    /* Loading animation */
    .loading-spinner {
        width: 50px;
        height: 50px;
        border: 4px solid rgba(255, 255, 255, 0.3);
        border-top-color: #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 2rem auto;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Toggle switch styling */
    .plan-toggle {
        display: flex;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 50px;
        margin: 2rem auto;
        width: fit-content;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Title styling */
    h1 {
        color: white !important;
        text-align: center;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    h2, h3 {
        color: #1f2937 !important;
        font-weight: 600 !important;
    }
    
    /* Payment status container */
    .payment-status {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
        border: 2px solid #10b981;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        animation: pulse 2s infinite;
    }
    </style>
    """, unsafe_allow_html=True)


def render_plan_header(title="Choose Your Plan", subtitle="Select the perfect plan for your needs"):
    """
    Renders an attractive header for the payment page.
    
    Args:
        title: Main heading text
        subtitle: Subtitle text
    """
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="margin-bottom: 0.5rem;">{title}</h1>
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.25rem; font-weight: 400;">
            {subtitle}
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_plan_toggle():
    """
    Renders a Monthly/Yearly toggle switch (visual only - functionality needs to be implemented).
    Returns the HTML for a toggle, you can enhance this with actual toggle logic.
    """
    st.markdown("""
    <div class="plan-toggle">
        <span style="font-weight: 600; color: #667eea;">Monthly</span>
        <label style="position: relative; display: inline-block; width: 60px; height: 30px;">
            <input type="checkbox" style="opacity: 0; width: 0; height: 0;">
            <span style="position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; 
                         background-color: #667eea; border-radius: 30px; transition: .4s;"></span>
        </label>
        <span style="font-weight: 600; color: #6b7280;">Yearly</span>
        <span style="background: #10b981; color: white; padding: 0.25rem 0.75rem; 
                     border-radius: 12px; font-size: 0.875rem; font-weight: 600;">Save 20%</span>
    </div>
    """, unsafe_allow_html=True)


def render_plan_card(plan_name, price, period, features, is_featured=False, button_text="Get Started"):
    
    """
    Renders a single plan card with modern design.

    Args:
        plan_name: Name of the plan (e.g., "Basic", "Professional")
        price: Price amount (e.g., "9", "29", "99")
        period: Billing period (e.g., "month", "year")
        features: List of feature strings
        is_featured: Boolean, adds special styling if True
        button_text: Text for the action button

    Returns:
        HTML string for the plan card
    """

    # Ensure features is always a list
    if not features or not isinstance(features, list):
        features = ["No features available"]

    featured_class = "featured" if is_featured else ""


    features_html = "".join(
        f'<div class="feature-item">{feature}</div>' for feature in features
    )

    return f"""
    <div class="plan-card {featured_class}" style="border:1px solid #ddd; padding:1rem; border-radius:8px; background:#fff; margin-bottom:1rem;">
        <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem; color: #1f2937;">{plan_name}</h3>
        <div class="price-tag" style="font-weight:bold;">₹{price}<span style="font-size: 1.25rem; color: #6b7280;">/{period}</span></div>
        <div style="margin: 1.5rem 0;">
            {features_html}
        </div>

    </div>
    """



def render_payment_status_card(status="processing", message="Processing your payment..."):
    """
    Renders a status card for payment processing/success/failure.
    
    Args:
        status: One of "processing", "success", "error"
        message: Status message to display
    """
    icons = {
        "processing": "🔄",
        "success": "✅",
        "error": "❌"
    }
    
    colors = {
        "processing": "#3b82f6",
        "success": "#10b981",
        "error": "#ef4444"
    }
    
    icon = icons.get(status, "🔄")
    color = colors.get(status, "#3b82f6")
    
    st.markdown(f"""
    <div class="payment-status" style="border-color: {color}; background: linear-gradient(135deg, rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1), rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.05));">
        <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
        <h2 style="color: {color} !important; margin-bottom: 0.5rem;">{message}</h2>
        <div class="loading-spinner"></div>
    </div>
    """, unsafe_allow_html=True)


def render_success_animation():
    """
    Renders a beautiful success animation for payment completion.
    """
    st.markdown("""
    <div style="text-align: center; padding: 3rem;">
        <div style="font-size: 6rem; animation: pulse 1s ease-in-out;">🎉</div>
        <h1 style="color: #10b981 !important; margin: 1rem 0;">Payment Successful!</h1>
        <p style="color: white; font-size: 1.25rem;">Your subscription has been activated</p>
        <div style="margin-top: 2rem;">
            <div style="width: 60px; height: 60px; border: 4px solid rgba(16, 185, 129, 0.3); 
                        border-top-color: #10b981; border-radius: 50%; animation: spin 1s linear infinite; 
                        margin: 0 auto;"></div>
            <p style="color: rgba(255, 255, 255, 0.8); margin-top: 1rem;">Redirecting to dashboard...</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_cancel_message():
    """
    Renders a cancellation message with modern styling.
    """
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); 
                border-radius: 24px; padding: 3rem; text-align: center; 
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3); margin: 2rem 0;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">😔</div>
        <h2 style="color: #f59e0b; margin-bottom: 1rem;">Payment Cancelled</h2>
        <p style="color: #6b7280; font-size: 1.1rem; line-height: 1.6;">
            Your payment was cancelled. No charges were made to your account.
        </p>
        <p style="color: #6b7280; font-size: 1.1rem; margin-top: 1rem;">
            You can return to the subscription page whenever you're ready.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_current_plan_badge(plan_name, usage, limit):
    """
    Renders a badge showing current plan status.
    
    Args:
        plan_name: Current plan name
        usage: Current usage count
        limit: Usage limit
    """
    percentage = (usage / limit * 100) if limit > 0 else 0
    
    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.9); border-radius: 16px; padding: 1.5rem; 
                margin: 1rem 0; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
                <span style="color: #6b7280; font-size: 0.875rem;">Current Plan</span>
                <h3 style="color: #1f2937; margin: 0.25rem 0; text-transform: capitalize;">{plan_name}</h3>
            </div>
            <div style="text-align: right;">
                <span style="color: #6b7280; font-size: 0.875rem;">Usage</span>
                <h3 style="color: #1f2937; margin: 0.25rem 0;">{usage} / {limit}</h3>
            </div>
        </div>
        <div style="background: #e5e7eb; height: 8px; border-radius: 4px; overflow: hidden;">
            <div style="background: linear-gradient(90deg, #667eea, #764ba2); 
                        height: 100%; width: {percentage}%; transition: width 0.3s ease;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# Custom CSS for Enhance Existing Resume Page
# ============================================
def enhance_existing_resume_ui():
        
    st.markdown("""
    <style>
        /* Main container */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        /* Header section */
        .header-section {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            margin-bottom: 2rem;
            color: white;
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .header-subtitle {
            font-size: 1.1rem;
            opacity: 0.95;
            max-width: 600px;
            margin: 0 auto;
        }
        
        /* Upload section */
        .upload-section {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }
        
        /* Result section */
        .result-container {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 2rem;
            margin-top: 2rem;
            border-left: 4px solid #667eea;
        }
        
        .resume-content {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            line-height: 1.8;
            font-size: 15px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        
        .resume-content h1, .resume-content h2, .resume-content h3 {
            color: #667eea;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }
        
        .resume-content strong {
            color: #2d3748;
            font-weight: 600;
        }
        
        /* Download buttons */
        .download-section {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }
        
        /* Info cards */
        .info-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
        }
        
        .info-card h4 {
            color: #2d3748;
            margin-bottom: 0.5rem;
        }
        
        /* Feature list */
        .feature-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .feature-item {
            background: white;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            border-left: 3px solid #667eea;
        }
        
        .feature-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .feature-title {
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 0.3rem;
        }
    </style>
    """, unsafe_allow_html=True)


# ============================================
# Custom CSS for Check and Fix Against Job Description Page
# ============================================

def check_and_fix_against_job_description_ui():
    """Inject modern custom CSS for SmartCareer branding"""
    st.markdown("""
        <style>
        /* SmartCareer Color Scheme */
        :root {
            --primary-color: #00BFA5;
            --secondary-color: #1E88E5;
            --accent-color: #FF6F00;
            --success-color: #00C853;
            --warning-color: #FFB300;
            --error-color: #DD2C00;
            --bg-light: #F5F7FA;
            --text-dark: #212121;
        }
        
        /* Main container styling */
        .main-header {
            background: linear-gradient(135deg, #00BFA5 0%, #1E88E5 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Card styling */
        .card {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--primary-color);
        }
        
        /* Score display */
        .score-display {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #00BFA5 0%, #00E5CC 100%);
            border-radius: 15px;
            color: white;
            margin: 1.5rem 0;
        }
        
        .score-number {
            font-size: 4rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Metric cards */
        .metric-card {
            background: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.2s;
        }
        
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        /* Recommendation list */
        .recommendation-item {
            background: #F8F9FA;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 0.75rem;
            border-left: 3px solid var(--secondary-color);
        }
        
        /* Progress bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #00BFA5 0%, #1E88E5 100%);
        }
        
        /* Buttons */
        .stButton > button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        /* File uploader */
        .stFileUploader {
            border: 2px dashed var(--primary-color);
            border-radius: 10px;
            padding: 1rem;
        }
        
        /* Text areas */
        .stTextArea textarea {
            border-radius: 8px;
            border: 1px solid #E0E0E0;
        }
        
        /* Step indicators */
        .step-indicator {
            display: inline-block;
            background: var(--primary-color);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)


def create_resume_from_scratch_ui():
    """Enhanced SmartCareer.in brand styling with improved layout"""
    st.markdown("""
    <style>
        :root {
            --primary-blue: #1E40AF;
            --secondary-blue: #3B82F6;
            --success-green: #10B981;
            --light-bg: #EFF6FF;
            --text-dark: #1F2937;
            --border-gray: #E5E7EB;
        }
        
        /* Main Header */
        .main-header {
            background: linear-gradient(135deg, #1E40AF, #3B82F6);
            padding: 2.5rem;
            border-radius: 16px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 8px 20px rgba(30, 64, 175, 0.25);
        }
        
        .main-header h1 {
            color: white;
            margin: 0;
            font-size: 2.8rem;
            font-weight: 700;
        }
        
        .main-header p {
            color: rgba(255,255,255,0.95);
            margin: 0.75rem 0 0;
            font-size: 1.1rem;
        }
        
        /* Enhanced Large Tab Navigation */
        .stRadio {
            background: white;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            margin-bottom: 2.5rem;
        }

        .stRadio > div {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .stRadio > div > label {
            background: #F9FAFB;
            padding: 2.75rem 3.75rem !important;
            border-radius: 16px;
            font-weight: 900;
            font-size: 1.35rem;
            transition: all 0.3s ease;
            cursor: pointer;
            border: 3px solid transparent;
            min-width: 240px;
            text-align: center;
        }

        .stRadio > div > label:hover {
            background: #EFF6FF;
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(59, 130, 246, 0.15);
        }

        .stRadio > div > label:has(input:checked) {
            background: linear-gradient(135deg, #1E40AF, #3B82F6) !important;
            color: white !important;
            border-color: #1E40AF;
            box-shadow: 0 8px 20px rgba(30, 64, 175, 0.35);
            transform: translateY(-4px);
        }

        
        /* Progress Indicators */
        .progress-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 2rem 0;
            gap: 8px;
        }
        
        .progress-step {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #D1D5DB;
            transition: all 0.3s ease;
        }
        
        .progress-step.active {
            background: #3B82F6;
            width: 40px;
            height: 12px;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.4);
        }
        
        .progress-step.completed {
            background: #10B981;
            box-shadow: 0 2px 6px rgba(16, 185, 129, 0.3);
        }
        
        /* Step Sections */
        .step-section {
            background: white;
            padding: 2.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
        }
        
        .step-section h2 {
            color: var(--primary-blue);
            margin-top: 0;
            font-size: 2rem;
            font-weight: 700;
        }
        
        /* Enhanced Preview Box */
        .preview-container {
            background: linear-gradient(135deg, #ffffff, #f8fafc);
            border-radius: 16px;
            margin: 2rem 0;
        }
        
        .preview-header {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
            border-radius: 12px;
            margin-bottom: 2rem;
        }
        
        .preview-section {
            background: white;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--secondary-blue);
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        
        .preview-section h3 {
            color: var(--primary-blue);
            font-size: 1.4rem;
            margin-top: 0;
            margin-bottom: 1rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Skills Grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .skill-badge {
            background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            color: var(--primary-blue);
            border: 1px solid #BFDBFE;
            transition: all 0.3s ease;
        }
        
        .skill-badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(59, 130, 246, 0.2);
        }
        
        /* Experience/Education Cards */
        .experience-card {
            background: #F9FAFB;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1.25rem;
            border-left: 3px solid var(--secondary-blue);
        }
        
        .experience-card h4 {
            color: var(--text-dark);
            margin: 0 0 0.5rem 0;
            font-size: 1.2rem;
            font-weight: 700;
        }
        
        .experience-meta {
            color: #6B7280;
            font-style: italic;
            margin-bottom: 0.75rem;
            font-size: 0.95rem;
        }
        
        /* Success Box */
        .success-box {
            background: linear-gradient(135deg, #D1FAE5, #A7F3D0);
            border-left: 5px solid #10B981;
            padding: 1.25rem;
            border-radius: 10px;
            color: #065F46;
            margin: 1.5rem 0;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
        }
        
        /* Auto-save indicator */
        .auto-save {
            background: linear-gradient(135deg, #DBEAFE, #BFDBFE);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            border-left: 4px solid var(--secondary-blue);
        }
        
        /* Input Fields */
        .stTextInput input, .stTextArea textarea {
            border-radius: 8px !important;
            border: 2px solid #E5E7EB !important;
            padding: 0.75rem !important;
            font-size: 1rem !important;
        }
        
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: var(--secondary-blue) !important;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
        }
        
        /* Buttons */
        .stButton button {
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.75rem 1.5rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, #1E40AF, #3B82F6) !important;
            box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3) !important;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(30, 64, 175, 0.4) !important;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background: #F9FAFB;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 1rem !important;
        }
        
        /* Download section */
        .download-section {
            background: linear-gradient(135deg, #F0F9FF, #E0F2FE);
            padding: 2rem;
            border-radius: 12px;
            margin-top: 2rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, #F9FAFB, #F3F4F6);
            border-radius: 12px;
            margin-top: 3rem;
            border-top: 3px solid var(--secondary-blue);
        }
    </style>
    """, unsafe_allow_html=True)
    

# SmartCareer.in Custom CSS
def resume_builder_ui():
    st.markdown("""
    <style>
    /* SmartCareer.in Brand Colors & Modern UI */
    :root {
        --primary-blue: #1E40AF;
        --secondary-blue: #3B82F6;
        --light-blue: #DBEAFE;
        --success-green: #10B981;
        --warning-orange: #F59E0B;
        --text-dark: #1F2937;
        --text-light: #6B7280;
        --bg-light: #F9FAFB;
        --border-color: #E5E7EB;
    }
    
    /* Main Container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 10px 40px rgba(30, 64, 175, 0.2);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.95;
        font-weight: 400;
    }
    
    /* Step Cards */
    .step-card {
        background: white;
        border-radius: 16px;
        margin-bottom: 2.5rem;
        border: 2px solid var(--border-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .step-card:hover {
        box-shadow: 0 12px 24px rgba(30, 64, 175, 0.15);
        border-color: var(--secondary-blue);
        transform: translateY(-2px);
    }
    
    .step-header {
        display: flex;
        align-items: center;
        margin-bottom: 2rem;
        padding-bottom: 1.5rem;
        border-bottom: 3px solid var(--light-blue);
    }
    
    .step-number {
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        color: white;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 700;
        margin-right: 1.5rem;
        box-shadow: 0 6px 16px rgba(30, 64, 175, 0.4);
        flex-shrink: 0;
    }
    
    .step-title {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-dark);
        margin: 0;
    }
    
    /* Template Cards */
    .template-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border: 2px solid var(--border-color);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .template-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 32px rgba(30, 64, 175, 0.2);
        border-color: var(--primary-blue);
    }
    
    .template-name {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin: 1rem 0 0.5rem 0;
    }
    
    .template-description {
        color: var(--text-light);
        font-size: 0.95rem;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    
    .ats-badge {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        display: inline-block;
        box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(30, 64, 175, 0.4);
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        border: 3px dashed var(--primary-blue);
        border-radius: 16px;
        padding: 2rem;
        background: linear-gradient(135deg, #F9FAFB 0%, #EFF6FF 100%);
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: var(--secondary-blue);
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
        color: #065F46;
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid #10B981;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.2);
    }
    
    .stError {
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
        color: #991B1B;
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid #EF4444;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
        color: #92400E;
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid #F59E0B;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
    }
    
    .stInfo {
        background: linear-gradient(135deg, #DBEAFE 0%, #BFDBFE 100%);
        color: #1E40AF;
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid #3B82F6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid var(--primary-blue);
        margin: 1rem 0;
    }
    
    .info-box h3 {
        color: var(--primary-blue);
        margin-top: 0;
        font-size: 1.2rem;
    }
    
    /* Analytics Cards */
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid var(--primary-blue);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 16px rgba(30, 64, 175, 0.15);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        color: var(--text-light);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Download Section */
    .download-section {
        background: linear-gradient(135deg, #F9FAFB 0%, #EFF6FF 100%);
        border-radius: 16px;
        padding: 2.5rem;
        margin-top: 2rem;
        border: 2px solid var(--light-blue);
    }
    
    /* Tips Section */
    .tips-card {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 1rem;
        border-left: 4px solid var(--primary-blue);
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.1);
    }
    
    .tips-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin-bottom: 1rem;
    }
    
    .tips-card ul {
        color: var(--text-dark);
        line-height: 2;
        font-size: 0.95rem;
    }
    
    /* Resume Preview */
    .resume-preview {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        border: 2px solid var(--border-color);
    }
    
    /* Text Inputs */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 2px solid var(--border-color);
        transition: all 0.3s ease;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: var(--primary-blue);
        box-shadow: 0 0 0 3px rgba(30, 64, 175, 0.1);
    }
    
    /* Select Box */
    .stSelectbox>div>div {
        border-radius: 10px;
        border: 2px solid var(--border-color);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--bg-light);
        border-radius: 10px;
        font-weight: 600;
        color: var(--primary-blue);
        border: 2px solid var(--border-color);
    }
    
    .streamlit-expanderHeader:hover {
        border-color: var(--secondary-blue);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 2rem;
        margin-top: 4rem;
        border-top: 3px solid var(--light-blue);
        color: var(--text-light);
    }
    
    .footer-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--primary-blue);
        margin-bottom: 0.5rem;
    }
    
    /* Navigation Buttons */
    .nav-buttons {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-top: 1.5rem;
    }
    
    /* Spinner Animation */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Subheaders */
    h2, h3 {
        color: var(--primary-blue);
    }
    
    /* Dividers */
    hr {
        border: none;
        border-top: 2px solid var(--light-blue);
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)


