# 🏦 CreditIQ — Loan Risk Classifier

> **ML-powered loan risk classification system** that predicts credit risk grades for loan applicants using machine learning.

🔗 **Live Demo:** [https://wrist-hunting-pavestone.ngrok-free.dev/](https://wrist-hunting-pavestone.ngrok-free.dev/)

---

## 📌 Overview

CreditIQ is a Streamlit-based web application that takes applicant financial and demographic details as input and predicts their credit risk grade — from **P1 (Very Low Risk)** to **P4 (High Risk)** — helping lenders make faster, data-driven loan decisions.

---

## 🚀 Features

- Predicts credit risk grade in real time
- Simple, intuitive dark-themed UI
- Supports 8 input features covering demographics and credit behavior
- Outputs a risk grade with a plain-English explanation
- Built with a trained ML model (Random Forest / sklearn pipeline)

---

## 🖥️ Application Screenshot

![CreditIQ App Screenshot](https://wrist-hunting-pavestone.ngrok-free.dev/)

> The app accepts applicant details and returns a credit risk grade (P1–P4) with an explanation.

---

## 🧠 Input Features

| Feature | Description |
|---|---|
| Age of Oldest Trade Line (months) | How long the applicant has had credit |
| Gender | M / F |
| Marital Status | Married / Single / Others |
| Education Level | SSC, 12TH, Graduate, Post-Graduate, etc. |
| Last Product Enquiry | Type of last loan product enquired (AL, CC, HL, PL, etc.) |
| First Product Enquiry | Type of first loan product enquired |
| Number of Enquiries (Last 6 months) | Recent credit enquiry count |
| Number of Active Loans | Count of currently active loans |

---

## 🎯 Risk Grades

| Grade | Label | Meaning |
|---|---|---|
| **P1** | ✅ Very Low Risk | Highly creditworthy. Very low probability of default. |
| **P2** | 🟡 Low Risk | Creditworthy with low risk. Loan likely to be approved. |
| **P3** | 🟠 Medium Risk | Moderate risk. Manual review recommended. |
| **P4** | 🔴 High Risk | High risk. Loan approval not recommended. |

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Streamlit** — Web application framework
- **scikit-learn** — ML model training & inference
- **pandas / numpy** — Data preprocessing
- **joblib** — Model serialization
- **Jupyter Notebook** — Data exploration and model development

---

## 📂 Project Structure

```
-CREDIT-IQ-risk-classifier/
│
├── app.py                   # Streamlit application
├── CREDIT ANALYZER.ipynb    # Jupyter notebook for EDA & model training
├── Loan_Approval_Model.pkl  # Trained ML model
├── model_columns.pkl        # Feature columns used by the model
├── CS_1.1 (1).xlsx          # Dataset 1
├── CS_2.1 (1).xlsx          # Dataset 2
├── confusion_matrix.png     # Model evaluation - confusion matrix
├── feature_importance.png   # Feature importance chart
└── requirements.txt         # Python dependencies
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/shashikiram/-CREDIT-IQ-risk-classifier.git
cd -CREDIT-IQ-risk-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 🌐 Live Application

The app is currently deployed and accessible at:

**[https://wrist-hunting-pavestone.ngrok-free.dev/](https://wrist-hunting-pavestone.ngrok-free.dev/)**

> ⚠️ Note: This is served via ngrok, so the URL may change periodically. Check this README or the repository for the latest link.

---

## 👨‍💻 Author

**Nagapuri Shashi Kiran**
NIT Warangal

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
