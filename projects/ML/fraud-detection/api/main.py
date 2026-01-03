from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / "models" / "fraud_model.pkl")
threshold = joblib.load(BASE_DIR / "models" / "threshold.pkl")
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")


class Transaction(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(tx: Transaction):
    X = np.array(tx.features).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0][1]
    is_fraud = int(prob >= threshold)
    return {
        "fraud_probability": float(prob),
        "is_fraud": is_fraud
    }
