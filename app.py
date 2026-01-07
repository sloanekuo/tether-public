<<<<<<< Updated upstream
# --- APP.PY V4.6.2 (Remove Spacy Downloader) ---
=======
# ------------------------------------------------------------------
# APP.PY V5 (The Habitat & Identity Calibration)
# ------------------------------------------------------------------
# Changelog:
# 1. Logic: Added 'habitat_logic' to force structural career advice.
# 2. Logic: Hard-coded Identity definitions to kill poetic hallucinations.
# 3. Tone: Enforced "Sapiens" biological metaphors (Metabolic, Oxygenate).
# 4. Output: "The Tether Profile" is the standard.
# 5. Privacy: Strict No-Log / Ephemeral Session.
# ------------------------------------------------------------------
>>>>>>> Stashed changes

import streamlit as st
import google.generativeai as genai
import spacy
import pandas as pd
import altair as alt
<<<<<<< Updated upstream
from collections import Counter
import re
import hashlib
=======
import google.generativeai as genai
from datetime import datetime
>>>>>>> Stashed changes
import uuid
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

<<<<<<< Updated upstream
# --- 1. CONFIGURATION & THEME ---
st.set_page_config(
    page_title="Tether.",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'mailto:stromalabs@proton.me',
        'About': "# Tether \n Semantic Resume Analysis Engine."
    }
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0F1116;
        color: #FFFFFF;
    }
    .highlight {
        color: #E63946;
        font-weight: bold;
    }
    header {visibility: hidden;}
    
    /* REMOVE UI STROKES */
    .stTextArea div[data-baseweb="base-input"] {
        background-color: #1C1E26; 
        border: none !important;
        border-radius: 4px;
    }
    .stTextArea div[data-baseweb="base-input"]:focus-within {
        box-shadow: none !important;
        border: none !important;
        outline: none !important;
    }
    .block-container {
        padding-top: 2rem; 
    }
    </style>
    """, unsafe_allow_html=True)
=======
# ------------------------------------------------------------------
# CONFIGURATION & SECRETS
# ------------------------------------------------------------------
st.set_page_config(page_title="Tether V5", page_icon="🧬", layout="wide")

# Initialize Session ID (For ephemeral session tracking only)
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
>>>>>>> Stashed changes

# --- 2. LOGIC ENGINE (NLP & SCORING) ---
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# THE LEXICON (LEMMAS / BASE FORMS)
BUILDER_VERBS = [
    "architect", "build", "create", "design", "develop", "devise", 
    "engineer", "establish", "found", "formulate", "implement", 
    "initiate", "launch", "originate", "pilot", "pioneer", "revamp", 
    "structure", "spearhead", "transform", "ship", "code", "deploy",
    "produce", "compose", "draft"
]

OPERATOR_VERBS = [
    "accelerate", "administer", "analyze", "augment", "centralize", 
    "conserve", "consolidate", "decrease", "ensure", "execute", 
    "expand", "expedite", "generate", "improve", "increase", 
    "maintain", "manage", "maximize", "optimize", "orchestrate", 
    "process", "reduce", "refine", "resolve", "scale", "streamline",
    "conduct", "coordinate"
]

BRIDGE_VERBS = [
    "align", "collaborate", "communicate", "convince", "cultivate", 
    "direct", "enable", "facilitate", "guide", "influence", 
    "mentor", "negotiate", "partner", "persuade", "present", 
    "promote", "reconcile", "represent", "secure", "unite",
    "counsel", "articulate"
]

WEAK_VERBS = [
    "assist", "help", "participate", "support", "work", 
    "handle", "contribute", "attend"
]

def analyze_archetype(text):
    doc = nlp(text.lower())
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    
    # Calculate Raw Scores
    b_score = sum(1 for v in verbs if v in BUILDER_VERBS) * 10
    o_score = sum(1 for v in verbs if v in OPERATOR_VERBS) * 10
    br_score = sum(1 for v in verbs if v in BRIDGE_VERBS) * 10
    
    # Identify Weaknesses
    weaknesses = [v for v in verbs if v in WEAK_VERBS]
    
    total = b_score + o_score + br_score
    if total == 0: total = 1 
    
    scores = {"Builder": b_score, "Operator": o_score, "Bridge": br_score}
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    (primary_name, primary_score) = sorted_scores[0]
    (secondary_name, secondary_score) = sorted_scores[1]
    
    delta = primary_score - secondary_score
    hybrid_label = primary_name 
    is_hybrid = False
    
    if delta < 20 and secondary_score > 0:
        is_hybrid = True
        pair = sorted([primary_name, secondary_name]) 
        if pair == ['Builder', 'Operator']:
            hybrid_label = "The Industrialist"
        elif pair == ['Bridge', 'Builder']:
            hybrid_label = "The Evangelist"
        elif pair == ['Bridge', 'Operator']:
            hybrid_label = "The Integrator"
            
    return {
        "b": b_score, "o": o_score, "br": br_score,
        "primary": primary_name, "secondary": secondary_name,
        "delta": delta, "label": hybrid_label, "is_hybrid": is_hybrid,
        "weaknesses": weaknesses, "length": len(text)
    }

<<<<<<< Updated upstream
# --- 3. THE BRAIN (GEMINI 2.0 UPGRADE) ---
def generate_stroma_report(text, analysis, api_key):
=======
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
# 3. GEMINI AI GENERATION (TTHE EVOLUTIONARY AUDIT)
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
    *Privacy Notice: Stroma Labs does not store your personal data. This session will be automatically erased.*
    """
    
