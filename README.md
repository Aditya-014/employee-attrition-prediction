# Employee Attrition Prediction System

**A machine learning application for predicting employee attrition using HR analytics data.**

An end-to-end machine learning project that analyzes employee-related information, compares classification algorithms, and provides attrition predictions through an interactive Streamlit web application.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189B65?style=for-the-badge&logo=xgboost&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Technology Stack](#technology-stack)
- [Project Workflow](#project-workflow)
- [Machine Learning Models](#machine-learning-models)
- [Model Evaluation](#model-evaluation)
- [Application Features](#application-features)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [How It Works](#how-it-works)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Responsible Use](#responsible-use)

## Overview

Employee attrition occurs when employees leave an organization. High employee turnover can increase recruitment and training costs, affect productivity, and disrupt team performance.

This project applies machine learning to historical HR data to predict whether an employee belongs to the **Attrition: Yes** or **Attrition: No** category.

The project covers data exploration, preprocessing, model training, performance evaluation, model persistence, and an interactive web interface for generating predictions from employee information.

The application is intended as a demonstration of predictive analytics for HR-related problems. Its predictions are estimates based on historical patterns, not guarantees of future employee behavior.

## Objectives

- Explore employee data and identify patterns associated with attrition.
- Prepare numerical and categorical variables for machine learning.
- Train and compare multiple classification algorithms.
- Evaluate performance using multiple classification metrics.
- Save the trained model and preprocessing objects for reuse.
- Develop an interactive application for making predictions.
- Identify limitations and potential improvements for future iterations.

## Dataset

**Dataset:** IBM HR Analytics Employee Attrition

| Property | Description |
|---|---|
| Number of records | 1,470 |
| Original columns | 35 |
| Target variable | `Attrition` |
| Target classes | `Yes`, `No` |
| Learning type | Supervised learning |
| Problem type | Binary classification |

The dataset contains employee-related attributes, including:

- Personal information, such as age and marital status
- Job role and department
- Monthly income and other compensation-related variables
- Overtime and business travel
- Job satisfaction and work environment
- Years of experience and tenure-related information

### Dataset availability

The dataset is not included in this repository.

Obtain an authorized copy of the IBM HR Analytics Employee Attrition dataset from a legitimate source, such as its Kaggle listing. Place the CSV file at:

`data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv`

The dataset is required to reproduce the notebook's data analysis and training workflow. The interactive application instead loads the saved model and preprocessing artifacts.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Preprocessing, classification, and evaluation |
| XGBoost | Gradient-boosting classifier |
| Joblib | Saving and loading trained objects |
| Streamlit | Interactive web application |
| Jupyter Notebook | Experimentation and model development |

## Project Workflow

The project follows a typical machine-learning pipeline:

1. **Data loading:** Load the employee dataset into a Pandas DataFrame.
2. **Exploratory data analysis:** Examine distributions, feature relationships, and attrition-class balance.
3. **Data cleaning:** Remove unnecessary columns, including `EmployeeCount`, `EmployeeNumber`, and `StandardHours`.
4. **Encoding:** Convert categorical features into numerical representations using one-hot encoding.
5. **Data splitting:** Separate the dataset into training and testing subsets.
6. **Feature scaling:** Apply `StandardScaler` to the model input features.
7. **Model training:** Train Logistic Regression, Random Forest, and XGBoost classifiers.
8. **Evaluation:** Compare the models using accuracy, precision, recall, F1-score, and ROC-AUC.
9. **Model persistence:** Save the selected model and associated preprocessing objects.
10. **Application integration:** Load the saved artifacts in the Streamlit application to generate predictions.

## Machine Learning Models

Three supervised classification algorithms were evaluated.

### 1. Logistic Regression

A classification algorithm that estimates class probabilities using a logistic function. It provides a useful baseline for binary classification and can be relatively easy to interpret.

### 2. Random Forest

An ensemble-learning algorithm that combines predictions from multiple decision trees to improve predictive performance and reduce dependence on a single tree.

### 3. XGBoost

A gradient-boosting algorithm that builds decision trees sequentially, with each stage attempting to improve on the existing model.

### Selected model

**Logistic Regression** was selected for the application based on the overall balance of the evaluation metrics obtained in this experiment.

XGBoost achieved higher precision, while Logistic Regression achieved higher recall, F1-score, and ROC-AUC among the three evaluated models.

## Model Evaluation

The models were evaluated using the following reported results:

| Metric | Logistic Regression | Random Forest | XGBoost |
|---|---:|---:|---:|
| Accuracy | 86.05% | 83.33% | 86.05% |
| Precision | 61.54% | 41.67% | 65.00% |
| Recall | 34.04% | 10.64% | 27.66% |
| F1-score | 43.84% | 16.95% | 38.81% |
| ROC-AUC | 80.79% | 78.62% | 76.38% |

### Interpretation

- **Accuracy:** Logistic Regression and XGBoost achieved the same reported accuracy of 86.05%.
- **Precision:** XGBoost achieved the highest precision at 65.00%.
- **Recall:** Logistic Regression achieved the highest recall at 34.04%.
- **F1-score:** Logistic Regression achieved the highest F1-score at 43.84%.
- **ROC-AUC:** Logistic Regression achieved the highest ROC-AUC at 80.79%.

The dataset is imbalanced, with more employees in the `No` class than the `Yes` class. Consequently, accuracy alone does not fully describe the model's performance. The relatively low recall indicates that the selected model misses some employees who actually left.

These metrics describe the reported experiment and should not be interpreted as a guarantee of performance on new organizations or future data.

## Application Features

The Streamlit interface provides:

- An interactive employee-information form
- Organized inputs for personal and job-related attributes
- Salary, performance, career, and work-environment information
- A prediction of whether the employee is classified as likely to leave or stay
- Probability-based prediction output
- Integration with saved model and preprocessing artifacts

The application is designed to make the trained classifier accessible without requiring users to interact directly with the notebook.

## Project Structure

```text
employee-attrition-prediction/
│
├── data/
│   └── raw/                       # Dataset location (not committed)
│
├── models/
│   ├── employee_attrition_model.pkl
│   ├── feature_names.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── Employee_Attrition_Prediction.ipynb
│
├── presentation/
│   ├── Employee-Attrition-Prediction-System.pdf
│   └── Employee-Attrition-Prediction-System.pptx
│
├── reports/
│   ├── Employee_Attrition_Prediction_Internship_Report.docx
│   └── Employee_Attrition_Prediction_Internship_Report.pdf
│
├── screenshots/                   # Application screenshots
│
├── streamlit_app/
│   ├── app.py
│   ├── utils.py
│   └── assets/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Setup

### Prerequisites

- Python installed on your system
- Git installed on your system
- The model and preprocessing files included in the repository

### 1. Clone the repository

```bash
git clone https://github.com/Aditya-014/employee-attrition-prediction.git
cd employee-attrition-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows — Command Prompt**

```cmd
.venv\Scripts\activate.bat
```

**Windows — PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run streamlit_app/app.py
```

Open the local address printed in the terminal, usually:

`http://localhost:8501`

**Note:** The application currently runs locally. Public hosting is not included in this repository setup.

## How It Works

At a high level, the application follows this sequence:

1. The user enters employee attributes in the Streamlit interface.
2. The application converts the submitted values into a DataFrame.
3. The input features are aligned with the feature columns used during training.
4. The saved scaler transforms the input.
5. The trained classifier generates the prediction and class probabilities.
6. The application displays the result.

The saved preprocessing objects are important because inference must use the same feature representation expected by the trained model.

## Limitations

- The model is trained on a specific HR dataset and may not generalize to other organizations.
- The dataset contains an imbalance between employees who stayed and employees who left.
- The selected model's recall is relatively low, meaning some actual attrition cases are missed.
- The current experiment did not use SMOTE or class weighting to address class imbalance.
- Predicted probabilities are not guarantees of actual employee behavior.
- Historical HR data may contain biases or patterns that should not be treated as causal explanations.

## Future Improvements

Potential improvements include:

- Handling class imbalance with class weighting or carefully validated resampling techniques
- Hyperparameter tuning and cross-validation
- Improving recall while evaluating the impact on precision
- Adding model explanations using SHAP or LIME
- Evaluating calibration of predicted probabilities
- Testing on additional representative datasets
- Assessing fairness, privacy, and potential bias
- Deploying the application to a suitable hosting platform
- Adding automated tests and a reproducible training pipeline

## Responsible Use

This project is intended for educational, demonstration, and research purposes.

Employee attrition predictions should be treated as uncertain decision-support signals. They should not be used as the sole basis for employment decisions, employee evaluation, or punitive actions. Any real-world use would require appropriate validation, privacy safeguards, fairness assessment, and human oversight.

---

**Project focus:** HR Analytics · Machine Learning · Binary Classification · Predictive Modeling · Streamlit