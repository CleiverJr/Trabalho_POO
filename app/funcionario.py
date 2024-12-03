from app import app
from flask import Flask, request, render_template, jsonify
import os
import json


# Caminho para o arquivo JSON
ARQUIVO_JSON = "dados_signup.json"

# Função para carregar os dados existentes no JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

# Função para salvar os dados no JSON
def salvar_dados(novos_dados):
    dados_existentes = carregar_dados()
    dados_existentes.append(novos_dados)
    
    try:
        with open(ARQUIVO_JSON, 'w') as arquivo:
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print("entrou no metodo")
    if request.method == 'POST':
        print("entrou no metodo")
        user_type = request.form.get('userType')

        if user_type == 'Cliente':
            dados = {
                "tipo": "Cliente",
                "clienteNome": request.form.get('clienteNome'),
                "clienteEmail": request.form.get('clienteEmail'),
                "clienteDepartamentos": request.form.get('clienteDepartamentos'),
                "clienteReceita": request.form.get('clienteReceita'),
                "clienteCnpj": request.form.get('clienteCnpj'),
                "clienteSede": request.form.get('clienteSede'),
                "clienteFuncionarios": request.form.get('clienteFuncionarios'),
                "clientePv": request.form.get('clientePv'),
                "clienteTelefone": request.form.get('clienteTelefone'),
                "clienteIndustria": request.form.get('clienteIndústria'),
                "clienteCapital": request.form.get('clienteCapital'),
                "clienteSenha": request.form.get('clienteSenha')
            }
        elif user_type == 'Funcionário':
            dados = {
                "tipo": "Funcionario",
                "funcionarioNome": request.form.get('funcionarioNome'),
                "funcionarioEmail": request.form.get('funcionarioEmail'),
                "funcionarioSalario": request.form.get('funcionarioSalario'),
                "funcionarioSenha": request.form.get('funcionarioSenha'),
                "funcionarioCpf": request.form.get('funcionarioCpf'),
                "funcionarioCep": request.form.get('funcionarioCep'),
                "funcionarioFormação": request.form.get('funcionarioFormação'),
                "funcionarioTipo": request.form.get('funcionarioTipo'),
                "funcionarioTelefone": request.form.get('funcionarioTelefone'),
                "funcionarioCargo": request.form.get('funcionarioCargo'),
                "funcionarioIdade": request.form.get('funcionarioIdade'),
                "funcionarioGrau": request.form.get('funcionarioGrau')
            }
        else:
            print("Passou direto")
            return "Erro: Tipo de usuário não reconhecido", 400

        # Salva os dados no arquivo JSON
        salvar_dados(dados)

        return render_template('funcionario/signup.html')
    print("Passou direto")

    return render_template('funcionario/signup.html')

@app.route("/attcontract") 
def attcontract():
    return render_template('funcionario/attContract.html')

@app.route ("/att", methods=['GET', 'POST'])
def att():
    dados = carregar_dados()
    print('carregou os dados')
    user_type = request.form.get('tipo')
    identificador = request.form.get('identifierSelect')
    print(identificador)
    
    if request.method == 'POST':
        novos_dados = {}
        print('acessou o POST')
        if user_type == 'Cliente':
            print("viu que era tipo:Cliente")
            novos_dados = {
                "tipo": "Cliente",
                "clienteNome": request.form.get('clienteNome'),
                "clienteEmail": request.form.get('clienteEmail'),
                "clienteDepartamentos": request.form.get('clienteDepartamentos'),
                "clienteReceita": request.form.get('clienteReceita'),
                "clienteCnpj": request.form.get('clienteCnpj'),
                "clienteSede": request.form.get('clienteSede'),
                "clienteFuncionarios": request.form.get('clienteFuncionarios'),
                "clientePv": request.form.get('clientePv'),
                "clienteTelefone": request.form.get('clienteTelefone'),
                "clienteIndustria": request.form.get('clienteIndústria'),
                "clienteCapital": request.form.get('clienteCapital'),
                "clienteSenha": request.form.get('clienteSenha')
            }
        elif user_type == 'Funcionario':
            novos_dados = {
                "tipo": "Funcionario",
                "funcionarioNome": request.form.get('funcionarioNome'),
                "funcionarioEmail": request.form.get('funcionarioEmail'),
                "funcionarioSalario": request.form.get('funcionarioSalario'),
                "funcionarioSenha": request.form.get('funcionarioSenha'),
                "funcionarioCep": request.form.get('funcionarioCep'),
                "funcionarioFormação": request.form.get('funcionarioFormação'),
                "funcionarioTipo": request.form.get('funcionarioTipo'),
                "funcionarioTelefone": request.form.get('funcionarioTelefone'),
                "funcionarioCargo": request.form.get('funcionarioCargo'),
                "funcionarioIdade": request.form.get('funcionarioIdade'),
                "funcionarioGrau": request.form.get('funcionarioGrau')
            }
        # Atualiza os dados na lista
        registro_atualizado = False
        for registro in dados:
            if registro.get("tipo") == user_type:
                print('tipo = usertype')
                print(registro.get("clienteCnpj"))
                if user_type == "Cliente": 
                    if registro.get("clienteCnpj") == identificador:
                        print('cnpj corresponde')
                if user_type == "Funcionario":
                    if registro.get("funcionarioCpf") == identificador:
                        print('cpf corresponde')
                    registro.update(novos_dados)
                    print('updtae no json feito')
                    registro_atualizado = True
                    break
            print('Atualizando os dados')

        if registro_atualizado:
            salvar_dados(dados)  # Salva os dados atualizados no JSON
            print("deu mec")
            return "Dados atualizados com sucesso.", 200
        else:
            print('deu bosta')
            return "Registro não encontrado.", 404
        
    return render_template('funcionario/att.html')

#dropdown
@app.route('/get_identifiers', methods=['GET'])
def get_identifiers():
    user_type = request.args.get('type')

    if not user_type:
        return jsonify({"error": "Tipo de usuário não fornecido"}), 400

    try:
        with open("dados_signup.json", "r") as arquivo:
            dados = json.load(arquivo)

        identifiers = []
        for usuario in dados:
            if user_type == "Cliente":
                if usuario.get("clienteCnpj"):
                    identifiers.append(usuario.get("clienteCnpj"))
            elif user_type == "Funcionário":
                if usuario.get("funcionarioCpf"):
                    identifiers.append(usuario.get("funcionarioCpf"))
        
        return jsonify(identifiers)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_type = request.args.get('type')
    identifier = request.args.get('id')

    if not user_type or not identifier:
        return jsonify({"error": "Parâmetros insuficientes"}), 400

    try:
        with open("dados_signup.json", "r") as arquivo:
            dados = json.load(arquivo)

        for usuario in dados:
            if (user_type == "Cliente" and usuario.get("clienteCnpj") == identifier) or \
                (user_type == "Funcionário" and usuario.get("funcionarioCpf") == identifier):
                return jsonify(usuario)

        return jsonify({"error": "Usuário não encontrado"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500