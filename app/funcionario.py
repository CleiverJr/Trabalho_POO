from app import app
from flask import request, render_template, jsonify, make_response

@app.route("/signupcli", methods=['POST']) 
def signupcli():
    user = request.form['user']
    password = request.form['pswrd']
    cnpj = request.form['cnpj']
    telefone = request.form['telefone']
    email = request.form['email']
    sede = request.form['sede']
    industria = request.form['industria']
    departamentos = request.form['departamentos']
    n_func = request.form['n_func']
    capital = request.form['capital']
    receita = request.form['receita']
    prop_valor = request.form['prop_valor']
    return render_template('funcionario/signupcli.html', user=user, password=password, cnpj=cnpj, telefone=telefone, 
    email=email, sede=sede, industria=industria, departamentos=departamentos, n_func=n_func, capital=capital,
    receita=receita, prop_valor=prop_valor)

@app.route("/signupfunc", methods=['POST']) 
def signupfunc():
    user = request.form['user']
    password = request.form['pswrd']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    cep = request.form['cep']
    cargo = request.form['cargo']
    salario = request.form['salario']
    formacao = request.form['formacao']
    idade = request.form['idade']
    atuacao = request.form['atuacao']
    tipo = request.form['tipo']
    grau = request.form['grau']
    return render_template('funcionario/signupfunc.html', user=user, password=password, cpf=cpf, telefone=telefone, email=email,
    cep=cep, cargo=cargo, salario=salario, formacao=formacao, idade=idade, atuacao=atuacao, tipo=tipo, grau=grau)

@app.route ("/attcli", methods=['PUT'])
def attcli():
    user = request.form['user']
    password = request.form['pswrd']
    cnpj = request.form['cnpj']
    telefone = request.form['telefone']
    email = request.form['email']
    sede = request.form['sede']
    industria = request.form['industria']
    departamentos = request.form['departamentos']
    n_func = request.form['n_func']
    capital = request.form['capital']
    receita = request.form['receita']
    prop_valor = request.form['prop_valor']
    return render_template('funcionario/attcli.html', user=user, password=password, cnpj=cnpj, telefone=telefone, 
    email=email, sede=sede, industria=industria, departamentos=departamentos, n_func=n_func, capital=capital,
    receita=receita, prop_valor=prop_valor)

@app.route ("/attfunc", methods=['PUT'])
def attfunc():
    user = request.form['user']
    password = request.form['pswrd']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    email = request.form['email']
    cep = request.form['cep']
    cargo = request.form['cargo']
    salario = request.form['salario']
    formacao = request.form['formacao']
    idade = request.form['idade']
    atuacao = request.form['atuacao']
    tipo = request.form['tipo']
    grau = request.form['grau']
    return render_template('funcionario/attfunc', user=user, password=password, cpf=cpf, telefone=telefone, email=email,
    cep=cep, cargo=cargo, salario=salario, formacao=formacao, idade=idade, atuacao=atuacao, tipo=tipo, grau=grau)

@app.route("/attcontract") 
def attContract():
    return render_template('attContract.html')