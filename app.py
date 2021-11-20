# coding=utf-8
import numpy as np
import os
import time
from flask import Flask, request, jsonify, render_template
import joblib

# Define a flask app
app = Flask(__name__)
model = joblib.load('models/rf_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    if prediction==0:
        return render_template('index.html',
                               prediction_text='Low chances of patient readmitted to hospital.'.format(prediction),
                               )
    else:
        return render_template('index.html',
                               prediction_text='High chances of patient readmitted to hospital'.format(prediction),
                              )

if __name__ == "__main__":
    app.run(debug=True)