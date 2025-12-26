"""
Reusable Landing Page Components for SmartCareer
Save as: landing_components.py

Import and use in any page:
from landing_components import render_hero, render_features, etc.
"""

import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page

# Custom CSS
def inject_landing_css():
    st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Main app styling */
    .stApp {
        background: #0a0a0a;
        color: white;
    }
    
    .main .block-container {
        max-width: 1400px;
        padding: 0;
    }
    
    /* Hero Section */
    .hero-section {
        position: relative;
        min-height: 90vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 4rem 2rem;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.3), transparent 50%),
                    radial-gradient(circle at 80% 50%, rgba(240, 147, 251, 0.3), transparent 50%);
        animation: pulse 8s ease-in-out infinite;
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 900px;
        margin: 0 auto;
    }
    
    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4.5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #ffffff 0%, #e0e7ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 3rem;
        font-weight: 400;
        animation: fadeInUp 1.2s ease-out;
    }
    
    .hero-cta {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
        animation: fadeInUp 1.4s ease-out;
    }
    
    .cta-button {
        padding: 1.25rem 3rem;
        font-size: 1.15rem;
        font-weight: 700;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none;
        display: inline-block;
    }
    
    .cta-primary {
        background: white;
        color: #667eea;
        box-shadow: 0 10px 40px rgba(255, 255, 255, 0.3);
    }
    
    .cta-primary:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(255, 255, 255, 0.4);
    }
    
    .cta-secondary {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    .cta-secondary:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-5px);
    }
    
    .trust-badge {
        margin-top: 3rem;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1rem;
        animation: fadeInUp 1.6s ease-out;
    }
    
    /* Section styling */
    .section {
        padding: 6rem 2rem;
        position: relative;
    }
    
    .section-dark {
        background: #0a0a0a;
    }
    
    .section-light {
        background: #111111;
    }
    
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .section-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #ffffff, #ffa500); /* white to orange */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    
    /* Problem cards */
    .problem-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .problem-card {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.05));
        border: 1px solid rgba(239, 68, 68, 0.2);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .problem-card:hover {
        transform: translateY(-10px);
        border-color: rgba(239, 68, 68, 0.4);
        box-shadow: 0 20px 60px rgba(239, 68, 68, 0.2);
    }
    
    .problem-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .problem-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .problem-desc {
        color: #aaa;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        margin-top: 3rem;
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 24px;
        padding: 2.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .feature-card:hover::before {
        transform: scaleX(1);
    }
    
    .feature-card:hover {
        transform: translateY(-12px);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 25px 70px rgba(102, 126, 234, 0.3);
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.1));
    }
    
    .feature-icon {
        font-size: 3.5rem;
        margin-bottom: 1.5rem;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
    }
    
    .feature-desc {
        color: #bbb;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* How it works */
    .steps-container {
        max-width: 1000px;
        margin: 0 auto;
        position: relative;
    }
    
    .step-item {
        display: flex;
        gap: 2rem;
        margin-bottom: 4rem;
        align-items: center;
    }
    
    .step-number {
        flex-shrink: 0;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea, #764ba2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 800;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .step-content {
        flex: 1;
    }
    
    .step-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.75rem;
    }
    
    .step-desc {
        color: #aaa;
        font-size: 1.1rem;
        line-height: 1.7;
    }
    
    /* Testimonials */
    .testimonial-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2.5rem;
        margin-top: 3rem;
    }
    
    .testimonial-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2.5rem;
        transition: all 0.3s ease;
    }
    
    .testimonial-card:hover {
        transform: translateY(-8px);
        border-color: rgba(102, 126, 234, 0.4);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.2);
    }
    
    .testimonial-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #ddd;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    
    .testimonial-author {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .author-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea, #764ba2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .author-info {
        flex: 1;
    }
    
    .author-name {
        font-weight: 600;
        color: white;
        margin-bottom: 0.25rem;
    }
    
    .author-role {
        color: #888;
        font-size: 0.9rem;
    }
    
    /* Pricing */
    .pricing-toggle {
        display: flex;
        justify-content: center;
        gap: 1rem;
        align-items: center;
        margin-bottom: 3rem;
    }
    
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2.5rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .pricing-card {
        background: rgba(255, 255, 255, 0.03);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 3rem 2.5rem;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
    }
    
    .pricing-card.featured {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(118, 75, 162, 0.1));
        border-color: #667eea;
        transform: scale(1.05);
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
    }
    
    .pricing-card:hover {
        transform: scale(1.08);
        border-color: #667eea;
    }
    
    .pricing-badge {
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: #1f2937;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
    }
    
    .pricing-name {
        font-size: 1.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 1rem;
    }
    
    .pricing-price {
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .pricing-period {
        color: #888;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    .pricing-features {
        text-align: left;
        margin: 2rem 0;
    }
    
    .pricing-feature {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem 0;
        color: #ddd;
        font-size: 1rem;
    }
    
    .pricing-feature::before {
        content: '✓';
        color: #10b981;
        font-weight: 700;
        font-size: 1.2rem;
    }
    
    .pricing-button {
        width: 100%;
        padding: 1.25rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 1.5rem;
    }
    
    .pricing-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
    }
    
    /* FAQ */
    .faq-container {
        max-width: 900px;
        margin: 0 auto;
    }
    
    .faq-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        margin-bottom: 1.5rem;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .faq-item:hover {
        border-color: rgba(102, 126, 234, 0.4);
    }
    
    .faq-question {
        padding: 1.75rem 2rem;
        font-size: 1.25rem;
        font-weight: 600;
        color: white;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .faq-answer {
        padding: 0 2rem 1.75rem 2rem;
        color: #aaa;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* Final CTA */
    .final-cta {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-radius: 30px;
        padding: 5rem 3rem;
        text-align: center;
        margin: 4rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .final-cta::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 50%, rgba(255, 255, 255, 0.1), transparent 60%);
        animation: pulse 6s ease-in-out infinite;
    }
    
    .final-cta-content {
        position: relative;
        z-index: 2;
    }
    
    .final-cta-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    .final-cta-desc {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1.5rem;
    }
    
    
    /* Footer */
    .footer {
        background: #050505;
        padding: 4rem 2rem 2rem 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 3rem;
        margin-bottom: 3rem;
    }
    
    .footer-section h3 {
        color: white;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    .footer-section a {
        display: block;
        color: #888;
        text-decoration: none;
        margin-bottom: 0.75rem;
        transition: color 0.3s ease;
    }
    
    .footer-section a:hover {
        color: #667eea;
    }
    
    .footer-bottom {
        text-align: center;
        padding-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        color: #666;
    }
    
    /* Animations */
    @keyframes fadeInUp {
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
            opacity: 1;
        }
        50% {
            opacity: 0.8;
        }
    }
    
    @keyframes float {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-20px);
        }
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1.2rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
        
        .step-item {
            flex-direction: column;
            text-align: center;
        }
        
        .final-cta-title {
            font-size: 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Hero Section
def render_hero_section():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Launch Your Dream Career with AI-Driven Guidance</h1>
            <p class="hero-subtitle">
                From exploration to placement — get a personalized roadmap, real-time coaching, 
                tools & insights all in one platform.
            </p>
            <div class="hero-cta">
                <a href="#features" class="cta-button cta-secondary">Why SmartCarrer</a>
                <a href="#working" class="cta-button cta-secondary">See How It Works</a>
            </div>
            <div class="trust-badge">
                ✨ Trusted by 10,000+ students, professionals & coaches across India
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
                    


# Problem Section
def render_problem_section():
    st.markdown("""
    <div class="section section-dark">
        <h2 class="section-title">The Career Confusion Problem</h2>
        <p class="section-subtitle">
            Most people struggle with career decisions due to lack of direction and personalized guidance
        </p>
        <div class="problem-grid">
            <div class="problem-card">
                <div class="problem-icon">😕</div>
                <h3 class="problem-title">Confused Which Career to Pick?</h3>
                <p class="problem-desc">Too many options, no clear path forward</p>
            </div>
            <div class="problem-card">
                <div class="problem-icon">🗺️</div>
                <h3 class="problem-title">No Roadmap or Direction</h3>
                <p class="problem-desc">Don't know what skills to learn or steps to take</p>
            </div>
            <div class="problem-card">
                <div class="problem-icon">👥</div>
                <h3 class="problem-title">Lack of Personalized Mentoring</h3>
                <p class="problem-desc">Generic advice doesn't fit your unique situation</p>
            </div>
            <div class="problem-card">
                <div class="problem-icon">📉</div>
                <h3 class="problem-title">Low Job Search Conversion</h3>
                <p class="problem-desc">Applying everywhere but getting nowhere</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Solution Section
def render_solution_section():
    st.markdown("""
    <div class="section section-light">
        <h2 class="section-title">Meet SmartCareer: Your AI Career Companion</h2>
        <p class="section-subtitle">
            We blend mentorship, real data, goal tracking, and AI recommendations to create 
            your personalized path to success
        </p>
    </div>
    """, unsafe_allow_html=True)

# Features Section
def render_features_section():
    st.markdown("""
    <div class="section section-dark" id="features">
        <h2 class="section-title">Powerful Features to Transform Your Career</h2>
        <p class="section-subtitle">
            Everything you need to plan, learn, build, and land your dream role
        </p>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3 class="feature-title">Personalized Roadmap Generator</h3>
                <p class="feature-desc">
                    Get a step-by-step career plan built specifically for your background, 
                    skills, and goals. No generic templates.
                </p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3 class="feature-title">Skill Gap Analytics</h3>
                <p class="feature-desc">
                    Identify exactly what skills you're missing and get curated learning 
                    resources to fill those gaps quickly.
                </p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📝</div>
                <h3 class="feature-title">AI Resume Builder</h3>
                <p class="feature-desc">
                    Create ATS-optimized resumes with AI suggestions, multiple templates, 
                    and real-time feedback on improvements.
                </p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3 class="feature-title">AI Career Coach</h3>
                <p class="feature-desc">
                    24/7 AI mentor to answer questions, provide guidance, and help you 
                    make better career decisions.
                </p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <h3 class="feature-title">Progress Tracking & Analytics</h3>
                <p class="feature-desc">
                    Monitor your journey, track milestones, and get data-driven insights 
                    to stay motivated and on track.
                </p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">👥</div>
                <h3 class="feature-title">Community & Networking</h3>
                <p class="feature-desc">
                    Connect with peers, share experiences, get feedback, and build 
                    your professional network.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# How It Works
def render_how_it_works_section():
    st.markdown("""
    <div class="section section-light" id="working">
        <h2 class="section-title">How SmartCareer Works</h2>
        <p class="section-subtitle">
            From sign-up to landing your dream job in 5 simple steps
        </p>
        <div class="steps-container">
            <div class="step-item">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3 class="step-title">Tell Us About Yourself</h3>
                    <p class="step-desc">
                        Share your background, skills, interests, and career goals. 
                        Our AI analyzes your profile to understand your unique situation.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3 class="step-title">Get Your Custom Roadmap</h3>
                    <p class="step-desc">
                        Receive a personalized career plan with specific milestones, 
                        skills to learn, and actionable tasks tailored to your goals.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3 class="step-title">Learn, Build & Create</h3>
                    <p class="step-desc">
                        Access curated resources, build projects, create your portfolio, 
                        and develop the skills employers are looking for.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h3 class="step-title">Get AI Feedback & Iterate</h3>
                    <p class="step-desc">
                        Receive continuous feedback on your resume, projects, and progress. 
                        Refine your approach based on data-driven insights.
                    </p>
                </div>
            </div>
            <div class="step-item">
                <div class="step-number">5</div>
                <div class="step-content">
                    <h3 class="step-title">Land Your Dream Role</h3>
                    <p class="step-desc">
                        Apply strategically with optimized materials, interview prep, 
                        and confidence. Get the job you deserve.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Testimonials
def render_testimonials_section():
    st.markdown("""
    <div class="section section-dark">
        <h2 class="section-title">What Our Users Say</h2>
        <p class="section-subtitle">
            Real stories from people who transformed their careers with SmartCareer
        </p>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <p class="testimonial-text">
                    "SmartCareer gave me the clarity I needed. Within 3 months, I pivoted 
                    from marketing to product management with complete confidence. The AI 
                    roadmap was spot-on!"
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">P</div>
                    <div class="author-info">
                        <div class="author-name">Priya Sharma</div>
                        <div class="author-role">Product Manager, Chennai</div>
                    </div>
                </div>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-text">
                    "The roadmap feature is game-changing. Instead of random YouTube tutorials, 
                    I had a clear path. Got my first data science job in 4 months!"
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">R</div>
                    <div class="author-info">
                        <div class="author-name">Rohan Mehta</div>
                        <div class="author-role">Data Scientist, Bangalore</div>
                    </div>
                </div>
            </div>
            <div class="testimonial-card">
                <p class="testimonial-text">
                    "As a career coach, SmartCareer helps me scale my impact. The AI tools 
                    save me hours while providing better insights to my clients."
                </p>
                <div class="testimonial-author">
                    <div class="author-avatar">A</div>
                    <div class="author-info">
                        <div class="author-name">Anita Desai</div>
                        <div class="author-role">Career Coach, Mumbai</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Pricing Section

def render_pricing_section():
    with st.container():
        st.markdown('<div class="section section-light" id="pricing">', unsafe_allow_html=True)
        st.markdown("""
            <h2 class="section-title">Choose Your Plan</h2>
            <p class="section-subtitle">
                Start free, upgrade when you're ready. All plans include core features.
            </p>
        """, unsafe_allow_html=True)

        # ✅ Minimal change: use Streamlit columns for equal width
        cols = st.columns(4)

        with cols[0]:
            st.markdown("""
            <div class="pricing-card">
                <h3 class="pricing-name">Free</h3>
                <div class="pricing-price">₹0</div>
                <div class="pricing-period">Forever free</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Create 1 AI Resume</div>
                    <div class="pricing-feature">Basic Career Roadmap</div>
                    <div class="pricing-feature">Limited AI Suggestions</div>
                    <div class="pricing-feature">Community Access</div>
                    <div class="pricing-feature">Email Support</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with cols[1]:
            st.markdown("""
            <div class="pricing-card">
                <h3 class="pricing-name">Basic</h3>
                <div class="pricing-price">₹199</div>
                <div class="pricing-period">per month</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Create 5 AI Resumes</div>
                    <div class="pricing-feature">All Basic Templates</div>
                    <div class="pricing-feature">AI Resume Scoring</div>
                    <div class="pricing-feature">Cover Letter Generator</div>
                    <div class="pricing-feature">Priority Email Support</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with cols[2]:
            st.markdown("""
            <div class="pricing-card featured">
                <div class="pricing-badge">⭐ Most Popular</div>
                <h3 class="pricing-name">Pro</h3>
                <div class="pricing-price">₹499</div>
                <div class="pricing-period">per month</div>
                <div class="pricing-features">
                    <div class="pricing-feature">Unlimited AI Resumes</div>
                    <div class="pricing-feature">Premium Templates</div>
                    <div class="pricing-feature">ATS Optimization</div>
                    <div class="pricing-feature">Voice-to-Text Input</div>
                    <div class="pricing-feature">AI Career Coach 24/7</div>
                    <div class="pricing-feature">Priority Chat Support</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with cols[3]:
            st.markdown("""
            <div class="pricing-card">
                <h3 class="pricing-name">Premium</h3>
                <div class="pricing-price">₹999</div>
                <div class="pricing-period">per month</div>
                <div class="pricing-features">
                    <div class="pricing-feature">All Pro Features</div>
                    <div class="pricing-feature">Job Match AI</div>
                    <div class="pricing-feature">Custom Branding</div>
                    <div class="pricing-feature">1:1 Coaching Sessions</div>
                    <div class="pricing-feature">Dedicated Manager</div>
                    <div class="pricing-feature">24/7 Premium Support</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


    # Add interactive pricing buttons
    # col1, col2, col3, col4 = st.columns(4)

    # with col1:
    #     if st.button("Get Started Free", key="free_btn", use_container_width=True):
    #         st.session_state["selected_plan"] = "free"
    #         st.switch_page("pages/payment.py")

    # with col2:
    #     if st.button("Start Basic Plan", key="basic_btn", use_container_width=True):
    #         st.session_state["selected_plan"] = "basic"
    #         st.switch_page("pages/payment.py")

    # with col3:
    #     if st.button("Start Pro Plan", key="pro_btn", use_container_width=True, type="primary"):
    #         st.session_state["selected_plan"] = "pro"
    #         st.switch_page("pages/payment.py")

    # with col4:
    #     if st.button("Go Premium", key="premium_btn", use_container_width=True):
    #         st.session_state["selected_plan"] = "premium"
    #         st.switch_page("pages/payment.py")

    # st.markdown("""
    #     <div style="text-align: center; margin-top: 3rem; color: #888; font-size: 1.1rem;">
    #         💰 <strong>Save 20%</strong> with yearly billing • 🔒 Secure payment • ✅ Cancel anytime
    #     </div>
    # </div>
    # """, unsafe_allow_html=True)



def render_faq_section():
    
    faq_html = """
    <style>
    /* --- FAQ Styles --- */
    .section-dark {
    background: linear-gradient(180deg, rgba(0,0,0,0.06), rgba(255,255,255,0.02));
    padding: 28px;
    border-radius: 12px;
    color: #0f172a;
    font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    .section-title {
    margin: 0 0 8px 0;
    font-size: 22px;
    font-weight: 700;
    color: #111827;
    }
    .section-subtitle {
    margin: 0 0 18px 0;
    font-size: 14px;
    color: #374151;
    }
    .faq-container {
    display: grid;
    gap: 12px;
    }
    .faq-item {
    background: rgba(255,255,255,0.98);
    border-radius: 10px;
    padding: 12px;
    border: 1px solid rgba(15, 23, 42, 0.06);
    box-shadow: 0 6px 18px rgba(2,6,23,0.04);
    overflow: hidden;
    }
    .faq-question {
    font-size: 15px;
    font-weight: 600;
    color: #0f172a;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    }
    .faq-question .icon {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: linear-gradient(90deg,#ff7e29,#ff9800);
    color: #fff;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    transition: transform .18s ease;
    }
    .faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.28s ease, padding 0.18s ease;
    padding: 0 0;
    color: #374151;
    margin-top: 8px;
    line-height: 1.5;
    font-size: 14px;
    }
    .faq-item.open .faq-answer {
    padding: 10px 0 0 0;
    max-height: 400px; /* enough for the content */
    }
    .faq-item.open .faq-question .icon {
    transform: rotate(45deg);
    }
    </style>

    <div class="section section-dark">
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-subtitle">
            Everything you need to know about SmartCareer
        </p>
        <div class="faq-container">

            <div class="faq-item">
                <div class="faq-question">
                    <span>How is SmartCareer different from job portals?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    SmartCareer focuses on career preparation and planning, not just job listings.
                    We help you build the right skills, create compelling materials, and develop
                    a strategic approach before you even start applying. Think of us as your
                    career GPS, not just a job board.
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>Do I need any specific background or experience?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    Not at all! SmartCareer works for everyone — fresh graduates, career switchers,
                    professionals looking to upskill, or anyone exploring career options. Our AI
                    adapts the roadmap based on your current situation and goals.
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>Can I get 1:1 mentorship with a real person?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    Yes! Premium plan users get access to 1:1 coaching sessions with experienced
                    career mentors. Pro and Basic users have 24/7 AI mentoring, and can upgrade
                    anytime for human coaching.
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>What if I don't complete all the modules?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    No problem! SmartCareer is flexible and self-paced. Your roadmap adjusts to
                    your progress, and you can pause, skip, or revisit modules as needed. Life
                    happens, and we understand that.
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>What's your refund policy?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    We offer a 7-day money-back guarantee on all paid plans. If you're not
                    satisfied within the first week, contact support and we'll process a full
                    refund, no questions asked.
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>How do I get support if I'm stuck?</span>
                    <span class="icon">+</span>
                </div>
                <div class="faq-answer">
                    All users get email support. Pro users get priority chat support. Premium
                    users get 24/7 dedicated support plus direct access to their account manager.
                    We also have an active community forum where you can get help from peers.
                </div>
            </div>

        </div>
    </div>

    <script>
    /* Simple accordion behavior */
    (function() {
    const items = document.querySelectorAll('.faq-item');
    items.forEach(item => {
        const q = item.querySelector('.faq-question');
        q.addEventListener('click', () => {
        const open = item.classList.contains('open');
        // close all (optional single-open behavior)
        items.forEach(i => i.classList.remove('open'));
        if (!open) {
            item.classList.add('open');
        }
        });
    });
    })();
    </script>
    """

    # Render via components.html so JS will run
    components.html(faq_html, height=700, scrolling=True)


def render_top_cta_section():

    st.markdown("""            
    <div class="section section-dark" id="features">
        <h2 class="section-title">Your Dream Career Starts Here</h2>
        <p class="section-subtitle">
            Take control of your future with SmartCareer — personalized roadmaps, AI-powered guidance, 
            and tools to accelerate your success.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CTA Buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            if st.button("🚀 Start Free Today", key="top_cta_primary", type="primary", use_container_width=True):
                st.switch_page("pages/Login.py")
        with subcol2:
            if st.button("📧 Contact Sales", key="top_cta_secondary", use_container_width=True):
                st.info("Email us at: leokit1013@gmail.com")


def render_final_cta_section():
    # Final CTA Section
    st.markdown("""
    <div class="section section-light">
        <div class="final-cta">
            <div class="final-cta-content">
                <h2 class="final-cta-title">Ready to Transform Your Career?</h2>
                <p class="final-cta-desc">
                    Join thousands of professionals who've already found their path with SmartCareer. 
                    Start free today, no credit card required.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Final CTA Buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            if st.button("🚀 Start Free Today", key="final_cta_primary", type="primary", use_container_width=True):
                st.switch_page("pages/Login.py")
        with subcol2:
            if st.button("📧 Contact Sales", key="final_cta_secondary", use_container_width=True):
                st.info("Email us at: leokit1013@gmail.com")

# Footer
# Inject CSS for footer
def render_footer():

    # --- Footer HTML + CSS ---
    footer_html = """
    <style>
    .footer {
        background-color: #111827;
        color: #f3f4f6;
        padding: 50px 0 30px 0;
        margin-top: 50px;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .footer-content {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 80px;
        margin-bottom: 30px;
    }
    .footer-section {
        flex: 1;
        min-width: 180px;
    }
    .footer-section h3 {
        color: #facc15;
        font-size: 1.2rem;
        margin-bottom: 15px;
    }
    .footer-section a {
        display: block;
        color: #9ca3af;
        text-decoration: none;
        margin-bottom: 6px;
        font-size: 0.95rem;
        transition: color 0.2s ease;
    }
    .footer-section a:hover {
        color: #facc15;
    }
    .footer-bottom {
        border-top: 1px solid #374151;
        padding-top: 15px;
        font-size: 0.9rem;
        color: #9ca3af;
    }
    </style>

    <div class="footer">
        <div class="footer-content">
            <div class="footer-section">
                <h3>SmartCareer</h3>
                <p style="color: #888; line-height: 1.7;">
                    AI-powered career guidance platform helping professionals 
                    find clarity and achieve their career goals.
                </p>
            </div>
            
            <div class="footer-section">
                <h3>Product</h3>
                <a href="#features">Features</a>
                <a href="#pricing">Pricing</a>
                <a href="#testimonials">Testimonials</a>
                <a href="/demo">Request Demo</a>
                <a href="/changelog">Changelog</a>
            </div>
            
            <div class="footer-section">
                <h3>Resources</h3>
                <a href="/blog">Blog</a>
                <a href="/guides">Career Guides</a>
                <a href="/templates">Resume Templates</a>
                <a href="/community">Community</a>
                <a href="/api">API Docs</a>
            </div>
            
            <div class="footer-section">
                <h3>Company</h3>
                <a href="/about">About Us</a>
                <a href="/careers">Careers</a>
                <a href="/contact">Contact</a>
                <a href="/privacy">Privacy Policy</a>
                <a href="/terms">Terms of Service</a>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>© 2025 SmartCareer. All rights reserved.</p>
            <p style="margin-top: 0.5rem;">Made with ❤️ for career seekers everywhere</p>
        </div>
    </div>
    """

    components.html(footer_html, height=400)


def render_stats_banner():
    """Animated stats banner"""
    st.markdown("""
    <div class="section section-dark">
        <h2 class="section-title">Stats Banner</h2>
        <p class="section-subtitle">
            Statistics that build trust and credibility
        </p>
        <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
                    padding: 3rem 2rem; margin: 3rem 0; border-radius: 24px;
                    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;
                    text-align: center;">
            <div>
                <div style="font-size: 3rem; font-weight: 800; color: #667eea;">10,000+</div>
                <div style="color: #888; font-size: 1.1rem; margin-top: 0.5rem;">Active Users</div>
            </div>
            <div>
                <div style="font-size: 3rem; font-weight: 800; color: #667eea;">50,000+</div>
                <div style="color: #888; font-size: 1.1rem; margin-top: 0.5rem;">Resumes Created</div>
            </div>
            <div>
                <div style="font-size: 3rem; font-weight: 800; color: #667eea;">95%</div>
                <div style="color: #888; font-size: 1.1rem; margin-top: 0.5rem;">Success Rate</div>
            </div>
            <div>
                <div style="font-size: 3rem; font-weight: 800; color: #667eea;">4.9/5</div>
                <div style="color: #888; font-size: 1.1rem; margin-top: 0.5rem;">User Rating</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_comparison_table():
    """Before vs After comparison"""
    st.markdown("""
    <div class="section section-dark">
        <h2 class="section-title">Comparison Table</h2>
        <p class="section-subtitle">
            What makes you stand out in today's competitive job market?
        </p>
        <div style="max-width: 1000px; margin: 4rem auto;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
                <div style="background: rgba(239, 68, 68, 0.1); border: 2px solid rgba(239, 68, 68, 0.3);
                            border-radius: 20px; padding: 2.5rem;">
                    <h3 style="color: #ef4444; font-size: 1.75rem; margin-bottom: 1.5rem; text-align: center;">
                        😰 Without SmartCareer
                    </h3>
                    <div style="color: #ddd; font-size: 1.05rem; line-height: 2;">
                        ❌ Confused about career path<br>
                        ❌ Generic resume templates<br>
                        ❌ No personalized guidance<br>
                        ❌ Wasting time on wrong skills<br>
                        ❌ Low interview conversion<br>
                        ❌ No progress tracking
                    </div>
                </div>
                <div style="background: rgba(16, 185, 129, 0.1); border: 2px solid rgba(16, 185, 129, 0.3);
                            border-radius: 20px; padding: 2.5rem;">
                    <h3 style="color: #10b981; font-size: 1.75rem; margin-bottom: 1.5rem; text-align: center;">
                        🚀 With SmartCareer
                    </h3>
                    <div style="color: #ddd; font-size: 1.05rem; line-height: 2;">
                        ✅ Clear roadmap & direction<br>
                        ✅ ATS-optimized AI resumes<br>
                        ✅ 24/7 AI career coach<br>
                        ✅ Learn exactly what you need<br>
                        ✅ 3x more interview calls<br>
                        ✅ Data-driven insights
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_cta_box(title, subtitle, button_text="Get Started", button_link=None):
    """Reusable CTA box"""
    st.markdown(f"""
    <div class="section section-dark">
        <h2 class="section-title">CTA Section</h2>
    
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); 
                    border-radius: 24px; padding: 4rem 3rem; text-align: center;
                    margin: 4rem 0; box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);">
            <h2 style="color: white; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem;">
                {title}
            </h2>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.3rem; margin-bottom: 2.5rem;">
                {subtitle}
            </p>
        </div>
     </div>

    """, unsafe_allow_html=True)
    
    # Add Streamlit button below the box
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(button_text, key=f"cta_{title}", type="primary", use_container_width=True):
            if button_link:
                st.switch_page(button_link)
            return True
    return False


def render_video_demo():
    """Video demo section placeholder"""
    st.markdown("""
    <div style="max-width: 900px; margin: 4rem auto; text-align: center;">
        <h2 style="color: white; font-size: 2.5rem; margin-bottom: 2rem;">
            See SmartCareer in Action
        </h2>
        <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;
                    background: rgba(255,255,255,0.05); border-radius: 20px;
                    border: 2px solid rgba(102, 126, 234, 0.3);">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                        font-size: 4rem; color: rgba(255,255,255,0.5);">
                ▶️
            </div>
        </div>
        <p style="color: #888; margin-top: 1.5rem; font-size: 1.1rem;">
            Watch how SmartCareer helps you build your dream career in minutes
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # You can replace this with actual video embed:
    # st.video("YOUR_VIDEO_URL")


def render_trust_badges():
    """Company logos / trust indicators"""
    st.markdown("""
    <div style="text-align: center; margin: 4rem 0;">
        <p style="color: #888; font-size: 1.1rem; margin-bottom: 2rem;">
            Trusted by students and professionals from
        </p>
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;
                    align-items: center; opacity: 0.6;">
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">IIT</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">NIT</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">BITS</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">Google</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">Amazon</div>
            <div style="font-size: 1.5rem; font-weight: 700; color: white;">Microsoft</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_feature_highlight(icon, title, description, image_url=None):
    """Single feature highlight with optional image"""
    cols = st.columns([1, 1])
    
    with cols[0]:
        st.markdown(f"""
        <div style="padding: 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1.5rem;">{icon}</div>
            <h3 style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">
                {title}
            </h3>
            <p style="color: #bbb; font-size: 1.15rem; line-height: 1.8;">
                {description}
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        if image_url:
            st.image(image_url, use_column_width=True)
        else:
            st.markdown("""
            <div style="background: rgba(102, 126, 234, 0.1); border-radius: 20px;
                        height: 300px; display: flex; align-items: center; justify-content: center;
                        border: 2px solid rgba(102, 126, 234, 0.3);">
                <span style="font-size: 3rem; color: rgba(255,255,255,0.3);">📊</span>
            </div>
            """, unsafe_allow_html=True)


def render_pricing_comparison():
    """Detailed pricing comparison table"""
    st.markdown("""
    <style>
    .comparison-table {
        background: rgba(255,255,255,0.03);
        border-radius: 20px;
        padding: 2rem;
        margin: 3rem 0;
        overflow-x: auto;
    }
    .comparison-table table {
        width: 100%;
        border-collapse: collapse;
    }
    .comparison-table th {
        background: rgba(102, 126, 234, 0.2);
        padding: 1.25rem;
        text-align: left;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
    }
    .comparison-table td {
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        color: #ddd;
    }
    .comparison-table tr:hover {
        background: rgba(102, 126, 234, 0.05);
    }
    .check-icon {
        color: #10b981;
        font-weight: 700;
        font-size: 1.3rem;
    }
    .cross-icon {
        color: #ef4444;
        font-size: 1.3rem;
    }
    </style>
    
    <div class="comparison-table">
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th style="text-align: center;">Free</th>
                    <th style="text-align: center;">Basic</th>
                    <th style="text-align: center; background: rgba(102, 126, 234, 0.4);">Pro</th>
                    <th style="text-align: center;">Premium</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AI Resume Builder</td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                </tr>
                <tr>
                    <td>Resume Templates</td>
                    <td style="text-align: center;">3 Basic</td>
                    <td style="text-align: center;">10+ Basic</td>
                    <td style="text-align: center;">50+ Premium</td>
                    <td style="text-align: center;">Unlimited</td>
                </tr>
                <tr>
                    <td>Career Roadmap</td>
                    <td style="text-align: center;">Basic</td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                </tr>
                <tr>
                    <td>AI Career Coach</td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;">Limited</td>
                    <td style="text-align: center;">24/7</td>
                    <td style="text-align: center;">24/7 + Priority</td>
                </tr>
                <tr>
                    <td>ATS Optimization</td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                </tr>
                <tr>
                    <td>Skill Gap Analysis</td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                </tr>
                <tr>
                    <td>Job Matching AI</td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="check-icon">✓</span></td>
                </tr>
                <tr>
                    <td>1:1 Coaching</td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;"><span class="cross-icon">✗</span></td>
                    <td style="text-align: center;">4 sessions/month</td>
                </tr>
                <tr>
                    <td>Priority Support</td>
                    <td style="text-align: center;">Email</td>
                    <td style="text-align: center;">Email (48h)</td>
                    <td style="text-align: center;">Chat + Email</td>
                    <td style="text-align: center;">24/7 Dedicated</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)


def render_use_case_cards():
    """Who is SmartCareer for? (renders via a Streamlit container + components.html)"""
    with st.container():
        html = """
            <div class="section section-light" style="padding: 2.5rem 1rem;">
            <h2 class="section-title" style="text-align:center; margin-bottom:0.5rem;">Use Cases</h2>
            <p class="section-subtitle" style="text-align:center; color:#ddd; margin-bottom:2rem;">
                For Every Career Stage and Ambition
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, rgba(59,130,246,0.1), rgba(37,99,235,0.05)); border: 1px solid rgba(59,130,246,0.25); border-radius: 16px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.75rem;">🎓</div>
                <h3 style="color: white; font-size: 1.15rem; font-weight: 700; margin: 0.25rem 0 0.75rem 0;">Students & Fresh Graduates</h3>
                <p style="color:#bbb; line-height:1.6; margin:0;">Get career clarity, build the right skills, and land your first job with confidence.</p>
                </div>

                <div style="background: linear-gradient(135deg, rgba(16,185,129,0.08), rgba(5,150,105,0.04)); border: 1px solid rgba(16,185,129,0.22); border-radius: 16px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.75rem;">🔄</div>
                <h3 style="color: white; font-size: 1.15rem; font-weight: 700; margin: 0.25rem 0 0.75rem 0;">Career Switchers</h3>
                <p style="color:#bbb; line-height:1.6; margin:0;">Pivot to a new field with a clear roadmap, skill-building plan, and expert guidance.</p>
                </div>

                <div style="background: linear-gradient(135deg, rgba(139,92,246,0.08), rgba(124,58,237,0.04)); border: 1px solid rgba(139,92,246,0.22); border-radius: 16px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.75rem;">👔</div>
                <h3 style="color: white; font-size: 1.15rem; font-weight: 700; margin: 0.25rem 0 0.75rem 0;">Working Professionals</h3>
                <p style="color:#bbb; line-height:1.6; margin:0;">Upskill strategically, get promotions, and accelerate your career growth.</p>
                </div>

                <div style="background: linear-gradient(135deg, rgba(251,191,36,0.08), rgba(245,158,11,0.04)); border: 1px solid rgba(251,191,36,0.22); border-radius: 16px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.75rem;">🎯</div>
                <h3 style="color: white; font-size: 1.15rem; font-weight: 700; margin: 0.25rem 0 0.75rem 0;">Career Coaches</h3>
                <p style="color:#bbb; line-height:1.6; margin:0;">Scale your impact with AI tools, help more clients, and deliver better results.</p>
                </div>
            </div>
            </div>
            """
        # height: tweak if cards get cut off; scrolling=True if you'd like internal scrollbar
        components.html(html, height=520, scrolling=False)



def render_urgency_banner(message="🔥 Limited Time: First 100 users get 50% off forever!"):
    """Urgency/scarcity banner"""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #f59e0b, #ef4444);
                padding: 1.5rem 2rem; border-radius: 16px; text-align: center;
                margin: 2rem 0; box-shadow: 0 10px 30px rgba(245, 158, 11, 0.4);
                animation: pulse 2s infinite;">
        <p style="color: white; font-size: 1.25rem; font-weight: 700; margin: 0;">
            {message}
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_social_proof_ticker():
    """Scrolling social proof messages"""
    st.markdown("""
    <div class="section section-light">
        <h2 class="section-title">Social Proof Ticker</h2>
        <p class="section-subtitle">
            Social Proof from Happy Users
        </p>
        <div style="background: rgba(255,255,255,0.03); padding: 1.5rem; border-radius: 16px;
                    margin: 2rem 0; overflow: hidden;">
            <div style="display: flex; gap: 3rem; animation: scroll 20s linear infinite;">
                <div style="flex-shrink: 0; color: #bbb;">
                    ⭐ "Best career tool I've used" - Amit K.
                </div>
                <div style="flex-shrink: 0; color: #bbb;">
                    💼 "Got 3 offers in 2 months" - Priya S.
                </div>
                <div style="flex-shrink: 0; color: #bbb;">
                    🚀 "Finally have career clarity" - Rohan M.
                </div>
                <div style="flex-shrink: 0; color: #bbb;">
                    ✨ "Game-changer for freshers" - Sneha R.
                </div>
                <div style="flex-shrink: 0; color: #bbb;">
                    🎯 "Worth every rupee" - Vikram P.
                </div>
            </div>
        </div>
    </div>
    
    <style>
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    </style>
    """, unsafe_allow_html=True)


def render_newsletter_signup():
    """Email capture for newsletter"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.05));
                border: 2px solid rgba(102, 126, 234, 0.3); border-radius: 24px;
                padding: 3rem; text-align: center; margin: 4rem 0;">
        <h3 style="color: white; font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">
            📧 Get Career Tips & Updates
        </h3>
        <p style="color: #bbb; font-size: 1.1rem; margin-bottom: 2rem;">
            Join 10,000+ subscribers getting weekly career insights and exclusive offers
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        email = st.text_input("Enter your email", key="newsletter_email", label_visibility="collapsed")
        if st.button("Subscribe Now", key="newsletter_submit", use_container_width=True):
            if email and "@" in email:
                st.success("✅ Thank you! Check your email for confirmation.")
                return email
            else:
                st.error("Please enter a valid email address")
    return None


def render_money_back_guarantee():
    """Trust badge with guarantee"""
    st.markdown("""
    <div class="section section-light">
        <h2 class="section-title">Money Back Gurantee</h2>
        <p class="section-subtitle">
            Money-Back Guarantee & Trust Badges
        </p>
        <div style="display: flex; justify-content: center; gap: 3rem; margin: 3rem 0;
                    flex-wrap: wrap; align-items: center;">
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔒</div>
                <div style="color: white; font-weight: 600;">Secure Payment</div>
                <div style="color: #888; font-size: 0.9rem;">256-bit SSL</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">💰</div>
                <div style="color: white; font-weight: 600;">7-Day Refund</div>
                <div style="color: #888; font-size: 0.9rem;">No questions asked</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">✨</div>
                <div style="color: white; font-weight: 600;">Cancel Anytime</div>
                <div style="color: #888; font-size: 0.9rem;">No commitments</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎯</div>
                <div style="color: white; font-weight: 600;">95% Success Rate</div>
                <div style="color: #888; font-size: 0.9rem;">Proven results</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_live_activity_feed():
    """Fake live activity to show social proof"""
    import random
    import time
    
    names = ["Amit", "Priya", "Rohan", "Sneha", "Vikram", "Anjali", "Karthik", "Divya"]
    cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Pune", "Hyderabad"]
    actions = [
        "just created a resume",
        "upgraded to Pro",
        "landed an interview",
        "completed their roadmap",
        "joined SmartCareer"
    ]
    
    activity = f"🟢 {random.choice(names)} from {random.choice(cities)} {random.choice(actions)}"
    
    st.markdown(f"""
    <div style="position: fixed; bottom: 20px; left: 20px; z-index: 1000;
                background: rgba(10, 10, 10, 0.95); backdrop-filter: blur(10px);
                border: 1px solid rgba(102, 126, 234, 0.5); border-radius: 12px;
                padding: 1rem 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                animation: slideInLeft 0.5s ease-out;">
        <p style="color: white; margin: 0; font-size: 0.95rem;">
            {activity}
        </p>
        <p style="color: #888; margin: 0.25rem 0 0 0; font-size: 0.8rem;">
            Just now
        </p>
    </div>
      
    <style>
    @keyframes slideInLeft {{
        from {{
            transform: translateX(-100%);
            opacity: 0;
        }}
        to {{
            transform: translateX(0);
            opacity: 1;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def render_countdown_timer(end_date="2025-12-31"):
    """Countdown timer for offers"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ef4444, #dc2626);
                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;">
        <p style="color: white; font-size: 1.1rem; margin-bottom: 1rem; font-weight: 600;">
            ⏰ Limited Time Offer Ends In:
        </p>
        <div style="display: flex; justify-content: center; gap: 1.5rem;">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: white;">23</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">DAYS</div>
            </div>
            <div style="font-size: 2.5rem; color: white; font-weight: 800;">:</div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: white;">14</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">HOURS</div>
            </div>
            <div style="font-size: 2.5rem; color: white; font-weight: 800;">:</div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: white;">37</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">MINS</div>
            </div>
            <div style="font-size: 2.5rem; color: white; font-weight: 800;">:</div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; font-weight: 800; color: white;">22</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 0.9rem;">SECS</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Optional: Add scroll-to-top button
def render_smooth_scroll():
    st.markdown("""
    <script>
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)
# Example usage function


def demo_all_components():
    """
    Demo function showing how to use all components
    Call this from your landing page to see all components
    """
    st.title("Landing Page Components Demo")
    
    st.header("Stats Banner")
    render_stats_banner()
    
    st.header("Comparison Table")
    render_comparison_table()
    
    st.header("Use Case Cards")
    render_use_case_cards()
    
    st.header("CTA Box")
    render_cta_box(
        title="Ready to Start?",
        subtitle="Join thousands building their dream careers",
        button_text="Get Started Free"
    )
    
    st.header("Trust Badges")
    render_trust_badges()
    
    st.header("Money Back Guarantee")
    render_money_back_guarantee()
    
    st.header("Urgency Banner")
    render_urgency_banner()
    
    st.header("Social Proof Ticker")
    render_social_proof_ticker()
    
    st.header("Newsletter Signup")
    render_newsletter_signup()
    
    st.header("Countdown Timer")
    render_countdown_timer()
    
    st.header("Pricing Comparison")
    render_pricing_comparison()
    
# demo_all_components()