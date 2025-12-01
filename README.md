# ⚕️ Healthcare Recommendation System using Machine Learning

This project predicts possible diseases based on patient symptoms and health parameters, and provides personalized **medicine, diet, and lifestyle recommendations**.  
It is built using **Machine Learning + Streamlit** and deployed as a live web app.

🔗 **Live Demo:**  
👉 https://YOUR-STREAMLIT-APP-LINK

---

## 🚀 Features
✔ Predicts health condition using ML (Random Forest)  
✔ Inputs: age, BP, glucose level, heart rate, BMI, symptoms  
✔ Healthcare recommendation system  
✔ Streamlit interactive UI  
✔ Lightweight — works on low RAM machines  
✔ Open-source project (educational purpose)

---

## 🧠 Tech Stack
| Component | Technology |
|----------|------------|
| Front-end UI | Streamlit |
| Back-end | Python |
| ML Model | Random Forest Classifier |
| Database | CSV dataset |
| Deployment | Streamlit Cloud |

---

## 📂 Project Folder Structure
healthcare_recommendation_system
│
├── app.py
├── train_model.py
├── medical_data.csv
├── disease_model.pkl
├── feature_columns.pkl
├── requirements.txt
└── README.md

---

## ⚙️ Run Locally
```bash
git clone https://github.com/tangallapalliakshayvarma-ai/healthcare_recommendation_system.git
cd healthcare_recommendation_system
pip install -r requirements.txt
python train_model.py
streamlit run app.py

📊 Machine Learning Workflow

1️⃣ Data collection
2️⃣ Data preprocessing
3️⃣ Train–test split
4️⃣ Model training using Random Forest
5️⃣ Model saving using joblib
6️⃣ Serving predictions to UI (Streamlit)

🧪 Sample Input Parameters

Age
Blood Pressure
Glucose Level
Heart Rate
BMI
Symptoms → fever, cough, fatigue, pain

🩺 Output

Predicted disease
Recommended medicine
Diet recommendations
Lifestyle changes
⚠️ This system is for educational use only and not a medical diagnostic tool.

🌱 Future Enhancements

🔹 Add chatbot for medical guidance
🔹 Add Login + Admin dashboard
🔹 Deep learning + LSTM model for improved accuracy
🔹 PDF medical report generation
👨‍💻 Author

Tangallapalli Akshay Varma
📧 Email: tangallapalliakshayvarma@gmail.com
⭐ If you like this project, consider giving the repo a star!

## 🔗 Live Application
https://healthcarerecommendationsystem-3qtlbrzegqb4k6p2teqxpt.streamlit.app/
