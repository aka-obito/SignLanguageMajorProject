import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page configurations
st.set_page_config(page_title="SignConnect App", page_icon="🤟", layout="wide")

# Lottie animation loader
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
animation_hero = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jcikwtux.json")
animation_features = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_8w6ny5ux.json")
animation_footer = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_oaulz5qh.json")

# Page layout
def main():
    # Custom CSS Animations
    st.markdown("""
        <style>
            @keyframes fadeIn {
                0% {opacity: 0;}
                100% {opacity: 1;}
            }
            .fade-in {
                animation: fadeIn 2s;
            }
            .hover-button:hover {
                background-color: #45a049;
                transform: scale(1.05);
                transition: all 0.3s ease-in-out;
            }
            .title-text {
                font-size: 60px;
                color: #4CAF50;
                text-align: center;
                font-weight: bold;
                margin-top: -20px;
                animation: fadeIn 2s;
            }
            .subtitle-text {
                font-size: 24px;
                color: #6c757d;
                text-align: center;
                margin-bottom: 30px;
                animation: fadeIn 2s;
            }
            .footer-text {
                text-align: center;
                color: grey;
                font-size: 14px;
                margin-top: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("## 🤟 SignConnect")
        st.info("Explore how AI bridges the communication gap for sign language users and non-users.")

    # Title with animations
    st.markdown('<div class="title-text">🤝 SignConnect</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">"Bridging the World of Silence and Sound"</div>', unsafe_allow_html=True)

    # Hero Section with Lottie Animation
    st_lottie(animation_hero, height=300, key="hero")

    # Welcome message
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 👋 Welcome!")
        st.markdown("""
            Welcome to **SignConnect**, a modern solution empowering communication 
            for the deaf community. Our app uses **Machine Learning** and **Computer Vision** 
            to translate sign language gestures into text in real-time, fostering inclusion 
            and accessibility for everyone.
        """)
    with col2:
        st.markdown("### 🧩 How It Works")
        st.markdown("""
            - Detect gestures in real-time.
            - Convert sign language into text.
            - Make communication seamless and inclusive.
        """)

    # Features Section with Emojis
    st.markdown("### 🌟 Key Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🚀 Real-Time Translation")
        st.write("Translate gestures into text instantly with precision.")
    with col2:
        st.markdown("### 🤖 AI-Powered Engine")
        st.write("Leverage cutting-edge ML and computer vision technology.")
    with col3:
        st.markdown("### 🎨 User-Friendly UI")
        st.write("Designed for simplicity and accessibility for all.")

    # Call-to-Action Button
    st.markdown("""
        <div style="text-align: center; margin-top: 40px;">
            <a class="hover-button" href="http://192.168.227.102:8502" target="_blank" 
            style="background-color:#4CAF50; color:white; padding:15px 30px; 
            text-decoration:none; border-radius:10px; font-size:20px;">
                Try It Now 🚀
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown('<p class="footer-text">&copy; 2024 SignConnect | Made with ❤️ for an inclusive world.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
