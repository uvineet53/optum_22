# coding=utf-8
import numpy as np
import os
import time
from flask import Flask, request, jsonify, render_template
import joblib
from flask.ext.heroku import Heroku
#from tensorflow.keras.models import load_model

# Define a flask app
app = Flask(__name__)
model = joblib.load('models/rf_model.h5')
#model = load_model('models/rf_model.h5')



# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nfrxwrxpyogqgs:e50e1c7425c88564e20bad61fb03f85dcca91714c19ec4051143c97c73dba4ed@ec2-34-194-119-178.compute-1.amazonaws.com:5432/d5hbgqogn1i8gj'
# heroku = Heroku(app)
# db = SQLAlchemy(app)



# DATABASE_URL will contain the database connection string:
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://nfrxwrxpyogqgs:e50e1c7425c88564e20bad61fb03f85dcca91714c19ec4051143c97c73dba4ed@ec2-34-194-119-178.compute-1.amazonaws.com:5432/d5hbgqogn1i8gj', '')
# Connects to the database using the app config
#db = SQLAlchemy(app)

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