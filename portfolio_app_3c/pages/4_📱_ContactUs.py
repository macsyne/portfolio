
import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="Contact | Maxene Victor", page_icon="📬", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .card { background:white; border-radius:16px; padding:28px 32px; box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:20px; }
    .social-btn {
        display: flex; align-items: center; gap: 12px;
        background: white; border-radius: 12px;
        padding: 14px 20px; margin-bottom: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.07);
        text-decoration: none; color: #302b63;
        font-weight: 600;
    }
    .social-btn:hover { box-shadow: 0 4px 20px rgba(17,153,142,0.25); }
    .info-row { display:flex; align-items:center; gap:12px; margin-bottom:14px; color:#444; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 📬 Contact Me")
st.markdown("*Have something to say? Feel free to reach out — I don't bite! 😊*")
st.markdown("---")

col_form, col_info = st.columns([3, 2])

# ── Contact Form ──────────────────────────────────────────────
with col_form:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### ✉️ Send a Message")

    name    = st.text_input("👤 Your Name", placeholder="e.g. Maria Santos")
    email   = st.text_input("📧 Your Email", placeholder="e.g. maria@example.com")
    subject = st.selectbox("📌 Subject", [
        "Just Saying Hi 👋",
        "Question About My Projects",
        "School / Study Related",
        "Collaboration Idea",
        "Other",
    ])
    message = st.text_area("💬 Message", placeholder="Write your message here...", height=160)

    col_btn, col_clear = st.columns([2, 1])
    with col_btn:
        send = st.button("💌 Send Message", use_container_width=True)
    with col_clear:
        clear = st.button("🗑️ Clear", use_container_width=True)

    if send:
        errors = []
        if not name.strip():
            errors.append("Name is required.")
        if not email.strip() or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("A valid email address is required.")
        if not message.strip() or len(message.strip()) < 10:
            errors.append("Message must be at least 10 characters.")

        if errors:
            for e in errors:
                st.error(f"⚠️ {e}")
        else:
            ts = datetime.now().strftime("%B %d, %Y at %I:%M %p")
            st.success(f"""
✅ **Message received!**

Thanks, **{name.strip()}**! I got your message about *"{subject}"* on {ts}.
I'll try to get back to you at **{email}** as soon as I can. 😊
            """)
            st.balloons()

    if clear:
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ── Info + Social Links ───────────────────────────────────────
with col_info:
    st.markdown("""<div class="card">
    <h3>📍 Contact Info</h3>
    <div class="info-row"><span>📧</span><span>mxnvctr@gmail.com</span></div>
    <div class="info-row"><span>📍</span><span>Philippines 🇵🇭</span></div>
    <div class="info-row"><span>🕐</span><span>I check messages when I can!</span></div>
    <div class="info-row"><span>🌱</span><span>Currently: studying & learning to code</span></div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card">
    <h3>🔗 Find Me On</h3>
    <a class="social-btn" href="https://github.com/" target="_blank">
        <span style="font-size:1.4rem">🐙</span> GitHub
    </a>
    <a class="social-btn" href="https://instagram.com/" target="_blank">
        <span style="font-size:1.4rem">📸</span> Instagram
    </a>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class="card" style="background:linear-gradient(135deg,#11998e,#38ef7d); color:white">
    <h4 style="color:white">🌱 Always Up to Learn</h4>
    <p style="opacity:0.9; font-size:0.9rem">
    I'm a student still finding my path in tech. If you have tips, resources,
    or just want to connect — I'm always happy to chat! 😊
    </p>
    </div>""", unsafe_allow_html=True)

st.caption("© 2025 Maxene Victor · Built with ❤️ using Streamlit")