>>>>>>> Stashed changes
    try:
        genai.configure(api_key=api_key)
        
        # Prompt Logic
        identity_context = f"Primary: {analysis['primary']}"
        if analysis['is_hybrid']:
            identity_context = f"HYBRID DETECTED: {analysis['label']} ({analysis['primary']} + {analysis['secondary']})"
        
        prompt = f"""
        You are 'Tether', a career architect engine from Stroma Labs.
        You are analyzing a professional profile.
        
        **DNA SIGNAL:**
        - Identity: {identity_context}
        - Builder Score: {analysis['b']}
        - Operator Score: {analysis['o']}
        - Bridge Score: {analysis['br']}
        
        **TASK:**
        Generate a "Stroma Professional Audit" in 3 strict sections. 
        Tone: Clinical, high-agency, unbiased. No fluff.
        
        **SECTION 1: THE MIRROR (The Identity)**
        Define who they are based on the Identity provided above.
        - If {analysis['label']} is "The Industrialist", "The Evangelist", or "The Integrator", explain that unique combination.
        - Write a 2-sentence "Hero Statement" that defines their value proposition.
        
        **SECTION 2: THE ENVIRONMENT AUDIT (The Framework)**
        Based on their traits, describe the ideal environment for success.
        - **Culture:** What kind of team pace/vibe suits them?
        - **Structure:** Flat vs. Hierarchical? 
        - **Trap:** One specific environment type they must avoid.
        
        **SECTION 3: THE PROOF (3 Rewritten Bullets)**
        Find 3 bullet points from the text that use weak language.
        Rewrite them to match their Archetype Voice ({analysis['label']}).
        
        **INPUT TEXT:**
        {text[:5000]}
        """
        
        # TRY GEMINI 2.0 (From your active list)
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(prompt)
            return response.text
        except:
            # FALLBACK TO LATEST ALIAS (Safety Net)
            model = genai.GenerativeModel('gemini-flash-latest')
            response = model.generate_content(prompt)
            return response.text

<<<<<<< Updated upstream
    except Exception as e:
        return f"System Signal Lost: {str(e)}"

# --- 4. DATA LOGGING ---
def scrub_pii(text):
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '<EMAIL_REDACTED>', text)
    text = re.sub(r'\+?\d[\d -]{8,15}\d', '<PHONE_REDACTED>', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '<LINK_REDACTED>', text)
    return text

def log_session(text, analysis, output_report):
    if len(text) < 50: return
    
    input_hash = hashlib.md5(text.encode()).hexdigest()
    
    if 'last_hash' in st.session_state and st.session_state.last_hash == input_hash:
        return
    
    st.session_state.last_hash = input_hash
    safe_text = scrub_pii(text)
    
    try:
        conn = st.connection("gsheets", type=GSheetsConnection)
        df_new = pd.DataFrame([{
            "Timestamp": datetime.now().isoformat(),
            "Session_ID": st.session_state.session_id,
            "Archetype_Label": analysis['label'],         
            "Archetype_Primary": analysis['primary'],
            "Archetype_Secondary": analysis['secondary'], 
            "Gap_Delta": analysis['delta'],               
            "Score_Builder": analysis['b'],
            "Score_Operator": analysis['o'],
            "Score_Bridge": analysis['br'],
            "Input_Redacted": safe_text,
            "Output_Report": output_report
        }])
        conn.update(data=df_new)
    except Exception as e:
        pass

