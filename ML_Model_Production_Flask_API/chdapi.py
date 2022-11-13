#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from flask import Flask, abort, jsonify, request, redirect, url_for, send_file, send_from_directory
import pickle
import os
my_logit = pickle.load(open("logreg.pkl","rb"))

from flask_cors import CORS
from werkzeug import secure_filename
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
#CORS(app)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/upload/'.format(PROJECT_HOME)
DOWNLOAD_FOLDER = '{}/download/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route('/api',methods = ['POST','GET'])
def make_pridict():
    if request.method == 'POST':
        print(request.files)
        print()
        print(request.form)
        file = request.files['file']
        if file.filename != '':
            print(file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('file path is', os.path.join(app.config['UPLOAD_FOLDER'], filename))

            df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(list(df))
            df.drop(['Sno', 'education', 'currentSmoker', 'BPMeds', 'prevalentHyp', 'totChol', 'diaBP', 'BMI', 'heartRate', 'glucose'], axis = 1, inplace=True)
            print(list(df))
            
            Pred_result = my_logit.predict(df)
            prediction_result = list(pd.Series(Pred_result))
            df['predict_result']= prediction_result

            print(df.head())
            df.to_csv(os.path.join(app.config['DOWNLOAD_FOLDER'], filename), index=False)
            print(df.head())
            url = "http://localhost:5000/download/"+filename
            print(url)

            return jsonify({"download_url":url})
           
    else:
        print('method is not POST')


if __name__ == '__main__':
    app.run(port=5000,debug = True)







