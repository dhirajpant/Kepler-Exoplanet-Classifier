import streamlit as st

def run_analysis():
    st.title("📊 Analysis & Model Performance")

    # --- Project Findings ---
    st.header("🌌 Project Findings: Exoplanet Discovery Insights")

    st.subheader("1️⃣ Dataset Characteristics")
    st.markdown("""
    - **9,564 observations** with **49 parameters** from the Kepler mission.  
    - Contains both **planetary parameters** (radius, orbital period, insolation) and **stellar parameters** (temperature, gravity).  
    - Outcome categories:  
      - **Candidate** → likely exoplanets  
      - **False Positive** → signals that mimic planets but aren’t real  
    - Near-equal class balance → supports **unbiased AI classification**.
    """)

    st.subheader("2️⃣ Feature Relationships")
    st.markdown("""
    - Many error terms (e.g., `koi_prad_err2`, `koi_insol_err2`) are **>0.9 correlated** with parent variables.  
      ➤ Redundant, should be reduced via **feature selection/PCA**.  
    - Strong links between **planet radius, stellar radius, insolation**, aligning with astrophysical theory.  
    - Moderate correlations for derived features (`koi_teq`, `koi_score`) → they integrate multiple factors.  

    **Interpretation:**  
    The dataset reflects **true astrophysical dependencies** but also contains **collinear features**.
    """)
    
    st.image("Images/planet vs radius.png", width=700)
    
    st.image("Images/distribution.png", width=700)
    st.markdown("""
    The distribution plots illustrate the Disposition Count in the dataset.""")

    st.subheader("3️⃣ Feature Distribution Patterns")
    st.markdown("""
    - Most features are **heavily skewed**, with clustered values and rare outliers.  
    - A few (e.g., `kepid`, `koi_period`) show wider distributions.  
    - Many measurements are **low-variance signals**, consistent with Kepler’s detection process.  

    **Modeling Insight:**  
    Requires **scaling or log transformation** to handle uneven feature ranges.
    """)
  
    st.subheader("4️⃣ Key Predictors")
    st.markdown("""
    - **`koi_score`** → strongest predictor; separates *Candidate* vs. *False Positive*.  
    - **False-positive flags (`koi_fpflag_*`)** → negatively correlated with true exoplanets.  
    - Orbital properties (`koi_period`, `koi_time0bk`) show **weak separation power**.  

    **Interpretation:**  
    Detection confidence and **quality flags matter more than orbital mechanics** for classification.
    """)

    st.subheader("5️⃣ Dimensionality Insights (PCA)")
    st.markdown("""
    - First 2 PCA components explain only **~22% variance**.  
    - Data is **high-dimensional and non-linear** → no dominant feature.  

    **Implication:**  
    Advanced models (e.g., **Random Forest, XGBoost, Deep Learning**) are better suited than linear methods.
    """)

    st.subheader("6️⃣ Scientific & Analytical Conclusions")
    st.markdown("""
    1. Dataset is balanced and suitable for ML.  
    2. **`koi_score` + flag features** are top predictors.  
    3. Several error features are redundant → prune or reduce.  
    4. PCA confirms **complex, multi-dimensional structure**.  
    5. Correlations align with **astrophysical laws** → validates dataset authenticity.  
    6. Non-linear models are most effective for classification.  
    """)


    # --- Final Interpretation ---
    st.markdown("""
    ---
    ### 🌠 Overall Interpretation
    AI can effectively **distinguish real exoplanets from false signals** by learning both astrophysical patterns and detection-related features.  
    While planetary physics provides context, **data quality and confidence metrics** ultimately drive classification performance.  

    ➤ This underscores the potential of **AI-driven astronomy** in accelerating exoplanet discovery 🚀
    """)
    
       # --- Distribution Plot ---
    st.header("📈 Feature Distributions")
    st.image("Images/distribution.jpeg", width=700, caption="Distribution of Exoplanet Classes")

    st.markdown("""
    The distribution plots illustrate how numeric features vary across the dataset.

    **🔎 Key Observations**
    - **Skewed Features:** Many variables (e.g., `koi_fpflag_nt`, `koi_period_err1`, `koi_period_err2`) are **right-skewed** — most values near zero with a few large outliers.  
      ➤ Indicates small errors for most candidates, but rare extreme cases.  
    - **Binary-like Indicators:** Flags such as `koi_fpflag_ss`, `koi_fpflag_co`, `koi_fpflag_nt` behave like categorical features, representing detection/validation states.  
      ➤ Should be handled as categorical during preprocessing.  
    - **Identifiers:** Columns like `kepid` show uniform-like distributions → not useful for prediction.  
      ➤ Must be **dropped** before training.  
    - **Error Columns:** Features ending in `_err1` or `_err2` have very narrow ranges → good proxies for measurement precision.  
    - **Values Near Zero:** Features like `koi_impact`, `koi_time0bk` cluster near 0, requiring **scaling/normalization**.  

    **💡 Modeling Insight:**  
    Many features are imbalanced or concentrated, so **log-scaling, normalization, or transformation** will be essential. Binary-like flags should be preserved as categorical predictors.
    """)

    # --- Correlation Heatmap ---
    st.header("📊 Feature Correlation Analysis")
    st.image("Images/heatmap.jpeg", width=700, caption="Correlation Heatmap of Features")

    st.markdown("""
    The correlation heatmap shows how features relate to each other.

    **🔎 Key Observations**
    - Groups like `koi_period`, `koi_period_err1`, `koi_period_err2` are **highly correlated**, as they describe similar orbital properties.  
    - Error features (`*_err1`, `*_err2`) are strongly correlated with their parent columns → **redundant information**.  
    - Most features show **low to moderate correlation**, meaning the dataset is diverse and informative.  
    - Some **negative correlations** exist (e.g., surface gravity vs. radius, luminosity vs. temperature).  

    **✅ Conclusion:**  
    Redundant error features should be pruned, but the overall diversity of independent variables supports **robust ML models** without severe multicollinearity.
    """)

