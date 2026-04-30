
import streamlit as st

st.set_page_config(page_title="About | Maxene Victor", page_icon="🧑‍💻", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .card { background:white; border-radius:16px; padding:28px 32px; box-shadow:0 4px 20px rgba(0,0,0,0.08); margin-bottom:20px; }
    .timeline-item { border-left: 3px solid #11998e; padding-left:16px; margin-bottom:20px; }
    .timeline-year { font-weight:800; color:#11998e; font-size:0.9rem; }
    .section-title { font-size:1.4rem; font-weight:700; color:#302b63; border-left:5px solid #11998e; padding-left:12px; margin:28px 0 16px; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🧑‍💻 About Me")
st.markdown("*Just a student trying to figure things out — one line of code at a time.*")
st.markdown("---")

# ── Bio ───────────────────────────────────────────────────────
col_bio, col_quick = st.columns([2, 1])

with col_bio:
    st.markdown("""<div class="card">
    <h3>👤 Who Am I?</h3>
    <p style="color:#444; line-height:1.8">
    I'm <strong>Maxene Victor</strong>, a student who recently got into coding and honestly loves it more
    than expected. I started learning Python not too long ago through Codedex, and it kind of just
    clicked — so here I am, building small projects and slowly figuring out how all of this works.
    </p>
    <p style="color:#444; line-height:1.8">
    I'm still very much a beginner, but I enjoy the process of learning. Right now I'm focused on
    getting comfortable with Python and exploring what I can build with it — starting with simple
    apps like this portfolio using Streamlit.
    </p>
    <p style="color:#444; line-height:1.8">
    When I'm not studying or coding, I enjoy listening to music 🎵, watching shows 📺,
    and hanging out with friends. Occasionally fueled by iced coffee ☕.
    </p>
    </div>""", unsafe_allow_html=True)

with col_quick:
    st.markdown("""<div class="card">
    <h4>⚡ Quick Facts</h4>
    <ul style="color:#555; line-height:2">
        <li>🎓 Currently a Student</li>
        <li>🐍 Learning Python</li>
        <li>📜 Codedex Certificate</li>
        <li>🗣️ Filipino & English</li>
        <li>☕ Iced coffee fan</li>
        <li>🌱 Always learning</li>
    </ul>
    </div>""", unsafe_allow_html=True)

# ── Education Timeline ────────────────────────────────────────
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
edu = [
    ("Present", "Currently Enrolled", "Senior High School / College",
     "Studying hard while exploring coding on the side."),
    ("2024", "Python Certificate", "Codedex",
     "Completed a beginner Python course and got my first coding certificate!"),
]
for year, degree, school, detail in edu:
    st.markdown(f"""<div class="timeline-item">
        <div class="timeline-year">{year}</div>
        <strong>{degree}</strong><br>
        <span style="color:#11998e">{school}</span><br>
        <span style="color:#666; font-size:0.9rem">{detail}</span>
    </div>""", unsafe_allow_html=True)

# ── No fake experience — replaced with learning journey ───────
st.markdown('<div class="section-title">🌱 My Learning Journey</div>', unsafe_allow_html=True)
journey = [
    ("2024", "Discovered Python", "Codedex",
     "Took my first coding course and completed the Python track. Loved it!"),
    ("2024–2025", "Built First Projects", "Self-learning",
     "Started experimenting with Streamlit and building small personal projects like this portfolio."),
    ("2025", "Exploring More", "Online Resources",
     "Looking into HTML, CSS, and basic web development to expand my skills little by little."),
]
for year, role, place, detail in journey:
    st.markdown(f"""<div class="timeline-item">
        <div class="timeline-year">{year}</div>
        <strong>{role}</strong><br>
        <span style="color:#11998e">{place}</span><br>
        <span style="color:#666; font-size:0.9rem">{detail}</span>
    </div>""", unsafe_allow_html=True)

# ── Goals ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">🎯 Goals & Aspirations</div>', unsafe_allow_html=True)
g1, g2 = st.columns(2)
goals_short = ["✅ Get better at Python basics",
               "✅ Build a few more projects to practice",
               "✅ Learn HTML & CSS properly"]
goals_long  = ["🚀 Eventually get into web development",
               "🌍 Build something people actually find useful",
               "📚 Keep learning and not give up"]
with g1:
    st.markdown("<div class='card'><h4>Right Now</h4>" +
                "".join(f"<p>{g}</p>" for g in goals_short) + "</div>", unsafe_allow_html=True)
with g2:
    st.markdown("<div class='card'><h4>Someday 🌟</h4>" +
                "".join(f"<p>{g}</p>" for g in goals_long) + "</div>", unsafe_allow_html=True)

st.caption("© 2025 Maxene Victor · Built with ❤️ using Streamlit")
