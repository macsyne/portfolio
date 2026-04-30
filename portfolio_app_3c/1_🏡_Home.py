
import streamlit as st

st.set_page_config(page_title="Home | Maxene Victor", page_icon="🏠", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .hero-home {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        border-radius: 20px;
        padding: 50px 40px;
        color: white;
        display: flex;
        align-items: center;
        gap: 40px;
    }
    .card { background:white; border-radius:16px; padding:28px; box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:20px; }
    .stat-number { font-size: 2.5rem; font-weight: 800; color: #11998e; }
    .stat-label  { color: #666; font-size: 0.9rem; }
    .tag { background:#e8f5e9; color:#2e7d32; border-radius:12px; padding:4px 12px; margin:3px; display:inline-block; font-size:0.8rem; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────
col_img, col_text = st.columns([1, 2])
with col_img:
    st.image(
        "https://api.dicebear.com/7.x/adventurer/svg?seed=Maxene&backgroundColor=b6e3f4",
        width=250,
    )
with col_text:
    st.markdown("## 👋 Hi, I'm **Maxene Victor**")
    st.markdown("### Computer Science Student · Aspiring Developer · Passionate Learner")
    st.markdown("""
I'm a computer science student with a love for building things on the web.
I enjoy learning new technologies and applying them to real-world projects.
Still growing, still learning — but always eager to create and improve.
    """)
    st.markdown("""
<span class="tag">Python</span>
<span class="tag">JavaScript</span>
<span class="tag">HTML & CSS</span>
<span class="tag">Streamlit</span>
<span class="tag">Beginner React</span>
<span class="tag">Open Source</span>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Stats ──────────────────────────────────────────────────────
st.markdown("### 📊 At a Glance")
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("4+", "Projects Built"),
    ("3rd Year", "CS Student"),
    ("3", "Technologies Learning"),
    ("100%", "Dedication"),
]
for col, (num, label) in zip([c1, c2, c3, c4], stats):
    with col:
        st.markdown(f"""<div class="card" style="text-align:center">
            <div class="stat-number">{num}</div>
            <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

# ── What I do ──────────────────────────────────────────────────
st.markdown("### 🚀 What I'm Into")
r1, r2, r3 = st.columns(3)
services = [
    ("🌐", "Web Development", "Learning to build websites and web apps using HTML, CSS, JavaScript, and Python."),
    ("🎨", "UI Design", "Exploring how to create clean and friendly interfaces that are easy to use."),
    ("📊", "Data & Dashboards", "Experimenting with data visualization and interactive tools using Python and Streamlit."),
]
for col, (icon, title, desc) in zip([r1, r2, r3], services):
    with col:
        st.markdown(f"""<div class="card" style="text-align:center">
            <div style="font-size:2.5rem">{icon}</div>
            <h4>{title}</h4>
            <p style="color:#555">{desc}</p>
        </div>""", unsafe_allow_html=True)

# ── Fun fact ticker ────────────────────────────────────────────
st.markdown("---")
st.info("💡 **Fun Fact:** I built my first website during a school project and got completely hooked on coding ever since! 💻")
st.caption("© 2025 Maxene Victor · Built with ❤️ using Streamlit")
