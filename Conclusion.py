import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")
st.title("✅ Conclusion & Insights")

def show_conclusion():
    # Fix typo in the image file extension
    st.image("Images/confusion matrix.png", width=600)

    st.markdown("""
This confusion matrix shows the performance of the Random Forest model in classifying three categories: **CANDIDATE, CONFIRMED, and FALSE POSITIVE**.

**CANDIDATE (Row 1):**
- Correctly predicted 318 as CANDIDATE.
- 72 misclassified as CONFIRMED.
- 6 misclassified as FALSE POSITIVE.

**CONFIRMED (Row 2):**
- Correctly predicted 481 as CONFIRMED.
- 67 misclassified as CANDIDATE.
- 1 misclassified as FALSE POSITIVE.

**FALSE POSITIVE (Row 3):**
- Correctly predicted 940 as FALSE POSITIVE.
- Only 28 misclassifications in total (24 → CANDIDATE, 4 → CONFIRMED).

**Interpretation:**
The model performs very well, especially for the FALSE POSITIVE class, where almost all predictions are correct. Misclassifications are mostly between CANDIDATE and CONFIRMED, suggesting that these two classes are harder to distinguish compared to FALSE POSITIVE.

---

### 2. Top 15 Important Features – Random Forest

This bar chart shows the feature importance scores calculated by the Random Forest model. The importance reflects how much each feature contributes to the model’s predictive power.

- The most influential feature is `koi_pdisposition_FALSE POSITIVE`, indicating that prior disposition labels strongly affect predictions.
- `koi_score` and `koi_model_snr` are also highly important, meaning that the statistical score and signal-to-noise ratio play a major role in classification.
- Other significant features include `koi_fpflag_ss`, `koi_time0bk_err2`, `koi_fpflag_co`, and `koi_prad`, which relate to planetary parameters, error estimates, and false-positive flags.
- The importance gradually decreases for features like duration errors, depth, period errors, and stellar effective temperature errors.

**Interpretation:**
The Random Forest model relies heavily on both previous disposition flags and quantitative astrophysical measurements (like score, radius, depth, and duration errors). This confirms that a mix of domain-specific physical parameters and metadata strongly drives prediction accuracy.
""")

    st.markdown("""
### 🔑 Key Takeaways
- A **Random Forest Classifier** can effectively classify exoplanets from Kepler data.
- Most important features for prediction include **orbital period, transit depth, planetary radius, and stellar properties**.
- Automated classification can save **astronomers significant manual effort**.

### 🚀 Future Work
- Integrate **TESS and K2 datasets** to expand model coverage.
- Enable **real-time retraining** with user-uploaded datasets.
- Develop a **fully interactive dashboard** with filtering, visualization, and model explanations.

### 📊 Summary
This project demonstrates the power of **AI/ML in astronomy**, providing a **user-friendly interface** for exoplanet classification.

---

Thank you for exploring the **Exoplanet Prediction App**.  
Feel free to experiment with different parameters in the **Prediction** page!
""")