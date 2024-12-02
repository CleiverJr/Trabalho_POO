from app import app
from flask import request, render_template, jsonify, make_response
import json
import os

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        clienteNome = request.form.get('clienteNome')
        clienteEmail = request.form.get('clienteEmail')
        clienteDepartamentos = request.form.get('clienteDepartamentos')
        clienteReceita = request.form.get('clienteReceita')
        clienteCnpj = request.form.get('clienteCnpj')
        clienteSede = request.form.get('clienteSede')
        clienteFuncionarios = request.form.get('clienteFuncionarios')
        clientePv = request.form.get('clientePv')
        clienteTelefone = request.form.get('clienteTelefone')
        clienteIndústria = request.form.get('clienteIndústria')
        clienteCapital = request.form.get('clienteCapital')
        clienteSenha = request.form.get('clienteSenha')
        funcionarioNome = request.form.get('funcionarioNome')
        funcionarioEmail = request.form.get('funcionarioEmail')
        funcionarioSalario = request.form.get('funcionarioSalario')
        funcionarioSenha = request.form.get('funcionarioSenha')
        funcionarioCpf = request.form.get('funcionarioCpf')
        funcionarioCep = request.form.get('funcionarioCep')
        funcionarioFormação = request.form.get('funcionarioFormação')
        funcionarioTipo = request.form.get('funcionarioTipo')
        funcionarioTelefone = request.form.get('funcionarioTelefone')
        funcionarioCargo = request.form.get('funcionarioCargo')
        funcionarioIdade = request.form.get('funcionarioIdade')
        funcionarioGrau = request.form.get('funcionarioGrau')
        funcionarioSenha = request.form.get('funcionarioSenha')
        
        # Cria um dicionário com os dados
        dados = {
            "clienteNome": clienteNome,
            "clienteEmail": clienteEmail,
            "clienteDepartamentos": clienteDepartamentos,
            "clienteReceita": clienteReceita,
            "clienteCnpj": clienteCnpj,
            "clienteSede": clienteSede,
            "clienteFuncionarios": clienteFuncionarios,
            "clientePv": clientePv,
            "clienteTelefone": clienteTelefone,
            "clienteIndústria": clienteIndústria,
            "clienteCapital": clienteCapital,
            "clienteSenha": clienteSenha,
            "funcionarioNome": funcionarioNome,
            "funcionarioEmail": funcionarioEmail,
            "funcionarioSalario": funcionarioSalario,
            "funcionarioSenha": funcionarioSenha,
            "funcionarioCpf": funcionarioCpf,
            "funcionarioCep": funcionarioCep,
            "funcionarioFormação": funcionarioFormação,
            "funcionarioTipo": funcionarioTipo,
            "funcionarioTelefone": funcionarioTelefone,
            "funcionarioCargo": funcionarioCargo,
            "funcionarioGrau": funcionarioGrau
        }
        
        # Define o caminho do arquivo JSON
        arquivo_json = "dados_signup.json"

        # Verifica se o arquivo já existe e carrega os dados existentes
        dados_existentes = []
        if os.path.exists(arquivo_json):
            with open(arquivo_json, 'r') as arquivo:
                try:
                    dados_existentes = json.load(arquivo)
                except json.JSONDecodeError:
                    dados_existentes = []  # Se o arquivo estiver vazio ou inválido
        
        # Adiciona os novos dados
        dados_existentes.append(dados)
        
        # Salva os dados atualizados no arquivo JSON
        try:
            with open(arquivo_json, 'w') as arquivo:  # Modo 'w' para sobrescrever
                json.dump(dados_existentes, arquivo, indent=4)  # Salva no formato JSON com indentação
        except Exception as e:
            return f"Erro ao salvar os dados: {e}"
        
        return render_template('funcionario/signup.html', **dados)
    return render_template('funcionario/signup.html')


# @app.route("/signup", methods=['GET','POST']) 
# def signupfunc():
#     if request.method == 'POST':

#         user = request.form.get['user']
#         password = request.form.get['pswrd']
#         cpf = request.form.get['cpf']
#         telefone = request.form.get['telefone']
#         email = request.form.get['email']
#         cep = request.form.get['cep']
#         cargo = request.form.get['cargo']
#         salario = request.form.get['salario']
#         formacao = request.form.get['formacao']
#         idade = request.form.get['idade']
#         atuacao = request.form.get['atuacao']
#         tipo = request.form.get['tipo']
#         grau = request.form.get['grau']

#         return render_template('funcionario/signup.html', user=user, password=password, cpf=cpf, telefone=telefone, email=email,cep=cep, cargo=cargo, salario=salario, formacao=formacao, idade=idade, atuacao=atuacao, tipo=tipo, grau=grau)
#     return render_template('funcionario/signup.html')

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