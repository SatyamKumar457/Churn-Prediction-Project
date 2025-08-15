#  Churn Prediction Project

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-yellow)]
[![Streamlit App](https://img.shields.io/badge/App-Status-Interactive-green)]

---

##  Project Overview

Welcome to the **Churn Prediction Project**! 🚀 This is a full-stack **machine learning pipeline** aimed at predicting customer churn. Here's what makes it shine:

-  **Data Exploration & Visualization**: Dive deep into customer behavior through EDA.
-  **Modeling**: Train and compare multiple algorithms like Logistic Regression, Random Forests, and more.
-  **Deployment**: Experience live predictions via an elegant **Streamlit app**.
-  **Interpretability**: Gain insights into why customers churn and how to retain them.

---

##  Repository Structure

| Folder / File           | Description                                           |
|--------------------------|-------------------------------------------------------|
| `data/`                  | Raw and processed datasets                            |
| `notebooks/`             | Exploratory analysis and model-building notebooks     |
| `graphs/`                | Saved visualizations (ROC curves, confusion matrices) |
| `src/`                   | Preprocessing, model training, and evaluation code    |
| `models/`                | Serialized best-performing model(s) (`.pkl`)          |
| `app.py`                 | Streamlit application for interactive predictions     |
| `README.md`              | Project documentation (you're reading it!)             |
| `LICENSE`                | MIT License                                           |

---

##  Technology Stack

| Component              | Tools / Libraries                          |
|------------------------|---------------------------------------------|
| Programming Language   | Python 3.8+                                 |
| Data Handling          | Pandas, NumPy                               |
| Visualization          | Matplotlib, Seaborn, Plotly (optional)      |
| Machine Learning       | Scikit-learn, XGBoost, etc.                |
| Deployment             | Streamlit, Docker (optional)                |

---

##  Sample Model Performance Metrics

**Classification Report**

| Metric     | Score   |
|------------|---------|
| Accuracy   |  88%   |
| Precision  |  0.87  |
| Recall     |  0.85  |
| F1 Score   |  0.86  |

**ROC Curve**

![ROC Curve](graphs/roc_curve.png)

**Confusion Matrix**

![Confusion Matrix](graphs/confusion_matrix.png)

_These visual aids offer a clear understanding of model strengths—and potential areas for improvement._

---

##  Business Context & Insights

Churn can significantly impact revenue. According to industry sources, acquiring a new customer costs up to **five times more** than retaining an existing one :contentReference[oaicite:0]{index=0}. To tackle churn effectively:

1. **Define churn** clearly (e.g., subscription cancellation or inactivity).
2. **Gather diverse data**: demographics, usage patterns, feedback.
3. **Preprocess wisely**: manage missing values, encode features, handle imbalances.
4. **Model & evaluate**: choose algorithms that balance accuracy and recall.
5. **Deploy & monitor** via tools like Streamlit for real-time predictions.

This project aims to blend **business value and technical rigour** seamlessly.

---

##  How to Use Locally

```bash
# Clone the Repository
git clone https://github.com/satyam951kr-ai/Churn-Prediction-Project.git
cd Churn-Prediction-Project

# Install Dependencies
pip install -r requirements.txt

# Run the Streamlit App
streamlit run app.py
