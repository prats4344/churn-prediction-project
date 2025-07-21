<<<<<<< HEAD
# churn-prediction-project
End-to-end machine learning project to predict customer churn
=======
<h1 align="center">📊 End-to-End Customer Churn Prediction 🚀</h1>


<p align="center">
  This project demonstrates a real-world machine learning application that predicts customer churn for a telecom company.<br>
  It showcases a complete <strong>MLOps workflow</strong> – from data analysis & experiment tracking to model deployment as an interactive web app.
</p>

---

## 🌟 **Key Features**
✅ **Interactive Web App** – Built with Streamlit for live churn predictions  
✅ **Scalable API Backend** – Served using FastAPI for reliable predictions  
✅ **Advanced Modeling** – Uses XGBoost, a high-performance gradient boosting algorithm  
✅ **Automated Hyperparameter Tuning** – Optimized using Optuna  
✅ **Experiment Tracking** – Managed with MLflow for reproducibility  
✅ **Model Explainability** – Visualized with SHAP to interpret model decisions  

---

## ⚙️ **Project Workflow**
The project follows a structured **MLOps pipeline**:

1️⃣ **Data Ingestion & Cleaning** – Handle missing values, inconsistent data types  
2️⃣ **Exploratory Data Analysis (EDA)** – Identify patterns & churn correlations  
3️⃣ **Feature Engineering & Preprocessing** – One-hot encode categorical features & scale numerical data  
4️⃣ **Experimentation & Tracking (MLflow)**  
    - Build baseline model  
    - Tune hyperparameters with Optuna  
    - Log experiments & metrics  
5️⃣ **Model Explainability (SHAP)** – Identify key features influencing churn  
6️⃣ **Model Deployment**  
   - Save final model & preprocessing pipeline (`.pkl`, `.json`)  
   - Deploy FastAPI backend (`/predict` endpoint)  
   - Serve interactive Streamlit frontend  

---

## 🛠️ **Tech Stack**

| **Component**        | **Technology**                          |
|-----------------------|------------------------------------------|
| **Language**         | Python 3.10+                             |
| **Modeling**         | Pandas, Scikit-learn, XGBoost            |
| **Hyperparameter Tuning** | Optuna                              |
| **Experiment Tracking**   | MLflow                               |
| **Explainability**    | SHAP                                    |
| **API Backend**       | FastAPI, Uvicorn                        |
| **Frontend**          | Streamlit                               |
| **Version Control**   | Git & GitHub                             |

---


## 🚀 **Local Setup & Installation**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/prats4344/churn-prediction-project.git
cd churn-prediction-project
```
### 2️⃣ Install Dependencies
pip install -r requirements.txt

---

## 🧠 Model Insights: Why Do Customers Churn?

Using SHAP, we explain the model predictions:
Top Features: Contract, tenure, InternetService

Interpretation:
- Low tenure → higher probability of churn (blue SHAP values)
- Long-term customers (high tenure) → lower churn probability (red SHAP values)

---

## ✨ Author
👤 Pratiyusha Kanungo


⭐ If you find this project useful, consider starring the repo!

>>>>>>> c3c3e569bb58b58247e0845dab28b75658742fd2
