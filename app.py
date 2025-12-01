# app.py

import streamlit as st
import numpy as np
import joblib

# -------------------------
# Load model and metadata
# -------------------------
@st.cache_resource
def load_model():
    model = joblib.load("disease_model.pkl")
    feature_cols = joblib.load("feature_columns.pkl")
    return model, feature_cols

model, feature_cols = load_model()

# -------------------------
# Simple rule-based recommendations
# -------------------------
def get_recommendations(diagnosis):
    diagnosis = str(diagnosis)

    recommendations = {
        "Diabetes": {
            "medicines": [
                "Metformin (as prescribed by doctor)",
                "Insulin therapy (if advised by doctor)"
            ],
            "diet": [
                "Avoid sugary drinks and sweets",
                "Eat more whole grains, vegetables, and high-fiber foods",
                "Control portion sizes, avoid overeating"
            ],
            "lifestyle": [
                "Walk at least 30 minutes daily",
                "Regular checkup for blood sugar levels",
                "Maintain healthy body weight"
            ]
        },
        "Hypertension": {
            "medicines": [
                "ACE inhibitors / ARBs (doctor prescribed)",
                "Beta-blockers or calcium channel blockers (if prescribed)"
            ],
            "diet": [
                "Low-salt (low-sodium) diet",
                "Avoid junk food and deep-fried items",
                "Increase intake of fruits and green leafy vegetables"
            ],
            "lifestyle": [
                "Regular blood pressure monitoring",
                "Reduce stress, practice yoga/meditation",
                "Avoid smoking and alcohol"
            ]
        },
        "Heart Disease": {
            "medicines": [
                "Antiplatelet drugs (like aspirin if prescribed)",
                "Statins to control cholesterol (doctor prescribed)"
            ],
            "diet": [
                "Low-fat, heart-healthy diet",
                "Avoid red meat and trans fats",
                "Eat more omega-3 rich foods (fish, flaxseeds)"
            ],
            "lifestyle": [
                "Regular moderate exercise (as per cardiologist guidance)",
                "Avoid smoking completely",
                "Manage stress properly"
            ]
        },
        "Flu": {
            "medicines": [
                "Paracetamol for fever (as per dosage)",
                "Cough syrup (if prescribed)",
                "Plenty of fluids and rest"
            ],
            "diet": [
                "Warm fluids like soup and herbal tea",
                "Avoid cold drinks and junk food",
                "Eat light, easy-to-digest food"
            ],
            "lifestyle": [
                "Take proper rest and sleep",
                "Avoid going out to prevent spreading infection",
                "Maintain hygiene and use mask if coughing"
            ]
        },
        "Normal": {
            "medicines": [
                "No specific medicine required"
            ],
            "diet": [
                "Maintain a balanced diet with fruits and vegetables",
                "Avoid excessive sugar, salt, and fast food"
            ],
            "lifestyle": [
                "Regular exercise (30 mins/day)",
                "Regular yearly health checkup",
                "Stay hydrated and sleep 7–8 hours"
            ]
        }
    }

    # Default if diagnosis not in dict
    return recommendations.get(diagnosis, {
        "medicines": ["Consult a registered medical practitioner."],
        "diet": ["Follow a simple, balanced home-cooked diet."],
        "lifestyle": ["Maintain regular exercise and sleep schedule."]
    })


# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(
    page_title="Healthcare Recommendation System",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ Healthcare Recommendation System")
st.write(
    "This application predicts a possible health condition based on "
    "your inputs and provides basic medicine, diet, and lifestyle recommendations.\n\n"
    "**Note:** This project is for educational purposes only and not a substitute for professional medical advice."
)

st.subheader("1. Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=10, max_value=90, value=30)
    blood_pressure = st.slider("Blood Pressure (Systolic mmHg)", 90, 200, 120)
    glucose_level = st.slider("Glucose Level (mg/dL)", 70, 250, 100)

with col2:
    heart_rate = st.slider("Heart Rate (beats per minute)", 50, 140, 80)
    bmi = st.slider("BMI (Body Mass Index)", 15.0, 40.0, 24.0)

st.subheader("2. Select Symptoms")

symptom_fever = st.checkbox("Fever")
symptom_cough = st.checkbox("Cough")
symptom_fatigue = st.checkbox("Fatigue / Tiredness")
symptom_pain = st.checkbox("Pain (Chest / Body Pain)")

# Convert boolean to 0/1
symptom_fever_val = 1 if symptom_fever else 0
symptom_cough_val = 1 if symptom_cough else 0
symptom_fatigue_val = 1 if symptom_fatigue else 0
symptom_pain_val = 1 if symptom_pain else 0

st.subheader("3. Predict Disease & Get Recommendations")

if st.button("🔍 Predict"):
    # Create input vector in the same order as feature_cols
    input_data = np.array([[
        age,
        blood_pressure,
        glucose_level,
        heart_rate,
        bmi,
        symptom_fever_val,
        symptom_cough_val,
        symptom_fatigue_val,
        symptom_pain_val
    ]])

    # Prediction
    prediction = model.predict(input_data)[0]

    st.success(f"🩺 Predicted Condition: **{prediction}**")

    # Recommendations
    rec = get_recommendations(prediction)

    st.markdown("### 💊 Medicine Suggestions")
    for med in rec["medicines"]:
        st.write(f"- {med}")

    st.markdown("### 🥗 Diet Recommendations")
    for d in rec["diet"]:
        st.write(f"- {d}")

    st.markdown("### 🌱 Lifestyle Suggestions")
    for life in rec["lifestyle"]:
        st.write(f"- {life}")

    st.info(
        "⚠️ Disclaimer: This is a student project and should not be used for real medical decisions. "
        "Always consult a certified doctor for diagnosis and treatment."
    )
