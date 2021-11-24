# coding=utf-8
import numpy as np
import os
import time
from flask import Flask, request, jsonify, render_template
import joblib

#from flask.ext.heroku import Heroku
#from tensorflow.keras.models import load_model

# Define a flask app
app = Flask(__name__)
model = joblib.load('models/rm_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():

    if request.method == 'POST':

        age = int(request.form['age'])
        time_in_hospital = int(request.form['time_in_hospital'])
        number_of_procedures = int(request.form['number_of_procedures'])
        number_of_medications = int(request.form['number_of_medications'])
        race = int(request.form['race'])
        gender = int(request.form['gender'])

        prediction = model.predict([[age, time_in_hospital, number_of_procedures, number_of_medications, race, gender]])
        # output = round(prediction[0],2)

        if prediction == 0:
            return render_template('index.html', prediction_text='Low chances of patient readmitted to hospital within 30 days.')
        else:
            return render_template('index.html', prediction_text='High chances of patient readmitted to hospital within 30 days')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)