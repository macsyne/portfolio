
import streamlit as st

st.set_page_config(page_title="Skills | Maxene Victor", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .card { background:white; border-radius:16px; padding:28px 32px; box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:20px; }
    .skill-label { display:flex; justify-content:space-between; font-weight:600; color:#302b63; margin-bottom:4px; }
    .cert-card { background:linear-gradient(135deg,#11998e,#38ef7d); color:white;
                 border-radius:14px; padding:18px 22px; margin-bottom:14px; }
    .section-title { font-size:1.4rem; font-weight:700; color:#302b63; border-left:5px solid #11998e; padding-left:12px; margin:28px 0 16px; }
    .note-box { background:#fff8e1; border-left:4px solid #f9a825; border-radius:10px; padding:14px 18px; color:#555; font-size:0.9rem; margin-bottom:20px; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("# ⚡ Skills & Technologies")
st.markdown("*Still learning, but making progress every day!*")
st.markdown('<div class="note-box">🙋 I\'m still a student and just getting started — these reflect my honest, current skill level.</div>', unsafe_allow_html=True)
st.markdown("---")

# ── Interactive filter ─────────────────────────────────────────
category = st.selectbox("🔍 Filter by Category", ["All", "Programming", "Tools I Use", "Soft Skills"])

# ── Data ──────────────────────────────────────────────────────
skills = {
    "Programming": [
        ("Python", 35, "🐍"),
        ("HTML / CSS", 40, "🌐"),
        ("JavaScript (basics)", 15, "🟨"),
    ],
    "Tools I Use": [
        ("Streamlit", 30, "🚀"),
        ("VS Code", 55, "💙"),
        ("GitHub (beginner)", 20, "🐙"),
        ("Canva", 60, "✏️"),
    ],
    "Soft Skills": [
        ("Willingness to Learn", 95, "📖"),
        ("Creativity", 80, "🎨"),
        ("Problem Solving", 60, "🧩"),
        ("Communication", 70, "💬"),
    ],
}

def skill_bar(name, pct, icon):
    color = "#38ef7d" if pct >= 70 else "#11998e" if pct >= 40 else "#f7971e"
    st.markdown(f"""
        <div class="skill-label"><span>{icon} {name}</span><span>{pct}%</span></div>
    """, unsafe_allow_html=True)
    st.progress(pct / 100)
    st.markdown("<div style='margin-bottom:12px'></div>", unsafe_allow_html=True)

shown = {k: v for k, v in skills.items() if category == "All" or k == category}

if len(shown) == 1:
    for cat, items in shown.items():
        st.markdown(f'<div class="section-title">{cat}</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        for name, pct, icon in items:
            skill_bar(name, pct, icon)
        st.markdown('</div>', unsafe_allow_html=True)
else:
    col_left, col_right = st.columns(2)
    cats = list(shown.items())
    for i, (cat, items) in enumerate(cats):
        col = col_left if i % 2 == 0 else col_right
        with col:
            st.markdown(f'<div class="section-title">{cat}</div>', unsafe_allow_html=True)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            for name, pct, icon in items:
                skill_bar(name, pct, icon)
            st.markdown('</div>', unsafe_allow_html=True)

# ── Certifications ─────────────────────────────────────────────
if category == "All":
    st.markdown('<div class="section-title">🏅 Certificates & Learning</div>', unsafe_allow_html=True)
    certs = [
        ("📜", "Python Certificate", "Codedex", "2024"),
        ("🌱", "Currently Exploring", "HTML & CSS via online resources", "2025"),
    ]
    c1, c2 = st.columns(2)
    for i, (icon, title, org, year) in enumerate(certs):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.markdown(f"""<div class="cert-card">
                <div style="font-size:1.8rem">{icon}</div>
                <strong>{title}</strong><br>
                <span style="opacity:0.9">{org} · {year}</span>
            </div>""", unsafe_allow_html=True)

st.markdown("---")
st.info("🚀 **Currently learning:** Python fundamentals, basic web development, and exploring Streamlit for fun projects!")
st.caption("© 2025 Maxene Victor · Built with ❤️ using Streamlit")
