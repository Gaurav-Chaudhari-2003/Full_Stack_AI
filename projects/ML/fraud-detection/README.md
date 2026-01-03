
# 🚨 Financial Fraud Detection System

## Overview
An end-to-end Machine Learning system to detect fraudulent financial transactions.  
Built for **learning purposes** to strengthen ML fundamentals and system thinking.

---

## 🎯 Objectives
- Handle highly imbalanced data
- Detect fraud with high recall
- Control false alerts via threshold tuning
- Validate predictions on real fraud samples
- Deploy model via API

---

## 📊 Dataset
**Credit Card Fraud Dataset (European cardholders)**  
- 284,807 transactions  
- 492 fraud cases (~0.17%)  
- 30 numerical features + target `Class`  

---

## 🧰 Tech Stack
| Area | Tools |
|------|--------|
| Language | Python |
| Data | Pandas, NumPy |
| Modeling | Scikit-learn |
| Explainability | SHAP |
| API | FastAPI |
| Tracking | MLflow |
| Serialization | Joblib |

---

## 🔁 ML Pipeline
1. Load & explore data  
2. Preprocess & scale  
3. Handle imbalance  
4. Train models  
5. Tune threshold  
6. Validate on fraud samples  
7. Explain & deploy  

---

## 📈 Model Performance
- ROC-AUC ≈ 0.98  
- Fraud Recall ≈ 99%  
- Missed Frauds: 4 / 492  

---

## 🗂 Folder Structure
```
fraud-detection/
│
├── data/
├── notebooks/
├── training/
├── api/
├── models/
├── mlruns/
└── README.md
```

---

## 🔌 API Usage

Start server:
```bash
uvicorn api.main:app --reload
```


POST /predict: example for fraud transaction
```json
{
  "features": [
    -3.0435406239976, -3.15730712090228, 1.08846277997285, 2.2886436183814,
    1.35980512966107, -1.06482252298131, 0.325574266158614, -0.0677936531906277,
    -0.270952836226548, -0.838586564582682, -0.414575448285725, -0.503140859566824,
    0.676501544635863, -1.69202893305906, 2.00063483909015, 0.666779695901966,
    0.599717413841732, 1.72532100745514, 0.283344830149495, 2.10233879259444,
    0.661695924845707, 0.435477208966341, 1.37596574254306, -0.293803152734021,
    0.279798031841214, -0.145361714815161, -0.252773122530705, 0.0357642251788156,
    529, 1
  ]
}

```

Response:
```json
{
  "fraud_probability": 0.92,
  "is_fraud": 1
}
```

---

## 🧠 Key Learnings
- Accuracy is misleading for anomaly detection
- Precision vs Recall is a risk trade-off
- Threshold defines system behavior
- Validation matters more than metrics

---

## 👤 Author
**Gaurav Vilas Chaudhari**  
B.E. Computer Science & Engineering  

---

## ⚠️ Disclaimer
Educational project only. Not intended for production or financial decisions.
