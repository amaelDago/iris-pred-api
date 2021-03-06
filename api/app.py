#!/usr/bin/python
import pickle
import numpy as np
from flask import Flask, request, render_template

# Define application
app = Flask(__name__)

# Deine route for homepage
@app.route("/")
def index() : 
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def predict() : 
    values = [float(x) for x in request.form.values()]
    values = np.array(values).reshape(1,-1)
    prediction = model.predict(values)
    return render_template('index.html', prediction_text= 'It seem you give characteristic of : \"{}\" is \n '.format(" ".join(prediction)))
     
if __name__ == "__main__" : 
    model= pickle.load(open("./model/model.pkl", "rb"))
    app.run(debug = True, host='0.0.0.0')
	
