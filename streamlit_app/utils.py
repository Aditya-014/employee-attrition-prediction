import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loading saved files
model = joblib.load(os.path.join(BASE_DIR, "models", "employee_attrition_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))
feature_names = joblib.load(os.path.join(BASE_DIR, "models", "feature_names.pkl"))

def predict_attrition(input_data):
    """
    Predict employee attrition using the trained Logistic Regression model.
    """

    # Converting input dictionary into DataFrame
    input_df = pd.DataFrame([input_data])

    # Applying One-Hot Encoding
    input_df = pd.get_dummies(input_df)

    # Ensuring all training columns are present
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    # Scaling the input
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0]

    print("Prediction :", prediction)
    print("Probability:", probability)

    return prediction, probability
