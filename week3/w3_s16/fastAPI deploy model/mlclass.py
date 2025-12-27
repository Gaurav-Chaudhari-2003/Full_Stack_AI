import uvicorn
from fastapi import FastAPI
import pickle
app = FastAPI()
pickle_in = open("models/logRegModel.pkl", "rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Hello and Welcome to 5 Minutes Engineering'}

@app.post('/predict')
def predict(num_links:int, num_words:int, num_special_chars:int, has_spammy_keywords:int):

    prediction = classifier.predict([[num_links,num_words,num_special_chars,has_spammy_keywords]])
    if prediction[0] == 0:
        prediction="NOT SPAM"
    else:
        prediction="SPAM"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
