
import streamlit as st

st.set_page_config(page_title="Projects | Maxene Victor", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f5f7fa; }
    .proj-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        height: 100%;
        border-top: 5px solid #11998e;
        margin-bottom: 20px;
    }
    .proj-card:hover { box-shadow: 0 8px 30px rgba(17,153,142,0.2); }
    .tag { background:#e8f5e9; color:#2e7d32; border-radius:10px; padding:3px 10px;
           font-size:0.78rem; margin:2px; display:inline-block; }
    .status-wip    { background:#fef3c7; color:#92400e; border-radius:8px; padding:2px 10px; font-size:0.78rem; }
    .status-done   { background:#dbeafe; color:#1e40af; border-radius:8px; padding:2px 10px; font-size:0.78rem; }
    .status-school { background:#f3e8ff; color:#6b21a8; border-radius:8px; padding:2px 10px; font-size:0.78rem; }
    .section-title { font-size:1.4rem; font-weight:700; color:#302b63; border-left:5px solid #11998e; padding-left:12px; margin:28px 0 16px; }
    .note-box { background:#fff8e1; border-left:4px solid #f9a825; border-radius:10px; padding:14px 18px; color:#555; font-size:0.9rem; margin-bottom:20px; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🛠️ My Projects")
st.markdown("*Small steps, but they're mine. 🌱*")
st.markdown('<div class="note-box">👩‍💻 These are beginner projects I built while learning and for school. Nothing fancy — just me practicing and having fun with code!</div>', unsafe_allow_html=True)
st.markdown("---")

# ── Filter ────────────────────────────────────────────────────
filter_tag = st.selectbox("🔍 Filter by Technology", ["All", "Python", "Streamlit", "HTML & CSS", "JavaScript"])

projects = [
    {
        "title": "🐾 Pet Adoption Website",
        "desc": "A website built for a school project where users can browse pets available for adoption. Designed with a clean, friendly layout to encourage people to adopt rather than shop.",
        "tags": ["HTML & CSS", "JavaScript"],
        "status": "school",
        "highlights": ["Browse adoptable pets with photos & details", "Responsive layout using HTML & CSS", "Built as a school project — proud of how it turned out!"],
        "github": None,
        "demo": None,
    },
    {
        "title": "🍎 Teacher's Day Card",
        "desc": "A digital greeting card made for Teacher's Day — a small but fun way to appreciate teachers using HTML, CSS & JavaScript. Uploaded on GitHub!",
        "tags": ["HTML & CSS", "JavaScript"],
        "status": "done",
        "highlights": ["Animated greeting card design", "Built with pure HTML, CSS & JavaScript", "My first project on GitHub! 🎉"],
        "github": "https://github.com/macsyne/teachers-day",
        "demo": None,
    },
    {
        "title": "📋 This Portfolio",
        "desc": "A personal portfolio website built with Streamlit. My first real project — still improving it as I learn more!",
        "tags": ["Python", "Streamlit"],
        "status": "wip",
        "highlights": ["Multi-page Streamlit app", "Custom CSS styling", "My first coding project!"],
        "github": None,
        "demo": None,
    },
    {
        "title": "🧮 Simple Calculator",
        "desc": "A basic calculator built in Python as part of my Codedex learning. Does simple math operations — nothing too crazy.",
        "tags": ["Python"],
        "status": "done",
        "highlights": ["Addition, subtraction, multiplication, division", "Handles divide-by-zero errors", "One of my first Python scripts"],
        "github": None,
        "demo": None,
    },
    {
        "title": "📝 To-Do List App",
        "desc": "A simple to-do list app made with Streamlit. You can add tasks, mark them as done, and delete them.",
        "tags": ["Python", "Streamlit"],
        "status": "done",
        "highlights": ["Add and delete tasks", "Mark tasks as complete", "Built while following a Streamlit tutorial"],
        "github": None,
        "demo": None,
    },
    {
        "title": "🔢 Number Guessing Game",
        "desc": "A fun little number guessing game made in Python. The program picks a random number and you try to guess it!",
        "tags": ["Python"],
        "status": "done",
        "highlights": ["Random number generation", "Gives hints (higher/lower)", "Simple loops and conditionals practice"],
        "github": None,
        "demo": None,
    },
]

status_map   = {"wip": "🟡 In Progress", "done": "🔵 Completed", "school": "📚 School Project"}
status_class = {"wip": "status-wip",     "done": "status-done",  "school": "status-school"}

filtered = [p for p in projects if filter_tag == "All" or filter_tag in p["tags"]]

if not filtered:
    st.warning("No projects match the selected filter. Try 'All'.")
else:
    cols = st.columns(2)
    for i, proj in enumerate(filtered):
        with cols[i % 2]:
            tags_html       = "".join(f'<span class="tag">{t}</span>' for t in proj["tags"])
            highlights_html = "".join(f"<li>{h}</li>" for h in proj["highlights"])
            github_btn      = f'<a href="{proj["github"]}" target="_blank" style="color:#11998e; text-decoration:none">📂 GitHub</a>' if proj["github"] else '<span style="color:#aaa; font-size:0.85rem">📂 Not on GitHub yet</span>'
            demo_btn        = f'<a href="{proj["demo"]}" target="_blank" style="margin-left:8px; color:#11998e; text-decoration:none">🚀 Live Demo</a>' if proj["demo"] else ""
            st.markdown(f"""
            <div class="proj-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px">
                    <h4 style="margin:0">{proj["title"]}</h4>
                    <span class="{status_class[proj['status']]}">{status_map[proj['status']]}</span>
                </div>
                <p style="color:#555; font-size:0.92rem">{proj["desc"]}</p>
                <div>{tags_html}</div>
                <ul style="color:#444; font-size:0.88rem; margin-top:12px">{highlights_html}</ul>
                <div style="margin-top:12px">
                    {github_btn}
                    {demo_btn}
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.info("🌱 More projects coming as I keep learning. Watch this space!")
st.caption("© 2025 Maxene Victor · Built with ❤️ using Streamlit")
