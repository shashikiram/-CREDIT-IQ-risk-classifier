
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and column names
model = joblib.load('Loan_Approval_Model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.set_page_config(page_title="CreditIQ", page_icon="🏦", layout="centered")

st.title("🏦 CreditIQ — Loan Risk Classifier")
st.write("Enter applicant details below to predict credit risk grade.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    age_oldest_tl = st.number_input("Age of Oldest Trade Line (months)", min_value=0, max_value=600, value=120)
    gender = st.selectbox("Gender", ["M", "F"])
    marital = st.selectbox("Marital Status", ["Married", "Single", "Others"])
    education = st.selectbox("Education Level", 
                    ["SSC", "12TH", "GRADUATE", "UNDER GRADUATE", 
                     "POST-GRADUATE", "PROFESSIONAL", "OTHERS"])

with col2:
    last_prod = st.selectbox("Last Product Enquiry", 
                    ["AL", "CC", "ConsumerLoan", "HL", "PL", "others"])
    first_prod = st.selectbox("First Product Enquiry", 
                    ["AL", "CC", "ConsumerLoan", "HL", "PL", "others"])
    num_enquiries = st.number_input("Number of Enquiries (Last 6 months)", min_value=0, max_value=50, value=1)
    active_loans = st.number_input("Number of Active Loans", min_value=0, max_value=30, value=2)

st.markdown("---")

edu_map = {
    "SSC": 1, "12TH": 2, "GRADUATE": 3,
    "UNDER GRADUATE": 3, "POST-GRADUATE": 4,
    "PROFESSIONAL": 3, "OTHERS": 1
}

if st.button("🔍 Predict Risk Grade", use_container_width=True):
    
    input_dict = {
        "Age_Oldest_TL": age_oldest_tl,
        "EDUCATION": edu_map[education],
        "GENDER": gender,
        "MARITALSTATUS": marital,
        "last_prod_enq2": last_prod,
        "first_prod_enq2": first_prod,
        "num_enquiries": num_enquiries,
        "active_loans": active_loans
    }
    
    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
    
    prediction = model.predict(input_encoded)[0]
    
    grade_map = {
        0: ("P1 — Very Low Risk", "✅", "green"),
        1: ("P2 — Low Risk", "🟡", "orange"),
        2: ("P3 — Medium Risk", "🟠", "red"),
        3: ("P4 — High Risk", "🔴", "darkred")
    }
    
    label, icon, color = grade_map[prediction]
    
    st.markdown(f"""
    <div style='background-color:#1e1e2e;padding:20px;border-radius:10px;text-align:center'>
        <h2 style='color:{color}'>{icon} Predicted Grade: {label}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### What this means:")
    explanations = {
        0: "This applicant is highly creditworthy. Very low probability of default.",
        1: "This applicant is creditworthy with low risk. Loan likely to be approved.",
        2: "This applicant carries moderate risk. Manual review recommended.",
        3: "This applicant carries high risk. Loan approval not recommended."
    }
    st.info(explanations[prediction])

st.markdown("---")
st.caption("CreditIQ | Built by Nagapuri Shashi Kiran | NIT Warangal")
