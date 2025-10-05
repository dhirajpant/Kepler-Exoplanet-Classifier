import streamlit as st

st.set_page_config(page_title="Conclusion", layout="wide")
st.title("✅ Conclusion & Insights")

def show_conclusion():
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
    """)


    # Optional: add a closing note
    st.markdown("""
    ---
    Thank you for exploring the **Exoplanet Prediction App**.  
    Feel free to experiment with different parameters in the **Prediction** page!
    """)

