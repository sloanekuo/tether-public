# STEP 1: ACTIVATE
# Windows:
.\venv\Scripts\activate
# Mac:
source venv/bin/activate

# STEP 2: INSTALL/UPDATE
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# STEP 3: RUN
streamlit run app.py