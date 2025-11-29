import streamlit as st
import db
import parser
import themes
from datetime import datetime

# Page Config
st.set_page_config(page_title="Roadmap Parser", layout="wide", initial_sidebar_state="collapsed")

# Initialize DB and UI state
if 'db_initialized' not in st.session_state:
    db.init_db()
    st.session_state['db_initialized'] = True

if 'active_page' not in st.session_state:
    st.session_state['active_page'] = "Auto Generate"

THEME_OPTIONS = [
    "Cyberpunk",
    "Sunset Neon",
    "Aqua Glow",
    "Ember Glow",
    "Titanium"
]
if 'theme' not in st.session_state:
    st.session_state['theme'] = THEME_OPTIONS[0]


def apply_selected_theme(theme_name: str):
    """Inject CSS for the chosen theme."""
    if theme_name == "Cyberpunk":
        st.markdown(themes.get_cyberpunk_theme(), unsafe_allow_html=True)
    elif theme_name == "Sunset Neon":
        st.markdown(themes.get_sunset_neon_theme(), unsafe_allow_html=True)
    elif theme_name == "Aqua Glow":
        st.markdown(themes.get_aqua_glow_theme(), unsafe_allow_html=True)
    elif theme_name == "Ember Glow":
        st.markdown(themes.get_ember_glow_theme(), unsafe_allow_html=True)
    elif theme_name == "Titanium":
        st.markdown(themes.get_titanium_theme(), unsafe_allow_html=True)


def import_roadmap(name, text):
    # Normalize name and block duplicates
    chosen_name = (name or "Untitled Roadmap").strip() or "Untitled Roadmap"
    existing = db.get_roadmaps()
    if any(r['name'].strip().lower() == chosen_name.lower() for r in existing):
        st.warning("A roadmap with this name already exists. Please rename it first.")
        return False

    if not text.strip():
        st.error("Please paste some roadmap text.")
        return False

    roadmap_id = db.save_roadmap(chosen_name, text)
    parsed_items = parser.parse_roadmap(text)

    timeframe_map = {}
    count_tf = 0
    for item in parsed_items:
        if item['type'] == 'timeframe':
            parent_id = None
            if item['parent_label'] and item['parent_label'] in timeframe_map:
                parent_id = timeframe_map[item['parent_label']]

            tf_id = db.save_timeframe(roadmap_id, item['label'], item['granularity'], parent_id)
            timeframe_map[item['label']] = tf_id
            count_tf += 1

    unassigned_id = None
    count_tasks = 0
    for item in parsed_items:
        if item['type'] == 'task':
            tf_label = item['timeframe_label']
            tf_id = None

            if tf_label == "Unassigned":
                if not unassigned_id:
                    unassigned_id = db.save_timeframe(roadmap_id, "Unassigned", "generic")
                tf_id = unassigned_id
            elif tf_label in timeframe_map:
                tf_id = timeframe_map[tf_label]
            else:
                if not unassigned_id:
                    unassigned_id = db.save_timeframe(roadmap_id, "Unassigned", "generic")
                tf_id = unassigned_id

            db.save_task(tf_id, item['title'])
            count_tasks += 1

    st.success(f"Imported {count_tf} timeframes and {count_tasks} tasks!")
    return True


def build_pdf(roadmap_label, tasks):
    """Generate a simple PDF of the roadmap tasks grouped by timeframe."""
    try:
        from fpdf import FPDF
    except ImportError:
        st.error("PDF generation requires the 'fpdf' package. Install with: pip install fpdf")
        return None

    # Group tasks by timeframe
    grouped = {}
    for t in tasks:
        grouped.setdefault(t['timeframe_label'], []).append(t)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, roadmap_label, ln=True)
    pdf.ln(4)

    pdf.set_font("Helvetica", "", 12)
    for timeframe, items in grouped.items():
        pdf.set_font("Helvetica", "B", 13)
        pdf.cell(0, 8, timeframe, ln=True)
        pdf.set_font("Helvetica", "", 11)
        for idx, item in enumerate(items, start=1):
            pdf.multi_cell(0, 7, f"- {item['title']}")
        pdf.ln(2)

    pdf_bytes = pdf.output(dest="S").encode("latin-1")
    return pdf_bytes


