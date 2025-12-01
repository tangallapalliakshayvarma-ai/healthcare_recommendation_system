import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def main():
    # 1. Load dataset
    df = pd.read_csv("medical_data.csv")

    # 2. Feature and target columns
    feature_cols = [
        "age",
        "blood_pressure",
        "glucose_level",
        "heart_rate",
        "bmi",
        "symptom_fever",
        "symptom_cough",
        "symptom_fatigue",
        "symptom_pain",
    ]
    target_col = "diagnosis"

    X = df[feature_cols]
    y = df[target_col]

    # 3. Train-test split (30% test because dataset is small)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 4. Train Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # 5. Evaluate model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # 6. Save model and feature list
    joblib.dump(model, "disease_model.pkl")
    joblib.dump(feature_cols, "feature_columns.pkl")
    print("\nModel and feature list saved successfully.")

if __name__ == "__main__":
    main()
