# Gurgaon Real Estate Intelligence

An end-to-end machine learning platform for real estate price prediction, market analytics, and apartment recommendations in Gurgaon. Deployed on AWS EC2 as a live Streamlit web application.

🔗 **Live Demo:** [http://15.206.212.117:8501](http://15.206.212.117:8501)

---

## What It Does

| Feature | Description |
|---|---|
| **Price Predictor** | Estimate property prices based on location, size, amenities, and property age using a tuned Random Forest model |
| **Market Analytics** | Interactive geomap visualization showing price-per-sqft trends across Gurgaon sectors |
| **Apartment Recommender** | Find apartments within a chosen radius of any location |

---

## The ML Pipeline

**Dataset:** Real estate listings from 99acres.com for Gurgaon

**End-to-end pipeline built in Jupyter notebooks:**

1. **Exploratory Data Analysis** — Extensive EDA on every feature: distributions, correlations, sector-wise trends
2. **Data Preprocessing** — Missing value imputation, categorical encoding, text parsing
3. **Feature Engineering** — Created new features from raw data to improve predictive power
4. **Outlier Treatment** — Statistical methods to handle price and area anomalies
5. **Feature Selection** — Identified most predictive features to reduce noise
6. **Model Selection** — Baseline SVR → Random Forest with hyperparameter tuning
7. **Model Serialization** — Saved trained pipeline as `.pkl` for inference

**Final Model:** Random Forest Regressor
- **R² Score:** 0.90 (90% variance explained)
- **Best Hyperparameters:** `max_depth=20`, `max_features=sqrt`, `n_estimators=300`

---

## Tech Stack

| Layer | Tools |
|---|---|
| ML & Data Science | Python, Scikit-learn, Pandas, NumPy |
| Visualization | Plotly, Folium, Matplotlib, Seaborn |
| App Framework | Streamlit |
| Deployment | AWS EC2, WinSCP |
| Artifacts | Pickle (pipeline & dataset) |

---

## Project Structure
```
real_estate/
├── Home.py                           # Streamlit entry point
├── pages/
│   ├── 1_price_predictor.py        # Price prediction interface
│   ├── 2_analysis_app.py           # Geomap & market analytics
│   └── 3_recommend_apartments.py   # Location-based recommender
├── notebooks/                        # EDA, preprocessing, model training
├── src/                              # Helper modules
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

> **Note:** The trained model pipeline (`pipeline.pkl`) and processed dataset are stored locally and excluded from Git via `.gitignore` due to file size. They are deployed alongside the application on AWS EC2.

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/areebarao108/real_estate.git
cd real_estate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run Home.py
