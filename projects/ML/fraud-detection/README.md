
# Financial Fraud Detection System

## Overview
This project implements an end-to-end Machine Learning system to detect fraudulent financial transactions in real time. It covers data preprocessing, feature engineering, model training, evaluation, explainability, and deployment via an API.

## Problem Statement
Financial fraud causes major losses every year. The goal is to build a model that predicts whether a transaction is fraudulent while handling highly imbalanced data and minimizing false positives.

## Dataset
Credit Card Fraud Dataset (European cardholders).

## Tech Stack
- Python, Pandas, NumPy
- Scikit-learn
- Random Forest, Logistic Regression, Gradient Boosting
- Isolation Forest for anomaly detection
- SHAP for explainability
- MLflow for experiment tracking
- FastAPI for deployment

## Pipeline
1. Data loading and cleaning
2. Feature engineering
3. Train/test split (stratified)
4. Model training and tuning
5. Evaluation using ROC-AUC and Precision-Recall
6. Explainability using SHAP
7. API deployment using FastAPI

## Evaluation Metrics
- ROC-AUC
- Precision
- Recall
- F1-score
- Confusion Matrix

## API
POST /predict  
Input: Transaction features  
Output: Fraud probability

## Folder Structure
fraud-detection/
- data/
- notebooks/
- training/
- api/
- models/
- mlruns/
- README.md

## How to Run
1. Install dependencies from requirements.txt
2. Run the training script
3. Start API server with FastAPI
4. Send requests to /predict endpoint

## Results
The final model achieves high ROC-AUC on imbalanced data and provides explainable predictions.

## Author
Gaurav Vilas Chaudhari
