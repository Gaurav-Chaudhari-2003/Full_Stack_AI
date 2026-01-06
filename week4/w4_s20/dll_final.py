import uvicorn
from tensorflow import keras
from fastapi import FastAPI, File, UploadFile
from sklearn.preprocessing import MinMaxScaler
from io import BytesIO
from PIL import Image
import numpy as npy

app = FastAPI()


@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to 5 Minutes Engineering'}


@app.post("/predict")
async def predict1(
        file: UploadFile = File(...)):
    (X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()

    X_train = MinMaxScaler().fit_transform(X_train)
    X_test = X_test / 255

    input_array_size = pow((X_train[0].shape[0]), 2)
    X_train_flattened = X_train.reshape(len(X_train), input_array_size)
    X_test_flattened = X_test.reshape(len(X_test), input_array_size)

    cnn_model = keras.Sequential([
        keras.layers.Dense(300, input_dim=input_array_size, activation='relu'),     # Hidden Layer
        keras.layers.Dense(10, activation='softmax')]                               # Output Layer
    )

    cnn_model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    cnn_model.fit(X_train_flattened, y_train, epochs=3)

    image = await file.read()
    image = Image.open(BytesIO(image))
    image = image.convert("L")

    pic = npy.array(image)

    pic = MinMaxScaler().fit_transform(pic)
    pic_flattened = pic.reshape(input_array_size)
    pic_flattened = npy.expand_dims(pic_flattened, axis=0)
    predicted = cnn_model.predict(pic_flattened)
    prediction = npy.argmax(predicted[0])
    if prediction == 0: output = 'zero'
    elif prediction == 1: output = 'one'
    elif prediction == 2: output = 'two'
    elif prediction == 3: output = 'three'
    elif prediction == 4: output = 'four'
    elif prediction == 5: output = 'five'
    elif prediction == 6: output = 'six'
    elif prediction == 7: output = 'seven'
    elif prediction == 8: output = 'eight'
    else : output = 'nine'

    return {"Prediction": output}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=5000)