def handle_rename(roadmap_id: int, state_key: str):
    """Rename a roadmap directly from the editable field."""
    new_name = (st.session_state.get(state_key, "") or "").strip()
    if not new_name:
        st.warning("Please enter a name.")
        return
    existing = db.get_roadmaps()
    if any(r['id'] != roadmap_id and r['name'].strip().lower() == new_name.lower() for r in existing):
        st.warning("A roadmap with this name already exists. Please choose a different name.")
        return
    db.rename_roadmap(roadmap_id, new_name)
    st.success("Roadmap renamed!")
    st.rerun()


def generate_roadmap_text(goal: str) -> str:
    """Generate a simple 4-week roadmap based on a goal string."""
    goal_clean = goal.strip() or "your goal"
    return f"""Month 1 - Foundations for {goal_clean}
Week 1 - Research and Plan
- Define the scope and success criteria for {goal_clean}
- Collect references and best practices
- Outline milestones and deliverables

Week 2 - Setup
- Set up tools, environment, and accounts needed for {goal_clean}
- Create a starter project structure
- Draft a checklist for quality and testing

Week 3 - Build Core
- Implement the core features for {goal_clean}
- Add instrumentation/logging for observability
- Run a first pass of testing and fix critical issues

Week 4 - Polish and Launch
- Refine UX/content and performance for {goal_clean}
- Add documentation/readme for how to use and extend it
- Ship a v1 and collect feedback to plan next steps
"""


def show_import_page():
    with st.form("import_form"):
        name = st.text_input("Name for your Roadmap", placeholder="roadmap_Name")
        text = st.text_area(
            "Paste Roadmap Text",
            height=300,
            placeholder="Month 1...\nWeek 1...\n- Task 1",
        )

        submitted = st.form_submit_button("Analyze", type="primary")

        if submitted:
            success = import_roadmap(name, text)
            if success:
                st.session_state['active_page'] = "View Tasks"
                st.rerun()


def show_auto_page():
    if 'auto_roadmap_text' not in st.session_state:
        st.session_state['auto_roadmap_text'] = ""

    with st.form("auto_form"):
        name = st.text_input("Name for your Roadmap", placeholder="roadmap_Name")
        col_goal, col_btn = st.columns([0.75, 0.25])
        with col_goal:
            goal_prompt = st.text_input("Describe your goal (for auto-generation)", placeholder="give me a roadmap so failure is 100% my fault")
        with col_btn:
            st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
            generate_clicked = st.form_submit_button("Generate", type="secondary")

        text = st.text_area(
            "Generated Roadmap (editable)",
            height=300,
            placeholder="Month 1...\nWeek 1...\n- Task 1",
            value=st.session_state.get('auto_roadmap_text', ""),
        )

        submitted = st.form_submit_button("Analyze", type="primary")

        if generate_clicked:
            st.session_state['auto_roadmap_text'] = generate_roadmap_text(goal_prompt or name or "your goal")
            st.rerun()

        if submitted:
            st.session_state['auto_roadmap_text'] = text
            success = import_roadmap(name, text)
            if success:
                st.session_state['active_page'] = "View Tasks"
                st.rerun()