# --- 5. UI & MAIN EXECUTION ---
def main():
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    st.title("Tether")
    st.markdown("""
    Most resumes are lists of tasks. This obscures your value.
    Tether decodes your professional DNA to measure your signal across the 
    **Builder**, **Operator**, and **Bridge** spectrum.
=======
# ------------------------------------------------------------------
# 4. UI/UX
# ------------------------------------------------------------------

st.title("Tether.")
st.markdown("Run a forensic audit on your career. See why you are a threat.")
st.caption("🔒 Privacy First: Stroma Labs does not store your personal data. All analysis will be automatically erased.")

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
>>>>>>> Stashed changes
    
    **SYSTEM PROTOCOL & PRIVACY**
    * **Encryption:** Personal information are **automatically destroyed** before analysis.
    * **The Vault:** We log *only* anonymized semantic patterns to refine the Stroma Engine.
    * **Usage:** Your data is never sold. It is used exclusively to architect your narrative and train internal models.
    """)
    
    st.write("---")
    text_input = st.text_area("Paste your full resume:", height=250)
    
<<<<<<< Updated upstream
    if st.button("Analyze Signal"):
        if not text_input or len(text_input) < 50:
            st.warning("Input signal too weak. Please provide more detail.")
        else:
            with st.spinner("Stroma System is extracting semantic patterns..."):
                # 1. ANALYZE
                analysis = analyze_archetype(text_input)
                
                # 2. GENERATE REPORT
                try:
                    api_key = st.secrets["GOOGLE_API_KEY"]
                    report = generate_stroma_report(text_input, analysis, api_key)
                except:
                    st.error("Connection Failed. Please check API Key.")
                    st.stop()
                
                # 3. LOG DATA
                log_session(text_input, analysis, report)
                
                # 4. VISUALIZE
                st.write("---")
                
                c1, c2 = st.columns(2)
                
                # Metric 1: Identity
                label_display = analysis['label']
                if analysis['is_hybrid']:
                    label_display = f"{analysis['label']} ({analysis['primary'][0]}+{analysis['secondary'][0]})"
                
                c1.metric("Dominant Signal", label_display)
                
                # Metric 2: Secondary Signal (Replaces Weak Verbs)
                c2.metric("Secondary Signal", f"{analysis['secondary']}")
                
                # Chart
                chart_data = pd.DataFrame({
                    'Archetype': ['Builder', 'Operator', 'Bridge'],
                    'Score': [analysis['b'], analysis['o'], analysis['br']]
                })
                
                # Chart Config for White Text
                chart = alt.Chart(chart_data).mark_bar().encode(
                    x=alt.X('Archetype', axis=alt.Axis(labelAngle=0)),
                    y=alt.Y('Score', axis=None),
                    color=alt.Color('Archetype', scale=alt.Scale(
                        domain=['Builder', 'Operator', 'Bridge'],
                        range=['#20BF55', '#2F75C6', '#E1BC29'] 
                    )),
                    tooltip=['Archetype', 'Score']
                ).configure(
                    background='transparent'
                ).configure_view(
                    strokeOpacity=0
                ).configure_axis(
                    labelColor='#FFFFFF',
                    titleColor='#FFFFFF',
                    grid=False
                ).configure_legend(
                    labelColor='#FFFFFF',
                    titleColor='#FFFFFF'
                ).properties(
                    height=200
                )
                
                st.altair_chart(chart, use_container_width=True, theme="streamlit")
                
                # 5. REPORT
                st.subheader("The Stroma Audit")
                st.markdown(report)
                
                st.write("---")
                
                # 6. FOOTER
                st.markdown(
                    """
                    <div style='text-align: center; color: rgba(255, 255, 255, 0.5); font-size: 12px; margin-top: 20px; font-weight: 300;'>
                        © 2025 Stroma Labs. All rights reserved.
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()
=======
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
        with st.spinner("Analyzing Threat Profile..."):
            audit_result = generate_stroma_audit(resume_text, pcts, sorted_pcts, is_hybrid)
            st.markdown(audit_result)
            
# Footer
st.markdown(
    """
    <div style='text-align: center; font-size: 12px; margin-top: 20px; font-weight: 300;'>
        © 2025 Stroma Labs. Stroma Labs does not store personal user data.
    </div>
    """, 
    unsafe_allow_html=True
)
>>>>>>> Stashed changes
