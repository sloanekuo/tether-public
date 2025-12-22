# Tether.

**Semantic Resume Analysis Engine**

Most resumes are lists of tasks. This obscures value. Tether decodes professional DNA to reveal the user's **Impact Archetype**:
* **Builder:** 0-to-1 Creation & Architecture.
* **Operator:** Scale, Optimization & Efficiency.
* **Bridge:** Alignment, Strategy & Translation.

---

### **New in v4.0: The Hybrid System (Logic V3)**
Tether V4 upgrades from a binary classifier to a **Spectrum Analyzer**. It detects nuanced signal gaps to identify complex, hybrid profiles:
* **The Industrialist (Builder + Operator):** The person who scales what they build.
* **The Evangelist (Builder + Bridge):** The person who creates the vision and sells it.
* **The Integrator (Operator + Bridge):** The person who aligns the people to the machine.

---

### **Features**
* **Context-Aware Narrative:** Generates a "Hero Statement" and "Environment Audit" based on the specific archetype mix.
* **The Vault (Google Sheets):** Anonymized semantic data is logged to a secure database for future model training.
* **Privacy First:** Automated PII Redaction scrubs emails and phone numbers before analysis.
* **Dark Editorial UI:** A custom-injected visual theme for high-focus reading.

---

### **Tech Stack**
* **Core:** Python 3.11, Streamlit
* **AI Model:** Google Gemini 1.5 Flash
* **NLP:** Spacy (`en_core_web_sm`)
* **Visualization:** Altair
* **Database:** Google Sheets API (via `st-gsheets-connection`)

---

### **Local Setup**

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/tether.git](https://github.com/YOUR_USERNAME/tether.git)
   cd tether
   
2. **Install Dependencies**   
   ```bash
   pip install -r requirements.txt
   
3. **Configure Secrets Create a file at .streamlit/secrets.toml with your credentials:**   
   ```Ini, TOML
   GOOGLE_API_KEY = "YOUR_GEMINI_KEY"
   
   [connections.gsheets]
   spreadsheet = "YOUR_GOOGLE_SHEET_URL"
   type = "service_account"
   project_id = "..."
   # ... (Add full JSON credentials from Google Cloud)
   
4. **Run the Engine**
   ```bash
   streamlit run app.py

---

### **License**
© 2025 Stroma Labs.
All rights reserved.