import streamlit as st

# Page configuration
st.set_page_config(page_title="Kepler Exoplanet Classifier", layout="wide")

# Sidebar navigation
st.sidebar.title("🔭 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "Predict", "Analysis", "Conclusion"]
)

# ---------- HOME PAGE ----------
if page == "Home":
    st.title("🚀 Kepler Exoplanet Classifier")
    st.markdown("""
    Welcome to the **Kepler Exoplanet Classifier**!  
    This project demonstrates how **Artificial Intelligence and Machine Learning** can be applied to automatically classify exoplanets using NASA's open-source Kepler dataset.
    """)
    st.image("Images/exoplanets-1.jpg",width=600)
    # Section: Background
    st.header("🌌 Background")
    st.markdown("""
    Exoplanets are planets that orbit stars outside our solar system.  
    Identifying exoplanets is crucial for understanding the universe and potentially finding habitable worlds.  

    NASA's **Kepler mission** used the **transit method**, which detects tiny dips in a star's brightness caused by a planet passing in front of it.  
    While Kepler has discovered thousands of exoplanets, most of the data analysis was done manually by scientists, which is time-consuming.  

    With advances in **machine learning**, it’s possible to **automate this process**, analyze large datasets efficiently, and discover new exoplanets hidden in the data.
    """)

    # Section: Project Objective
    st.header("🎯 Project Objective")
    st.markdown("""
    The goal of this project is to create an **AI/ML model** that can:
    - Classify exoplanets as **Confirmed**, **Candidate**, or **False Positive**
    - Analyze new Kepler data automatically
    - Provide a **user-friendly web interface** for researchers and enthusiasts
    """)

    # Section: Dataset
    st.header("📊 Dataset Overview")
    st.markdown("""
    We used **NASA open-source exoplanet datasets**:

    1. **Kepler Objects of Interest (KOI):**  
       A comprehensive list of all confirmed exoplanets, planetary candidates, and false positives determined from Kepler transits.  
       - Target column for classification: `koi_disposition` ("Disposition Using Kepler Data").

    2. **TESS Objects of Interest (TOI):**  
       Lists all confirmed exoplanets, planetary candidates, false positives, ambiguous planetary candidates, and known planets from TESS.  
       - Target column for classification: `TFOWPG Disposition`.

    3. **K2 Planets and Candidates:**  
       Lists all confirmed exoplanets, planetary candidates, and false positives from the K2 mission.  
       - Target column for classification: `Archive Disposition`.
    """)

    # Section: Machine Learning Approach
    st.header("🤖 Machine Learning Approach")
    st.markdown("""
    We built a **Random Forest Classifier** to predict exoplanet classification.  

    **Key steps:**
    1. **Data Cleaning:** Handle missing values, remove irrelevant columns.
    2. **Feature Engineering:** Encode categorical columns, scale numerical features.
    3. **Model Training:** Train a Random Forest model on the cleaned dataset.
    4. **Evaluation:** Assess accuracy, precision, recall, and confusion matrix.
    5. **Deployment:** Save the model and use it in a web interface for predictions.
    """)

    # Section: Resources
    st.header("📚 Resources & References")
    st.markdown("""
    We relied on the following resources to guide our project:

    - **[NASA Kepler Objects of Interest (KOI)](https://exoplanetarchive.ipac.caltech.edu/)**
    - **[TESS Objects of Interest (TOI)](https://tess.mit.edu/)**
    - **[K2 Planets and Candidates](https://archive.stsci.edu/k2/)**
    - *Exoplanet Detection Using Machine Learning* — Survey of ML approaches for exoplanet identification (2021)
    - *Assessment of Ensemble-Based Machine Learning Algorithms for Exoplanet Identification* — Research on preprocessing and ensemble methods for high accuracy
    """)

    # Section: Significance
    st.header("✨ Significance")
    st.markdown("""
    - Automates the **labor-intensive exoplanet classification process**
    - Helps astronomers **quickly identify promising candidates**
    - Encourages **public engagement** in space exploration
    - Provides a foundation for future **AI-driven astronomical discoveries**
    """)

    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ by **3Ds**")


# ---------- PREDICT PAGE ----------
elif page == "Predict":
    import Predict
    Predict.run_predict()


# ---------- ANALYSIS PAGE ----------
elif page == "Analysis":
    import Analysis
    Analysis.run_analysis()


# ---------- CONCLUSION PAGE ----------
elif page == "Conclusion":
    import Conclusion
    Conclusion.show_conclusion()
