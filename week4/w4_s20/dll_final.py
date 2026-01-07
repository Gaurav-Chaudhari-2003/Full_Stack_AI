import uvicorn
from fastapi import FastAPI, UploadFile, File
from tensorflow import keras
from io import BytesIO
from PIL import Image
import numpy as np

app = FastAPI()

(X_train, y_train), _ = keras.datasets.mnist.load_data()
X_train = X_train / 255.0
X_train = X_train.reshape(len(X_train), 784)

model = keras.Sequential([
    keras.layers.Input(shape=(784,)),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=5)


@app.get("/")
def index():
    return {"Deployment": "Hello and Welcome to 5 Minutes Engineering"}

@app.post("/predict")
async def predict1(file: UploadFile = File(...)):
    image = await file.read()
    image = Image.open(BytesIO(image)).convert("L")             # L = GreyScale Image
    image = image.resize((28, 28))

    pic = np.array(image) / 255.0
    pic_flattened = pic.reshape(1, 784)                         # 0 --> 1 Dimension Conversion

    predicted = model.predict(pic_flattened)
    prediction = int(np.argmax(predicted[0]))

    labels = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    return {"Prediction": labels[prediction]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