def show_view_page():
    col1, col_date, col2, col3 = st.columns([0.26, 0.18, 0.28, 0.28])

    roadmaps = db.get_roadmaps()
    if not roadmaps:
        st.info("No roadmaps found. Go to 'Import Roadmap' to add one.")
        return

    def fmt_date(raw):
        try:
            return datetime.fromisoformat(raw).strftime("%d-%b-%Y").lower()
        except Exception:
            return raw[:10]

    with col1:
        selected_roadmap = st.selectbox(
            "Select Roadmap",
            roadmaps,
            format_func=lambda r: r['name'],
        )
        selected_roadmap_id = selected_roadmap['id']
        selected_roadmap_name = selected_roadmap['name']

        name_key = f"roadmap_name_{selected_roadmap_id}"
        st.text_input(
            "Edit name",
            value=selected_roadmap_name,
            key=name_key,
            on_change=handle_rename,
            args=(selected_roadmap_id, name_key),
        )

        c_pdf, c_del = st.columns(2)
        with c_pdf:
            all_tasks_for_pdf = db.get_tasks(selected_roadmap_id, None)
            has_tasks = bool(all_tasks_for_pdf)
            if st.button("Save", type="secondary", disabled=not has_tasks):
                if has_tasks:
                    st.session_state['pdf_bytes'] = build_pdf(selected_roadmap_name, all_tasks_for_pdf)
                    st.session_state['pdf_filename'] = f"{selected_roadmap_name}.pdf"
            if st.session_state.get('pdf_bytes'):
                st.download_button(
                    "Download PDF",
                    st.session_state['pdf_bytes'],
                    file_name=st.session_state.get('pdf_filename', f"{selected_roadmap_name}.pdf"),
                    mime="application/pdf",
                    type="secondary",
                )
        with c_del:
            if st.button("Delete", type="primary"):
                db.delete_roadmap(selected_roadmap_id)
                st.success("Roadmap deleted!")
                st.rerun()

    with col_date:
        st.markdown("**Created**")
        st.markdown(f"<span style='color:#a0a8b8;'>{fmt_date(selected_roadmap['created_at'])}</span>", unsafe_allow_html=True)

    with col2:
        granularity = st.selectbox("Granularity", ["All", "Month", "Week", "Day", "Hour", "Generic"])

    timeframes = db.get_timeframes(selected_roadmap_id, granularity if granularity != "All" else None)
    timeframe_options = {"All": None}
    for tf in timeframes:
        timeframe_options[tf['label']] = tf['id']

    with col3:
        selected_tf_label = st.selectbox("Timeframe", list(timeframe_options.keys()))
        selected_tf_id = timeframe_options[selected_tf_label]

    st.divider()

    tasks = db.get_tasks(selected_roadmap_id, selected_tf_id)

    if not tasks:
        st.info("No tasks found for this selection.")
    else:
        current_group = None
        for task in tasks:
            if task['timeframe_label'] != current_group:
                current_group = task['timeframe_label']
                st.markdown(f"### {current_group}")

            c1, c2 = st.columns([0.05, 0.95])
            with c1:
                is_done = st.checkbox("", value=bool(task['is_done']), key=f"task_{task['id']}")
                if is_done != bool(task['is_done']):
                    db.update_task_status(task['id'], is_done)
                    st.rerun()
            with c2:
                if task['is_done']:
                    st.markdown(f"~~{task['title']}~~")
                else:
                    st.markdown(task['title'])


