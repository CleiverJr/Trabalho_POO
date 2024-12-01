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

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simulação de autenticação
        if username == 'cliente':
            session['user_type'] = 'cliente'
            return redirect(url_for('cliente_routes.analise'))
        elif username == 'funcionario':
            session['user_type'] = 'funcionario'
            return redirect(url_for('funcionario_routes.cadastro'))
        else:
            return "Login inválido!"
    
    return render_template('login.html')