# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cs", methods = ['POST'])
def cs():
    model = pickle.load(open('model.pkl', 'rb'))

    #exemplo que tem diabetes
    # lista = [6,148,72,35,0,33.6,0.627,50]

    #exemplo que NAO tem diabetes
    # lista = [6,120,72,35,0,33.6,0.427,25]

    lista = [
        request.form.get('Pregnancies'),
        request.form.get('Glucose'),
        request.form.get('BloodPressure'),
        request.form.get('SkinThickness'),
        request.form.get('Insulin'),
        request.form.get('BMI'),
        request.form.get('DiabetesPedigreeFunction'),
        request.form.get('Age'),
    ]

    reshaped = np.reshape(lista, [1, -1])

    predict = model.predict(reshaped);

    if predict[0] == 1:
        resposta = "Você tem diabetes"
    else:
        resposta = "Você não tem diabetes"

    return render_template("index.html", result = 1, data = resposta)


# if __name__ == '__main__': # This only runs if
#   app.run()