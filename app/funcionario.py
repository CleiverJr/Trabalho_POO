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
    arquivo_json = "dados_signup.json"
    if request.method == 'POST':
        clienteCnpj = request.form.get('clienteCnpj')
        funcionarioCpf = request.form.get('funcionarioCpf')
        if funcionarioCpf == '':
            chamada = clienteCnpj
        else: 
            chamada = clienteCnpj
        dados = {
            "clienteNome": request.form.get('clienteNome'),
            "clienteEmail": request.form.get('clienteEmail'),
            "clienteDepartamentos": request.form.get('clienteDepartamentos'),
            "clienteReceita": request.form.get('clienteReceita'),
            "clienteCnpj": request.form.get('clienteCnpj'),
            "clienteSede": request.form.get('clienteSede'),
            "clienteFuncionarios": request.form.get('clienteFuncionarios'),
            "clientePv": request.form.get('clientePv'),
            "clienteTelefone": request.form.get('clienteTelefone'),
            "clienteIndústria": request.form.get('clienteIndústria'),
            "clienteCapital": request.form.get('clienteCapital'),
            "clienteSenha": request.form.get('clienteSenha'),
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

        # Verifica se o arquivo existe e carrega os dados
        if os.path.exists(arquivo_json):
            with open(arquivo_json, 'r') as arquivo:
                try:
                    dados_existentes = json.load(arquivo)
                except json.JSONDecodeError:
                    return "Erro ao carregar os dados existentes.", 400
        else:
            return "Arquivo de dados não encontrado.", 404
        
        # Atualiza o cliente baseado na chamada
        for usuario in dados_existentes:
            if usuario[chamada] == chamada:
                usuario.update(dados)
                break
        else:
            return "Cliente não encontrado.", 404
        
        # Salva os dados atualizados
        try:
            with open(arquivo_json, 'w') as arquivo:
                json.dump(dados_existentes, arquivo, indent=4)
        except Exception as e:
            return f"Erro ao salvar os dados: {e}"

        return "Cliente atualizado com sucesso!"
        
    return render_template('funcionario/att.html')

@app.route('/get_identifiers', methods=['GET'])
def get_identifiers():
    user_type = request.args.get('type')
    if not user_type:
        return jsonify({"error": "Tipo de usuário não especificado"}), 400

    try:
        with open("dados_signup.json", "r") as arquivo:
            dados = json.load(arquivo)
        if user_type == "Cliente":
            identifiers = [cliente["clienteCnpj"] for cliente in dados if "clienteCnpj" in cliente]
        elif user_type == "Funcionário":
            identifiers = [funcionario["funcionarioCpf"] for funcionario in dados if "funcionarioCpf" in funcionario]
        else:
            return jsonify({"error": "Tipo de usuário inválido"}), 400

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