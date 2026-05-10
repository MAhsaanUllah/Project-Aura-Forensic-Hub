import streamlit as st
from fpdf import FPDF
import requests
import re
import os
from datetime import datetime

# 1. PROFESSIONAL PDF ENGINE (Unicode Safe)
class AURA_PDF(FPDF):
    def __init__(self, case_id="AURA-999X", investigator="Neural Agent"):
        super().__init__()
        self.case_id = case_id
        self.investigator = investigator
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150, 150, 150)
        footer_content = f"Case: {self.case_id} | Page {self.page_no()} | Audit Time: {self.timestamp} | Project Aura (AMD MI300X)"
        self.cell(0, 10, footer_content, 0, 0, 'C')

def create_pdf(query, result, case_id, investigator):
    pdf = AURA_PDF(case_id, investigator)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    
    # --- HEADER ---
    pdf.set_fill_color(11, 11, 18)
    pdf.rect(0, 0, 210, 50, 'F')
    pdf.set_text_color(78, 204, 163)
    pdf.set_font("Helvetica", 'B', 24)
    pdf.ln(10)
    pdf.cell(0, 15, txt="PROJECT AURA", ln=True, align='C')
    pdf.set_font("Helvetica", 'I', 10)
    pdf.cell(0, 5, txt="Neural Forensic Intelligence Audit Report", ln=True, align='C')
    
    # --- METADATA BAR ---
    pdf.set_y(40)
    pdf.set_font("Helvetica", 'B', 9)
    pdf.set_text_color(255, 255, 255)
    meta_text = f"CASE ID: {case_id}   |   INVESTIGATOR: {investigator.upper()}   |   DATE: {pdf.timestamp}"
    pdf.cell(0, 10, txt=meta_text, ln=True, align='C')

    # --- SUMMARY ---
    pdf.set_y(60)
    pdf.set_text_color(40, 40, 40)
    pdf.set_font("Helvetica", 'B', 12)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 10, txt=" 1. INVESTIGATION INQUIRY", ln=True, fill=True)
    pdf.ln(4)
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 7, txt=query)
    
    # --- FINDINGS ---
    pdf.ln(10)
    pdf.set_font("Helvetica", 'B', 12)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 10, txt=" 2. FORENSIC INTELLIGENCE FINDINGS", ln=True, fill=True)
    pdf.ln(4)
    pdf.set_font("Helvetica", '', 10)
    pdf.multi_cell(0, 7, txt=result)
    
    return pdf.output()

def generate_forensic_intelligence(query):
    # Use environment variable for the endpoint, fallback to localhost for dev
    AMD_ENDPOINT = os.getenv("AMD_INFERENCE_ENDPOINT", "http://localhost:8000/v1/chat/completions")
    API_KEY = os.getenv("AMD_API_KEY", "EMPTY")
    
    payload = {
        "model": "Qwen/Qwen2-7B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a senior digital forensic investigator. Provide detailed, analytical, and structured findings."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.3
    }
    headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY != "EMPTY" else {}
    
    try:
        response = requests.post(AMD_ENDPOINT, json=payload, headers=headers, timeout=180)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Neural Analysis Error: {str(e)}"

