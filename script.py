#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
#from feature_extractor import feature_extractor

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#def ValuePredictor(to_predict_list):
#    to_predict = np.array(to_predict_list).reshape(1,10)
#    loaded_model = pickle.load(open("model.pkl","rb"))
#    result = loaded_model.predict(to_predict)
#    return result[0]
#
#@app.route('/result',methods = ['POST'])
#def result():
#    if request.method == 'POST':
#        to_predict_list = request.form.to_dict()
#        to_predict_list=list(to_predict_list.values())
#        to_predict_list = feature_predictor(to_predict_list)
#        result = ValuePredictor(to_predict_list)
#        
#        prediction='Predicted Chain Length is ' + result
#            
#        return render_template("result.html",prediction=prediction)
