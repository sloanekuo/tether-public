# ------------------------------------------------------------------
# APP.PY V5.0 (The Hard-Lock Profile)
# ------------------------------------------------------------------
# Changelog:
# 1. Logic: Hard-coded Identity definitions to kill poetic hallucinations.
# 2. Tone: Enforced "Sapiens" biological metaphors (Metabolic, Oxygenate).
# 3. Output: "The Tether Profile" is the standard.
# 4. Privacy: Strict No-Log / Ephemeral Session.
# ------------------------------------------------------------------

import streamlit as st
import re
import fitz  # PyMuPDF
import docx
import pandas as pd
import altair as alt
import google.generativeai as genai
from datetime import datetime
import uuid

# ------------------------------------------------------------------
# CONFIGURATION & SECRETS
# ------------------------------------------------------------------
st.set_page_config(page_title="Tether V5.0", page_icon="🧬", layout="wide")

# Initialize Session ID (For ephemeral session tracking only)
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

# Setup Gemini
if "gemini" in st.secrets:
    genai.configure(api_key=st.secrets["gemini"]["api_key"])
else:
    st.error("Gemini API Key not found. Please add it to Streamlit Secrets.")
    st.stop()

# ------------------------------------------------------------------
# 1. CORE LOGIC
# ------------------------------------------------------------------

BRIDGE_VERBS = [
    "negotiate", "close", "prospect", "canvass", "pitch", "lobby", "advocate", 
    "rally", "galvanize", "broker", "influence", "charm", "convert", "recruit", 
    "source", "interview", "hire", "onboard", "persuade", "sell", "upsell",
    "win", "secure", "capture", "retain", "deal", "network",
    "align", "unify", "integrate", "merge", "mentor", "coach", "empower", 
    "facilitate", "mediate", "liaise", "collaborate", "partner", "guide", 
    "teach", "train", "present", "speak", "communicate", "translate", 
    "bridge", "connect", "represent", "champion", "evangelize", "foster",
    "cultivate", "nurture", "relationship", "stakeholder"
]

BUILDER_VERBS = [
    "build", "architect", "engineer", "develop", "code", "program", "design",
    "create", "construct", "forge", "implement", "deploy", "launch", "ship",
    "prototype", "draft", "compose", "write", "author", "fabricate", "assemble",
    "invent", "innovate", "pioneer", "found", "establish", "generate", "produce",
    "craft", "devise", "formulate", "conceptualize", "model"
]

OPERATOR_VERBS = [
    "manage", "operate", "run", "maintain", "support", "administer", "optimize",
    "streamline", "scale", "execute", "process", "handle", "oversee", "supervise",
    "direct", "coordinate", "monitor", "track", "report", "analyze", "audit",
    "ensure", "enforce", "comply", "regulate", "budget", "forecast", "schedule",
    "logistics", "inventory", "efficiency", "workflow", "systematize", "organize"
]

SALES_KEYWORDS = ["sales", "account", "business development", "biz dev", "recruiter", "talent acquisition", "pr", "public relations", "brand", "marketing", "client", "customer success"]
EXECUTIVE_KEYWORDS = ["chief", "president", "vp", "vice president", "head of", "director", "founder", "c-suite", "principal"]

def analyze_archetype(text):
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    
    builder_score = sum(10 for w in words if w in BUILDER_VERBS)
    operator_score = sum(10 for w in words if w in OPERATOR_VERBS)
    bridge_score = sum(10 for w in words if w in BRIDGE_VERBS)

    is_commercial = any(k in text_lower for k in SALES_KEYWORDS)
    is_executive = any(k in text_lower for k in EXECUTIVE_KEYWORDS)

    if is_commercial:
        bridge_score = int(bridge_score * 1.5)

    if is_executive:
        shift = int(operator_score * 0.2)
        operator_score -= shift
        bridge_score += shift

    total = builder_score + operator_score + bridge_score
    if total == 0:
        return {"Builder": 0, "Operator": 0, "Bridge": 0, "Total": 1}

    return {
        "Builder": builder_score,
        "Operator": operator_score,
        "Bridge": bridge_score,
        "Total": total
    }