# 3. STREAMLIT CONFIG
st.set_page_config(page_title="Project Aura", page_icon="🔍", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
        /* Lock Sidebar: Hide ALL collapse/resize controls */
        [data-testid="stSidebarNav"] { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stSidebarCollapsedControl"] { display: none !important; }
        section[data-testid="stSidebar"] button { display: none !important; }
        [data-testid="stSidebarResizer"] { display: none !important; }
        
        /* Force Sidebar Width and Visibility */
        section[data-testid="stSidebar"] { 
            min-width: 320px !important; 
            max-width: 320px !important; 
            background-color: #11111b !important; 
            border-right: 2px solid #4ecca333 !important; 
            visibility: visible !important;
        }
        
        /* Hide the 'X' close button inside sidebar if it appears */
        button[kind="headerNoSpacing"] { display: none !important; }
        
        .stApp { background-color: #0b0b12; color: white; }
        
        .stMainBlockContainer { 
            max-width: 850px !important; 
            margin: auto !important; 
            padding-top: 2rem !important; 
        }

        /* 10px Gap for Presets */
        div[data-testid="stHorizontalBlock"] {
            gap: 10px !important;
        }
        
        div[data-testid="stTextArea"] textarea { 
            background: rgba(255, 255, 255, 0.02) !important; 
            border: 2px solid #4ecca3 !important; 
            color: #4ecca3 !important; 
            border-radius: 12px !important; 
            height: 180px !important; 
        }
        
        .stButton button { 
            width: 100% !important; 
            border-radius: 8px !important; 
            font-weight: 700 !important; 
        }
        
        div.run-btn button { 
            background: linear-gradient(90deg, #4ecca3, #00f2fe) !important; 
            color: #0b0b12 !important; 
            height: 55px !important; 
            font-size: 1.1rem !important; 
        }
        
        div.clear-btn button {
            background: rgba(255, 255, 255, 0.05) !important;
            color: #ff4b4b !important;
            border: 1px solid #ff4b4b44 !important;
            height: 55px !important;
        }
        
        .preset-btn button {
            background: rgba(78, 204, 163, 0.1) !important;
            color: #4ecca3 !important;
            border: 1px solid #4ecca344 !important;
            height: 45px !important;
            font-size: 0.85rem !important;
        }
        
        .result-box { 
            background: rgba(0, 242, 254, 0.05); 
            border-left: 5px solid #00f2fe; 
            padding: 25px; 
            border-radius: 12px; 
            margin-top: 25px; 
            line-height: 1.6; 
            white-space: pre-wrap; 
        }

        /* Spacing for Sidebar Content */
        .sidebar-content {
            padding: 10px 0px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>🌸</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color:#4ecca3; margin-top:0;'>AURA CONTROL</h2>", unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.markdown("### 📁 CASE METADATA")
    case_id = st.text_input("Case Reference", value="AURA-2026-X1")
    investigator = st.text_input("Investigator", value="Senior Agent")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("📍 **Compute:** AMD Instinct MI300X")
    st.info("🤖 **Engine:** Qwen-72B-Agentic")
    st.info("🛠️ **Platform:** ROCm 6.0 + vLLM")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption(f"LIVE TIMESTAMP: {datetime.now().strftime('%H:%M:%S UTC')}")
    st.caption("© 2026 Project Aura | AMD MI300X")
    st.markdown('</div>', unsafe_allow_html=True)

# MAIN
st.markdown("<h1 style='text-align: center; font-size: 3rem; font-weight: 800; background: linear-gradient(90deg, #00f2fe, #4ecca3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom:0;'>PROJECT AURA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6; margin-bottom:20px;'>Forensic Intelligence Hub</p>", unsafe_allow_html=True)

# QUICK PRESETS AREA (Horizontal with 10px gap)
st.markdown("### ⚡ QUICK PRESETS")
cp1, cp2, cp3 = st.columns(3)
with cp1:
    st.markdown('<div class="preset-btn">', unsafe_allow_html=True)
    if st.button("🔍 Kernel Audit", key="kp1"):
        st.session_state.query_input = "Perform a deep-trace audit on these kernel logs. Identify any suspicious process injections or unauthorized persistence drivers."
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with cp2:
    st.markdown('<div class="preset-btn">', unsafe_allow_html=True)
    if st.button("📡 C2 Analysis", key="kp2"):
        st.session_state.query_input = "Analyze this network traffic capture for Command & Control (C2) heartbeat patterns. Look for high-entropy payloads and beaconing intervals."
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with cp3:
    st.markdown('<div class="preset-btn">', unsafe_allow_html=True)
    if st.button("🛡️ Metadata Scrub", key="kp3"):
        st.session_state.query_input = "Conduct a forensic metadata scrub on the following file header. Identify document checksum mismatches and 'Incremental Update' anomalies."
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if "query_input" not in st.session_state:
    st.session_state.query_input = ""

st.markdown("<br>", unsafe_allow_html=True)
query_text = st.text_area("Inquiry", value=st.session_state.query_input, placeholder="Describe the forensic investigation or paste system logs...", label_visibility="collapsed")

# ACTION BUTTONS
col_run, col_clear = st.columns([3, 1])
with col_run:
    st.markdown('<div class="run-btn">', unsafe_allow_html=True)
    run_exec = st.button("Initiate Neural Analysis")
    st.markdown('</div>', unsafe_allow_html=True)
with col_clear:
    st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
    if st.button("Clear Buffer"):
        st.session_state.query_input = ""
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

if run_exec and query_text:
    with st.status("🌌 Accessing AMD MI300X Neural Clusters...", expanded=False):
        intel = generate_forensic_intelligence(query_text)
    
    st.markdown(f"<div class='result-box'><h3>Forensic Intelligence Report</h3><p>{intel}</p></div>", unsafe_allow_html=True)
    
    try:
        pdf_report = create_pdf(query_text, intel, case_id, investigator)
        st.download_button(
            label="📥 DOWNLOAD PROFESSIONAL PDF REPORT",
            data=pdf_report,
            file_name=f"Aura_Report_{case_id}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as e:
        st.error(f"PDF Generation Failed: {str(e)}")
elif run_exec:
    st.warning("Please provide an investigation inquiry.")
