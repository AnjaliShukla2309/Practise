import streamlit as st
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Prakash Tiwari - Resume",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize theme in session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Initialize selected page in session state
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "📋 About"

# Function to get theme colors
def get_theme_colors(theme):
    if theme == "dark":
        return {
            "bg_main": "#1a1a1a",
            "bg_card": "#2d2d2d",
            "text_primary": "#ffffff",
            "text_secondary": "#cccccc",
            "border": "#444444",
            "primary_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "card_shadow": "0 2px 8px rgba(0,0,0,0.3)"
        }
    else:
        return {
            "bg_main": "#f5f5f5",
            "bg_card": "#ffffff",
            "text_primary": "#333333",
            "text_secondary": "#666666",
            "border": "#e0e0e0",
            "primary_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "card_shadow": "0 2px 8px rgba(0,0,0,0.1)"
        }

theme_colors = get_theme_colors(st.session_state.theme)

# Custom CSS with theme support
st.markdown(f"""
<style>
    * {{
        margin: 0;
        padding: 0;
    }}
        
    /* Fix Streamlit top header background */
    [data-testid="stHeader"] {{
        background-color: {theme_colors['bg_main']} !important;
    }}

    
    /* Hide Deploy button */
    button[kind="header"] {{
        display: none !important;
    }}

    /* Hide three dots menu */
    button[data-testid="baseButton-headerMenu"] {{
        display: none !important;
    }}


    body {{
        background-color: {theme_colors['bg_main']} !important;
        color: {theme_colors['text_primary']} !important;
    }}
    
    .main {{
        background-color: {theme_colors['bg_main']};
        color: {theme_colors['text_primary']};
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: {theme_colors['bg_main']};
    }}
    
    [data-testid="stSidebar"] * {{
        color: {theme_colors['text_primary']} !important;
    }}
    
    /* Increase radio button and navigation font size */
    [data-testid="stRadio"] {{
        font-size: 18px !important;
    }}
    
    [data-testid="stRadio"] label {{
        color: {theme_colors['text_primary']} !important;
        font-size: 18px !important;
        padding: 12px 8px !important;
    }}
    
    /* Increase icon size in navigation */
    [data-testid="stRadio"] label span {{
        font-size: 22px !important;
        margin-right: 10px !important;
    }}
    
    /* Increase sidebar heading size */
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        font-size: 20px !important;
        margin-top: 20px !important;
    }}
    
    /* Multiselect dropdown styling */
    [data-testid="stMultiSelect"] {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
    }}
    
    [data-testid="stMultiSelect"] > div {{
        background-color: {theme_colors['bg_card']} !important;
        border: 2px solid #667eea !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }}
    
    [data-testid="stMultiSelect"] input {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
        border-color: {theme_colors['border']} !important;
    }}
    
    [data-testid="stMultiSelect"] > div > div {{
        color: {theme_colors['text_primary']} !important;
    }}
    
    /* Multiselect/Select input main styling - more aggressive */
    [data-baseweb="select"] {{
        background-color: {theme_colors['bg_card']} !important;
    }}
    
    [data-baseweb="select"] > div {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
    }}
    
    [data-baseweb="input"] {{
        background-color: {theme_colors['bg_card']} !important;
    }}
    
    /* Input field text color */
    [data-baseweb="input"] input {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
        border-color: {theme_colors['border']} !important;
    }}
    
    /* All input text styling */
    input {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
    }}
    
    input::placeholder {{
        color: {theme_colors['text_secondary']} !important;
    }}
    
    /* Input field placeholder */
    [data-baseweb="input"] input::placeholder {{
        color: {theme_colors['text_secondary']} !important;
    }}
    
    /* Multiselect tags/pills styling */
    [data-baseweb="tag"] {{
        background-color: #667eea !important;
        color: white !important;
        border-radius: 6px !important;
        padding: 6px 12px !important;
        margin: 4px !important;
    }}
    
    /* Dropdown menu items */
    [role="listbox"] {{
        background-color: {theme_colors['bg_card']} !important;
        border: 1px solid {theme_colors['border']} !important;
    }}
    
    [role="option"] {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
        padding: 10px 15px !important;
    }}
    
    [role="option"]:hover {{
        background-color: #667eea !important;
        color: white !important;
    }}
    
    /* Select input styling */
    [data-baseweb="select"] {{
        background-color: {theme_colors['bg_card']} !important;
    }}
    
    /* Tooltip styling - all tooltip elements */
    div[role="tooltip"],
    .stTooltip,
    .stTooltipHoverTarget,
    [class*="tooltip"] {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
        border: 1px solid {theme_colors['border']} !important;
    }}
    
    /* Popover styling */
    [class*="popover"],
    [role="tooltip"] {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
    }}
    
    /* All buttons */
    button {{
        background-color: {theme_colors['bg_card']} !important;
        color: {theme_colors['text_primary']} !important;
        border: 1px solid {theme_colors['border']} !important;
    }}
    
    button:hover {{
        background-color: {theme_colors['border']} !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4) !important;
    }}
    
    /* Main content area styling */
    [data-testid="stMainBlockContainer"] {{
        background-color: {theme_colors['bg_main']};
    }}
    
    /* All text elements */
    p, span, div, h1, h2, h3, h4, h5, h6, label {{
        color: {theme_colors['text_primary']} !important;
    }}
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {{
        color: {theme_colors['text_primary']} !important;
        font-weight: 700;
    }}
    
    /* Main heading enhancement */
    [data-testid="stMainBlockContainer"] h1 {{
        font-size: 2.5rem !important;
        margin-bottom: 20px !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    /* Header section h1 - keep visible */
    .header-section h1 {{
        color: white !important;
        -webkit-text-fill-color: white !important;
        background: none !important;
    }}
    
    /* Section heading enhancement */
    [data-testid="stMainBlockContainer"] h2 {{
        font-size: 2rem !important;
        margin: 40px 0 20px 0 !important;
        padding-bottom: 15px !important;
        border-bottom: 3px solid #667eea !important;
    }}
    
    /* Links */
    a {{
        color: #667eea !important;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    a:hover {{
        color: #764ba2 !important;
        text-decoration: underline;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        background-color: {theme_colors['bg_card']};
        border-radius: 10px;
        padding: 10px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        border-radius: 5px;
        font-weight: 600;
    }}
    
    .header-section {{
        background: {theme_colors['primary_gradient']};
        color: white;
        padding: 40px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 30px;
    }}
    
    .skill-card {{
        background: {theme_colors['bg_card']};
        padding: 18px 20px;
        border-radius: 10px;
        box-shadow: {theme_colors['card_shadow']};
        margin: 12px 0;
        color: {theme_colors['text_primary']};
        border: 1px solid {theme_colors['border']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
        font-weight: 500;
    }}
    
    .skill-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3) !important;
        border-color: #667eea !important;
    }}
    
    .project-card {{
        background: {theme_colors['bg_card']};
        padding: 28px;
        border-left: 5px solid #667eea;
        border-radius: 12px;
        box-shadow: {theme_colors['card_shadow']};
        margin: 20px 0;
        color: {theme_colors['text_primary']};
        border: 1px solid {theme_colors['border']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .project-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }}
    
    .project-card:hover {{
        transform: translateY(-6px);
        box-shadow: 0 12px 28px rgba(102, 126, 234, 0.4) !important;
    }}
    
    .experience-card {{
        background: {theme_colors['bg_card']};
        padding: 24px;
        border-left: 5px solid #764ba2;
        border-radius: 12px;
        margin: 20px 0;
        color: {theme_colors['text_primary']};
        border: 1px solid {theme_colors['border']};
        box-shadow: {theme_colors['card_shadow']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }}
    
    .experience-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 10px 24px rgba(118, 75, 162, 0.3) !important;
    }}
    
    .cert-badge {{
        background: linear-gradient(135deg, {theme_colors['bg_card']} 0%, {theme_colors['bg_card']} 100%);
        padding: 28px 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px;
        border: 2px solid #667eea;
        color: {theme_colors['text_primary']};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
        position: relative;
        overflow: hidden;
    }}
    
    .cert-badge::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    
    .cert-badge:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.4);
        border-color: #764ba2;
    }}
    
    .cert-badge:hover::before {{
        opacity: 1;
    }}
    
    h1, h2, h3 {{
        color: {theme_colors['text_primary']};
    }}
    
    .contact-info {{
        background: linear-gradient(135deg, {theme_colors['bg_card']} 0%, {theme_colors['bg_card']} 100%);
        padding: 32px;
        border-radius: 12px;
        margin: 20px 0;
        color: {theme_colors['text_primary']};
        border: 2px solid #667eea;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }}
    
    .contact-info::before {{
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(20px); }}
    }}
    
    .contact-info:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.35);
    }}
    
    p, span, div {{
        color: {theme_colors['text_primary']} !important;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar with theme toggle at the top
with st.sidebar:
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st.image("https://via.placeholder.com/200x200?text=Prakash+Tiwari", width=150, caption="Prakash Tiwari")
    with col2:
        if st.button("🌙" if st.session_state.theme == "light" else "☀️", key="theme_toggle"):
            st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
            st.rerun()
    
    st.markdown("---")
    st.session_state.selected_page = st.radio("Navigate", [
        "📋 About",
        "🛠️ Skills",
        "💼 Experience",
        "🚀 Projects",
        "🏆 Certifications",
        "📞 Contact"
    ], index=[
        "📋 About",
        "🛠️ Skills",
        "💼 Experience",
        "🚀 Projects",
        "🏆 Certifications",
        "📞 Contact"
    ].index(st.session_state.selected_page))

# Header Section
st.markdown("""
<div class="header-section">
    <h1>�‍💻 PRAKASH TIWARI</h1>
    <h3>Salesforce Senior Engineer | 5x Certified | Full-Stack Developer</h3>
    <p style="margin-top: 20px; font-size: 16px;">
        5x Salesforce Certified with 7 years of experience designing and developing scalable Salesforce solutions
    </p>
</div>
""", unsafe_allow_html=True)

# ABOUT PAGE
if st.session_state.selected_page == "📋 About":
    st.header("Professional Summary")
    st.write("""
    5x Salesforce Certified with 7 years of experience in designing, developing, and implementing Salesforce 
    solutions to streamline business processes and enhance customer engagement. Proficient in Salesforce 
    development, customization, and integration, with expertise in modern web technologies including React.js, 
    Node.js, TypeScript, and Java. Skilled in delivering high-quality CRM solutions, leveraging Apex, Visualforce, 
    Lightning Web Components (LWC), and full-stack development frameworks.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Contact Information")
        st.write("**Mobile:** +91-8770430104")
        st.write("**Email:** prakash-tiwari@outlook.com")
        st.write("**LinkedIn:** www.linkedin.com/in/prakash-tiwari-/")
        st.write("**Location:** Hyderabad, India")
    
    with col2:
        st.subheader("📚 Education")
        st.write("**PG-DAC: Advanced Computing**")
        st.write("CDAC ACTS Hyderabad | August 2018 – February 2019")
        st.write("")
        st.write("**M.Sc. in Computer Science**")
        st.write("Guru Ghasidas Central University, Bilaspur | June 2015 - July 2017")
        st.write("")
        st.write("**B.Sc. in Computer Science**")
        st.write("Guru Ghasidas Central University, Bilaspur | July 2012 - May 2015")

# SKILLS PAGE
elif st.session_state.selected_page == "🛠️ Skills":
    st.header("Technical Skills")
    
    skills_data = {
        "Salesforce Expertise": ["Apex Programming", "Lightning Web Components", "Visualforce Pages", "Process Automation", "Salesforce CPQ", "SOQL & SOSL", "REST & SOAP APIs", "Platform Events"],
        "Web & App Development": ["React.js", "Node.js", "TypeScript", "JavaScript", "HTML", "CSS", "Java", "Express.js"],
        "Cloud Services": ["Sales Cloud", "Service Cloud", "Salesforce Integration", "Email-to-Case", "Web-to-Case"],
        "Development Tools": ["Git", "Bitbucket", "JIRA", "Postman", "Agile (Scrum)"],
        "Data Management": ["Salesforce Reports", "Dashboards", "Data Loader", "Record Types", "Permission Sets"]
    }
    
    for category, skills in skills_data.items():
        st.subheader(f"🔹 {category}")
        cols = st.columns(3)
        for i, skill in enumerate(skills):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="skill-card">
                    <b>{skill}</b>
                </div>
                """, unsafe_allow_html=True)

# EXPERIENCE PAGE
elif st.session_state.selected_page == "💼 Experience":
    st.header("Professional Experience")
    
    st.markdown("""
    <div class="experience-card">
        <h3 style="margin-bottom: 8px; color: #667eea;">Senior Engineer, Applications</h3>
        <p style="margin: 6px 0; font-weight: 600; color: {theme_colors['text_primary']};">Accurate Background</p>
        <p style="margin: 4px 0; color: {theme_colors['text_secondary']}; font-size: 14px;">Hyderabad, India | July 2025 – Present</p>
        <ul style="margin-top: 12px; line-height: 1.8; color: {theme_colors['text_secondary']};">
            <li>Design and develop scalable Salesforce Service Cloud solutions supporting background verification and customer support workflows</li>
            <li>Implement Email-to-Case and Web-to-Case, configure Record Types, Support Processes, and Case Assignment Rules</li>
            <li>Develop and maintain Apex Classes, Triggers, Lightning Web Components, and Flows for complex business logic automation</li>
            <li>Configure Omni-Channel routing and integrated Amazon Connect Contact Center with Salesforce</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3 style="margin-bottom: 8px; color: #667eea;">Senior Software Developer</h3>
        <p style="margin: 6px 0; font-weight: 600; color: {theme_colors['text_primary']};">Qvantel Software Solutions Ltd.</p>
        <p style="margin: 4px 0; color: {theme_colors['text_secondary']}; font-size: 14px;">Hyderabad, India | January 2022 – June 2025</p>
        <ul style="margin-top: 12px; line-height: 1.8; color: {theme_colors['text_secondary']};">
            <li>Designed and implemented Salesforce CRM solutions using Apex, Lightning Web Components, and Visualforce</li>
            <li>Developed custom objects, validation rules, and automation to streamline business processes</li>
            <li>Built React.js-based UI components integrated with Salesforce to improve application usability</li>
            <li>Implemented and maintained REST/SOAP integrations with external systems for seamless data synchronization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-card">
        <h3 style="margin-bottom: 8px; color: #764ba2;">Software Engineer</h3>
        <p style="margin: 6px 0; font-weight: 600; color: {theme_colors['text_primary']};">SpinSci Technologies Pvt. Ltd.</p>
        <p style="margin: 4px 0; color: {theme_colors['text_secondary']}; font-size: 14px;">Hyderabad, India | April 2019 – December 2021</p>
        <ul style="margin-top: 12px; line-height: 1.8; color: {theme_colors['text_secondary']};">
            <li>Designed and implemented custom Salesforce solutions using Apex, Lightning Web Components, and process automation tools</li>
            <li>Developed and optimized flows, triggers, and Lightning Components to automate complex business processes</li>
            <li>Developed scalable Node.js-based server-side applications and backend REST services using Express.js</li>
            <li>Built responsive web applications using React, Redux, TypeScript, and Node.js</li>
            <li>Led end-to-end application implementation strategies and provided technical mentorship to team members</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Key Highlights")
    st.write("✓ 5x Salesforce Certified Professional")
    st.write("✓ Full-stack development expertise across Salesforce and modern web technologies")
    st.write("✓ Strong track record of delivering scalable CRM solutions")
    st.write("✓ Skilled in Agile methodologies and cross-functional team collaboration")

# PROJECTS PAGE
elif st.session_state.selected_page == "🚀 Projects":
    st.header("Featured Projects")
    
    projects = [
        {
            "title": "Salesforce Sales Cloud Optimization",
            "description": "Designed and developed a scalable Sales Cloud solution for a client, increasing lead conversion by 25%. Implemented custom workflows, automated reports, and enhanced dashboard functionality.",
            "tech": ["Apex", "Lightning Components", "Visualforce"],
            "category": "Sales Cloud"
        },
        {
            "title": "Custom LWC and React Application",
            "description": "Built a hybrid Lightning Web Component and React-based application to manage service requests efficiently, reducing resolution time by 30%. Integrated with backend systems for real-time data synchronization.",
            "tech": ["Lightning Web Components", "React.js", "Node.js"],
            "category": "Full-Stack"
        },
        {
            "title": "Salesforce - ERP Integration",
            "description": "Led the integration of Salesforce with a client's ERP system, ensuring real-time data synchronization and enhancing operational visibility. Implemented REST APIs and custom triggers for seamless data flow.",
            "tech": ["REST APIs", "Apex", "SOAP"],
            "category": "Integration"
        },
        {
            "title": "Node.js Data Processing for Salesforce",
            "description": "Developed a Node.js backend to process and synchronize bulk Salesforce data, improving performance by 40%. Implemented batch processing and error handling mechanisms.",
            "tech": ["Node.js", "Express.js", "Data Processing"],
            "category": "Backend"
        }
    ]
    
    # Filter section with enhanced styling
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 30px 0 20px 0;">
        <div></div>
        <p style="font-size: 14px; color: #667eea; font-weight: 600; margin: 0;">Filter Projects by Technology</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        filter_tech = st.multiselect(
            "Select Technology",
            options=sorted(set([tech for p in projects for tech in p["tech"]])),
            placeholder="All Projects",
            label_visibility="collapsed"
        )
    
    # Display selected filters
    if filter_tech:
        st.markdown(f"""
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;">
            {''.join([f'<span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 6px 12px; border-radius: 16px; font-size: 12px; font-weight: 600;">{tech}</span>' for tech in filter_tech])}
        </div>
        """, unsafe_allow_html=True)
    
    for project in projects:
        if not filter_tech or any(tech in filter_tech for tech in project["tech"]):
            st.markdown(f"""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h3 style="margin: 0;">{project['title']}</h3>
                    <span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600;">{project['category']}</span>
                </div>
                <p style="margin: 12px 0; line-height: 1.6; color: {theme_colors['text_secondary']};">{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            tech_cols = st.columns(len(project["tech"]))
            for i, tech in enumerate(project["tech"]):
                with tech_cols[i]:
                    st.write(f"`{tech}`")
            st.markdown("---")

# CERTIFICATIONS PAGE
elif st.session_state.selected_page == "🏆 Certifications":
    st.header("Certifications & Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="cert-badge">
            <h3>🏅 Salesforce Certified Platform Developer II</h3>
            <p>Salesforce, 2024</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cert-badge">
            <h3>🏅 Salesforce Certified Platform Developer I</h3>
            <p>Salesforce, 2023</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cert-badge">
            <h3>🏅 Salesforce Certified JavaScript Developer</h3>
            <p>Salesforce, 2023</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="cert-badge">
            <h3>🏅 Salesforce Certified Agentforce Specialist</h3>
            <p>Salesforce, 2024</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cert-badge">
            <h3>🏅 Salesforce Certified AI Associate</h3>
            <p>Salesforce, 2024</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cert-badge">
            <h3>🎓 School Representative Certificate</h3>
            <p>Mathematical and Computer Science Department<br>Guru Ghasidas University, Bilaspur (C.G.), 2014-15</p>
        </div>
        """, unsafe_allow_html=True)

# CONTACT PAGE
elif st.session_state.selected_page == "📞 Contact":
    st.header("Get In Touch")
    
    st.markdown("""
    <div class="contact-info">
        <h3>📱 Contact Information</h3>
        <p><b>Mobile:</b> +91-8770430104</p>
        <p><b>Email:</b> prakash-tiwari@outlook.com</p>
        <p><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/prakash-tiwari-/" target="_blank">linkedin.com/in/prakash-tiwari-/</a></p>
        <p><b>Location:</b> Hyderabad, India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("Feel free to reach out for:")
    st.write("✓ Salesforce development opportunities")
    st.write("✓ CRM solutions and consulting")
    st.write("✓ Full-stack development projects")
    st.write("✓ Collaboration and partnerships")
    
    st.markdown("---")
    st.write("*Last updated: March 2026*")