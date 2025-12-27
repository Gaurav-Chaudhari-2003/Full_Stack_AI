import numpy as np
import uvicorn
from fastapi import FastAPI
import pickle

app = FastAPI()
pickle_in = open('models/scaler.pkl', 'rb')
scaler = pickle.load(pickle_in)
pickle_in = open("models/outlier_detection_model.pkl", "rb")
model = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to 5 Minutes Engineering'}


@app.post('/predict')
def predict(num_links: int, num_words: int, num_special_chars: int, has_spammy_keywords: int):

    x = np.array([[num_links, num_words, num_special_chars, has_spammy_keywords]])
    x_scaled = scaler.transform(x)

    score = model.decision_function(x_scaled)[0]
    prediction = model.predict(x_scaled)[0]
    return {
        "anomaly_score": float(score),
        "is_outlier": bool(prediction == -1)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
