from app import app
from flask import request, render_template, jsonify, make_response

@app.route("/signup", methods=['GET', 'POST'])
def signupcli():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pswrd')
        cnpj = request.form.get('cnpj')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        sede = request.form.get('sede')
        industria = request.form.get('industria')
        departamentos = request.form.get('departamentos')
        n_func = request.form.get('n_func')
        capital = request.form.get('capital')
        receita = request.form.get('receita')
        prop_valor = request.form.get('prop_valor')

        return render_template('funcionario/signup.html',user=user,password=password,cnpj=cnpj,telefone=telefone,email=email,sede=sede,industria=industria,departamentos=departamentos,n_func=n_func, capital=capital, receita=receita, prop_valor=prop_valor)
    return render_template('funcionario/signup.html')


@app.route("/signup", methods=['GET','POST']) 
def signupfunc():
    if request.method == 'POST':

        user = request.form.get['user']
        password = request.form.get['pswrd']
        cpf = request.form.get['cpf']
        telefone = request.form.get['telefone']
        email = request.form.get['email']
        cep = request.form.get['cep']
        cargo = request.form.get['cargo']
        salario = request.form.get['salario']
        formacao = request.form.get['formacao']
        idade = request.form.get['idade']
        atuacao = request.form.get['atuacao']
        tipo = request.form.get['tipo']
        grau = request.form.get['grau']

        return render_template('funcionario/signup.html', user=user, password=password, cpf=cpf, telefone=telefone, email=email,cep=cep, cargo=cargo, salario=salario, formacao=formacao, idade=idade, atuacao=atuacao, tipo=tipo, grau=grau)
    return render_template('funcionario/signup.html')

@app.route ("/att", methods=['GET', 'PUT'])
def attcli():
    if request.method == 'PUT':

        user = request.form.get['user']
        password = request.form.get['pswrd']
        cnpj = request.form.get['cnpj']
        telefone = request.form.get['telefone']
        email = request.form.get['email']
        sede = request.form.get['sede']
        industria = request.form.get['industria']
        departamentos = request.form.get['departamentos']
        n_func = request.form.get['n_func']
        capital = request.form.get['capital']
        receita = request.form.get['receita']
        prop_valor = request.form.get['prop_valor']

        return render_template('funcionario/att.html', user=user, password=password, cnpj=cnpj, telefone=telefone, email=email, sede=sede, industria=industria, departamentos=departamentos, n_func=n_func, capital=capital,receita=receita, prop_valor=prop_valor)
    return render_template('funcionario/att.html')


@app.route ("/att", methods=['GET', 'PUT'])
def attfunc():
    if request.method == 'PUT':

        user = request.form.get['user']
        password = request.form.get['pswrd']
        cpf = request.form.get['cpf']
        telefone = request.form.get['telefone']
        email = request.form.get['email']
        cep = request.form.get['cep']
        cargo = request.form.get['cargo']
        salario = request.form.get['salario']
        formacao = request.form.get['formacao']
        idade = request.form.get['idade']
        atuacao = request.form.get['atuacao']
        tipo = request.form.get['tipo']
        grau = request.form.get['grau']
        return render_template('funcionario/att.html', user=user, password=password, cpf=cpf, telefone=telefone, email=email, cep=cep, cargo=cargo, salario=salario, formacao=formacao, idade=idade, atuacao=atuacao, tipo=tipo, grau=grau)
    return render_template('funcionario/att.html')

@app.route("/attcontract") 
def attContract():
    return render_template('funcionario/attcontract.html')