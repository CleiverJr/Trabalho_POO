from app import app
from flask import request, render_template, jsonify, make_response, session, redirect, url_for

@app.route("/") 
def main():
    return render_template('index.html') # Está correto

@app.route("/index") 
def index():
    return render_template('index.html') # Está correto

@app.route("/home") 
def home():
    return render_template('index.html') # Está correto

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=['POST'])

def logincli():
    email = request.form.get('email')  
    password = request.form.get('password')
    
    if email == "funcionario@gmail.com" and password == "123":
        session['user_email'] = email  # Salva o e-mail na sessão
        return redirect(url_for('attcontract'))
    elif email == "cliente@gmail.com" and password == "123":
        session['user_email'] = email  # Salva o e-mail na sessão
        return redirect(url_for('predict'))
    else:        
        return "Login inválido!", 401

