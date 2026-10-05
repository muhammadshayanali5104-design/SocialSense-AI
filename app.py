from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict-page')
def predict_page():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['age'])
    usage = float(request.form['usage'])
    sleep = float(request.form['sleep'])
    mental = float(request.form['mental'])

    features = np.array([[age, usage, sleep, mental]])

    prediction = model.predict(features)

    score = round(prediction[0], 2)

    return render_template(
        'predict.html',
        prediction_text=score
    )

if __name__ == '__main__':
    app.run(debug=True)