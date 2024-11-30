from app import app
from flask import request, render_template, jsonify, make_response

@app.route("/signup", methods=['POST']) 
def signup():
    user = request.form['user']
    password = request.form['pswrd']
    return render_template('signup.html', user=user, password=password)

@app.route ("/att")
def att():
    return render_template('att')

@app.route("/attContract.html") 
def attContract():
    return render_template('attContract.html')