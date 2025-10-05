import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")
st.title("✅ Conclusion & Insights")

st.markdown("""
### Key Takeaways
- A **Random Forest Classifier** can accurately classify exoplanets from Kepler data.
- Important features for prediction include **orbital period, transit depth, planetary radius, and stellar properties**.
- Automated classification can significantly reduce manual work for astronomers.

### Future Work
- Incorporate **TESS and K2 datasets** for a more comprehensive model.
- Allow **real-time model retraining** with user-uploaded data.
- Build a **more interactive dashboard** with filtering, charts, and explanations.

### Summary
This project demonstrates the power of AI/ML in **astronomical discoveries** and provides a **user-friendly interface** for exoplanet classification.
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Exoplanet_Illustration.png/640px-Exoplanet_Illustration.png", use_column_width=True)
