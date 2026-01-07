import uvicorn
from tensorflow.python.keras.models import load_model
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import numpy as np


from tensorflow.keras.models import load_model
model = load_model("animal_classifier.keras")


app = FastAPI()


@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to 5 Minutes Engineering'}


@app.post("/predict")
async def predict1(file: UploadFile = File(...)):
    image = await file.read()
    image = Image.open(BytesIO(image)).convert("RGB")

    image = image.resize((100, 100))  # ← FIX

    pic = np.array(image) / 255.0
    pic = np.expand_dims(pic, axis=0)

    predicted = model.predict(pic)
    prediction = predicted[0][0]

    output = "Dog" if prediction >= 0.9 else "Cat"
    print(prediction)
    return {"Prediction": output}



if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=5000)