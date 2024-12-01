from app import app
from flask import request, render_template, jsonify, make_response

@app.route("/contract")
def contract():
    return render_template('contract.html')

@app.route("/predict") 
def predict():
    return render_template('cliente/predict.html')

@app.route("/suport")
def suport():
    return render_template('suport')