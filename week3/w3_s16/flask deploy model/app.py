import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='.')
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        return render_template('index.html', prediction_text='Species = {}'.format(prediction[0]))
    except (ValueError, TypeError):
        return render_template('index.html', prediction_text='Error: Please provide valid numeric inputs.')

if __name__ == "__main__":
    app.run(debug=True)