def get_archetype_percentages(scores):
    total = scores['Total']
    pcts = {
        "Builder": round((scores['Builder'] / total) * 100),
        "Operator": round((scores['Operator'] / total) * 100),
        "Bridge": round((scores['Bridge'] / total) * 100)
    }
    sorted_pcts = sorted(pcts.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_pcts[0]
    secondary = sorted_pcts[1]
    
    gap = primary[1] - secondary[1]
    is_hybrid = gap < 20
    
    return pcts, sorted_pcts, is_hybrid

# ------------------------------------------------------------------
# 2. FILE PARSING
# ------------------------------------------------------------------

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# ------------------------------------------------------------------
# 3. GEMINI AI GENERATION (THE HARD-LOCK PROFILE V5.0)
# ------------------------------------------------------------------

def generate_stroma_audit(text, pcts, sorted_pcts, is_hybrid):
    primary_name = sorted_pcts[0][0]
    secondary_name = sorted_pcts[1][0]
    
    # 1. Identity Logic (Hard-Coded Sapiens Descriptions)
    # This prevents the AI from inventing "Tapestries" or "Mandarin Blood".
    identity_logic = {
        "Builder": "The Hunter (Kinetic Energy). You are a metabolic engine. Your biology is designed to convert chaos into structure. You do not just 'work'; you hunt for results. Stasis feels like dying.",
        "Bridge": "The Pollinator (Conductive Energy). You are the connective tissue. Your biology is designed to carry signals across nerves and arteries. You do not just 'communicate'; you oxygenate the system. In isolation, you starve.",
        "Operator": "The Groundskeeper (Structural Energy). You are the immune system. Your biology is designed to detect errors and preserve reality. You do not just 'manage'; you protect the hive from entropy."
    }
    
    # 2. Friction Logic (The Physics)
    friction_logic = {
        "Builder": "You introduce SPEED into a system designed for STASIS. To a slow manager, your momentum looks like recklessness.",
        "Bridge": "You introduce CONNECTION into a system designed for SILOS. To a hoarding manager, your communication looks like a leak.",
        "Operator": "You introduce TRUTH into a system designed for DELUSION. To a chaotic manager, your data looks like negativity."
    }
    
    # 3. Habitat Logic (The Structural Advice)
    habitat_logic = {
        "Builder": "You belong in a High-Velocity Environment (Startups, Crisis Response). Stop trying to run a race in a prison cell.",
        "Bridge": "You belong in a Networked Environment (Matrix Orgs, Cross-Functional Teams). Stop trying to build bridges in a kingdom of walls.",
        "Operator": "You belong in a High-Fidelity Environment (Operations, Safety, Audit). Stop trying to organize a burning building."
    }
    
    primary_definition = identity_logic[primary_name]
    friction_context = friction_logic[primary_name]
    habitat_context = habitat_logic[primary_name]

    prompt = f"""
    You are Nex, the Evolutionary Psychologist for Stroma Labs.
    Your job is to diagnose the "System Incompatibility" between the user's biology and their corporate environment.
    
    USER SPECIES DATA:
    - Archetype: {primary_name} ({sorted_pcts[0][1]}%)
    - Identity Definition: "{primary_definition}"
    - Friction Law: "{friction_context}"
    - Habitat Law: "{habitat_context}"
    
    INSTRUCTIONS:
    1. **Tone:** "Sapiens" meets "Noir." Clinical, anthropological, but visceral. Simple, direct English. Avoid "Corporate" words.
    2. **Concept:** Treat "Burnout" not as weakness, but as "System Overheat" caused by incompatible physics.
    3. **Privacy:** End with the standard Stroma Labs privacy disclaimer.

    OUTPUT FORMAT:

    ## The Tether Profile

    ### 1. THE SPECIES (Who You Are)
    [Use the 'Identity Definition' provided above exactly as written. Do not add metaphors about tapestries, weaving, or blood cocktails. State the definition clearly.]
    **The Instinct:** [A single sentence defining what their brain craves based on the definition.]

    ### 2. THE FRICTION (Why You Overheated)
    [Explain the crash. Use the 'Friction Law' provided above.]
    * **The Physics:** You didn't burn out because you are weak. You burned out because you are a **{primary_name}** trapped in a system designed for the opposite.
    * **The Crash:** [Explain how their specific strength (Speed/Connection/Truth) triggered a system immune response. Use biological metaphors like "White Blood Cell vs Tumor".]

    ### 3. THE GASLIGHT DECODER (Translation of Abuse)
    [Find 3 specific strengths in the resume that a toxic boss likely twisted into insults.]
    * **The Insult:** "They likely called you [Insert Negative Label like 'Aggressive', 'Disruptive', 'Rigid']."
    * **The Translation:** "The truth is, you simply [Insert the High-Value Action they actually took, e.g., 'Moved faster than they could think']."

    ### 4. THE HABITAT
    {habitat_context}

    RESUME DATA:
    {text[:3000]}
    
    PRIVACY:
    *Privacy Notice: Stroma Labs does not store your personal data. This session is automatically erased.*
    """
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash') 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating audit: {e}"

# ------------------------------------------------------------------
# 4. UI/UX
# ------------------------------------------------------------------

st.title("Tether.")
st.markdown("Run a forensic audit on your career. See why you are a threat.")
st.caption("🔒 Privacy First: Stroma Labs does not store your personal data. All analysis is automatically erased.")

uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

if uploaded_file is not None:
    # 1. Parse
    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = extract_text_from_docx(uploaded_file)
        
    # 2. Analyze
    scores = analyze_archetype(resume_text)
    pcts, sorted_pcts, is_hybrid = get_archetype_percentages(scores)
    
    primary_name = sorted_pcts[0][0]
    secondary_name = sorted_pcts[1][0]
    
    # 3. Visuals (Top Section)
    st.divider()
    
    st.caption("Dominant Signal")
    if is_hybrid:
        st.header(f"{primary_name} + {secondary_name}")
    else:
        st.header(primary_name)
    
    # Layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        legend_col, chart_col = st.columns([0.5, 1])
        
        with legend_col:
            st.markdown("##### Signal DNA")
            color_map = {"Builder": "#20BF55", "Operator": "#2F75C6", "Bridge": "#E1BC29"}
            
            for arch in ['Builder', 'Operator', 'Bridge']:
                color = color_map[arch]
                pct = pcts[arch]
                st.markdown(f"<span style='color:{color}'>■</span> {arch} {pct}%", unsafe_allow_html=True)

        with chart_col:
            chart_df = pd.DataFrame({
                'Archetype': ['Builder', 'Operator', 'Bridge'],
                'Percentage': [pcts['Builder'], pcts['Operator'], pcts['Bridge']],
                'Color': ['#20BF55', '#2F75C6', '#E1BC29']
            })
            
            donut = alt.Chart(chart_df).mark_arc(innerRadius=40).encode(
                theta=alt.Theta(field="Percentage", type="quantitative"),
                color=alt.Color(field="Color", type="nominal", scale=None),
                tooltip=['Archetype', 'Percentage']
            ).properties(width=160, height=160)
            
            st.altair_chart(donut, use_container_width=False)

    with col2:
        with st.spinner("Analyzing Biological Compatibility..."):
            audit_result = generate_stroma_audit(resume_text, pcts, sorted_pcts, is_hybrid)
            st.markdown(audit_result)
            
# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: rgba(255, 255, 255, 0.5); font-size: 12px; margin-top: 20px; font-weight: 300;'>
        © 2025 Stroma Labs. R&D for the Concurrent Reality.<br>
        Stroma Labs does not store personal user data.
    </div>
    """, 
    unsafe_allow_html=True
)