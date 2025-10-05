import streamlit as st
import pandas as pd
import joblib

def run_predict():
    
    # -------------------------------
    # Load trained model & preprocessing objects
    # -------------------------------
    @st.cache_resource
    def load_model():
        model = joblib.load("Models/rf_model_top10.pkl")
        scaler = joblib.load("Models/scaler_top10.pkl")
        label_encoder = joblib.load("Models/label_encoder_top10.pkl")
        top_features = joblib.load("Models/top_features.pkl")
        return model, scaler, label_encoder, top_features

    model, scaler, label_encoder, top_features = load_model()

    # -------------------------------
    # Streamlit Page
    # -------------------------------
    st.title("🔮 Exoplanet Prediction App")
    st.write("Provide exoplanet parameters to predict whether it is **Confirmed**, **Candidate**, or **False Positive**.")

    st.markdown("""We have used top 10 features based on feature importance from Random Forest model for the prediction.""")

    # -------------------------------
    # User Input Section (Main Page)
    # -------------------------------
    st.header("Enter Exoplanet Parameters")
    
    user_input = {}
    for feature in top_features:
        # You can customize default values for better UX
        default_val = 0.0
        if "koi_period" in feature:
            default_val = 10.0
        elif "koi_duration" in feature:
            default_val = 5.0
        elif "koi_depth" in feature:
            default_val = 500.0
        elif "koi_prad" in feature:
            default_val = 1.0
        elif "koi_teq" in feature:
            default_val = 500.0
        elif "koi_insol" in feature:
            default_val = 1.0
        elif "koi_steff" in feature:
            default_val = 5500.0
        elif "koi_slogg" in feature:
            default_val = 4.5
        elif "koi_srad" in feature:
            default_val = 1.0
        elif "koi_kepmag" in feature:
            default_val = 14.0

        user_input[feature] = st.number_input(f"{feature}", value=float(default_val), min_value=0.0)

    input_df = pd.DataFrame([user_input])

    # -------------------------------
    # Scale input
    # -------------------------------
    input_scaled = scaler.transform(input_df)

    # -------------------------------
    # Prediction
    # -------------------------------
    if st.button("Predict"):
        prediction = model.predict(input_scaled)
        pred_class = label_encoder.inverse_transform(prediction)[0]

        st.subheader("✅ Prediction Result:")
        st.success(f"The object is classified as: **{pred_class}**")