def main():
    # UI shell styling for nav dots, theme list, and slide animation
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {display: none;}
            .main .block-container {max-width: 1250px; padding: 0.8rem 1rem 1.8rem 1rem;}
            .page-title {margin: 0 0 1rem 0; font-size: 40px; font-weight: 800; color: #e7edf7;}
            /* tighten column padding */
            div[data-testid="column"] {padding-left: 6px !important; padding-right: 6px !important;}
            /* bolder labels */
            label[data-testid="stMetricLabel"], .stTextInput label, .stTextArea label, .stSelectbox label {
                font-size: 16px !important;
                font-weight: 800 !important;
                color: #e7edf7 !important;
            }
            /* button styling */
            .stButton>button[data-testid="baseButton-primary"] {
                color: #0c1424 !important;
                font-weight: 700;
                background: var(--primary, #5f97ff) !important;
                border: 1px solid var(--accent, #7cf0ff) !important;
                box-shadow: 0 8px 22px rgba(0,0,0,0.35), 0 0 0 1px rgba(255,255,255,0.08);
                padding: 0.65rem 1.05rem;
            }
            .stButton>button[data-testid="baseButton-primary"]:hover {
                box-shadow: 0 10px 26px rgba(0,0,0,0.45), 0 0 0 1px rgba(255,255,255,0.14);
            }
            .stButton>button[data-testid="baseButton-secondary"] {
                color: #0c1424 !important;
                font-weight: 700;
                background: linear-gradient(135deg, var(--primary, #5f97ff), var(--accent, #7cf0ff)) !important;
                border: 1px solid var(--primary, #5f97ff) !important;
                box-shadow: 0 10px 26px rgba(0,0,0,0.35), 0 0 0 1px rgba(255,255,255,0.08);
                padding: 0.65rem 1.05rem;
            }
            .stButton>button[data-testid="baseButton-secondary"]:hover {
                box-shadow: 0 12px 32px rgba(0,0,0,0.45), 0 0 0 1px rgba(255,255,255,0.12);
            }
            /* keep download button simple */
            .stDownloadButton>button {
                font-weight: 700;
                background: #131a27;
                border: 1px solid #1f2735;
                color: #e7edf7;
                padding: 0.65rem 1.05rem;
                border-radius: 10px;
            }
            /* pointer cursor on selects */
            .stSelectbox label {cursor: pointer;}
            .stSelectbox div[data-baseweb="select"] > div {cursor: pointer;}

            /* Nav dots */
            .nav-dots [role="radiogroup"] {gap: 2rem !important; justify-content: center;}
            .nav-dots label {
                padding: 6px 10px 6px 28px;
                margin: 0;
                position: relative;
                cursor: pointer;
                font-size: 22px;
                font-weight: 700;
                letter-spacing: 0.01em;
                color: #e7edf7;
            }
            .nav-dots label div:first-of-type {display: none;} /* hide default radio icon */
            .nav-dots label div:last-of-type {
                color: inherit;
                font-size: inherit;
                font-weight: inherit;
            }
            .nav-dots label::before {
                content: "";
                position: absolute;
                left: 0;
                top: 50%;
                transform: translateY(-50%);
                width: 14px;
                height: 14px;
                border-radius: 50%;
                border: 2px solid #6b768a;
                background: transparent;
            }
            .nav-dots label:has(input:checked)::before {
                background: #ff5660;
                border-color: #ff5660;
                box-shadow: 0 0 0 4px rgba(255, 86, 96, 0.25);
            }

            /* Theme pills (top right) */
            .theme-pills {display: flex; justify-content: flex-end; margin-top: 0.5rem;}
            .theme-pills [role="radiogroup"] {gap: 0.4rem !important; flex-wrap: wrap; justify-content: flex-end;}
            .theme-pills label {
                padding: 8px 12px;
                margin: 0;
                position: relative;
                cursor: pointer;
                border-radius: 10px;
                background: #131a27;
                border: 1px solid #1f2735;
                color: #e7edf7;
                font-weight: 600;
                letter-spacing: 0.01em;
                transition: border-color 0.15s ease, box-shadow 0.2s ease, transform 0.15s ease;
            }
            .theme-pills label div:first-of-type {display: none;} /* hide default radio icon */
            .theme-pills label div:last-of-type {
                color: inherit;
                font-weight: inherit;
            }
            .theme-pills label:hover {transform: translateY(-1px);}
            .theme-pills label:has(input:checked) {
                border-color: #5f97ff;
                box-shadow: 0 12px 24px rgba(0,0,0,0.25);
            }

            .page-shell {animation: slideIn 0.35s ease;}
            @keyframes slideIn {from {opacity: 0; transform: translateY(8px);} to {opacity: 1; transform: translateY(0);}}
        </style>
        """,
        unsafe_allow_html=True,
    )

    apply_selected_theme(st.session_state['theme'])

    st.markdown('<div class="nav-dots">', unsafe_allow_html=True)
    nav_pages = ["Auto Generate", "Import Roadmap", "View Tasks"]
    nav_choice = st.radio(
        "Navigation",
        nav_pages,
        horizontal=True,
        index=nav_pages.index(st.session_state['active_page']),
        label_visibility="collapsed",
        key="nav_radio",
    )
    st.markdown('</div>', unsafe_allow_html=True)
    st.session_state['active_page'] = nav_choice

    top_bar_left, top_bar_right = st.columns([0.55, 0.45])
    with top_bar_left:
        if st.session_state['active_page'] == "Import Roadmap":
            title_text = "Roadmap"
        elif st.session_state['active_page'] == "Auto Generate":
            title_text = "Auto Generate"
        else:
            title_text = "Your Tasks"
        st.markdown(f"<h1 class='page-title'>{title_text}</h1>", unsafe_allow_html=True)
    with top_bar_right:
        st.markdown('<div class="theme-pills">', unsafe_allow_html=True)
        theme_choice = st.radio(
            "Theme selector",
            THEME_OPTIONS,
            horizontal=True,
            index=THEME_OPTIONS.index(st.session_state['theme']),
            label_visibility="collapsed",
            key="theme_radio",
        )
        st.markdown('</div>', unsafe_allow_html=True)
        if theme_choice != st.session_state['theme']:
            st.session_state['theme'] = theme_choice
            st.rerun()

    st.markdown('<div class="page-shell">', unsafe_allow_html=True)
    if st.session_state['active_page'] == "Import Roadmap":
        show_import_page()
    elif st.session_state['active_page'] == "Auto Generate":
        show_auto_page()
    elif st.session_state['active_page'] == "View Tasks":
        show_view_page()
    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
