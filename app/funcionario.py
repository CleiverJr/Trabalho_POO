from app import app
from flask import Flask, request, render_template, jsonify
import os
import json
import logging

# Caminho do arquivo JSON
CONTRACTS_FILE = "contratos.json"

# Caminho para o arquivo JSON
ARQUIVO_JSON = "dados_signup.json"

# Funcao para carregar os dados existentes no JSON
def carregar_dados():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []

# Funcao para salvar os dados no JSON
def salvar_dados(novos_dados):
    dados_existentes = carregar_dados()
    dados_existentes.append(novos_dados)
    
    try:
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")


@app.route("/attcontract")
def attcontract():
    return render_template('funcionario/attContract.html')

# Função para carregar os contratos do arquivo JSON
def load_contracts():
    if os.path.exists(CONTRACTS_FILE):
        with open(CONTRACTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Função para salvar os contratos no arquivo JSON
def save_contracts(contracts):
    with open(CONTRACTS_FILE, "w", encoding="utf-8") as file:
        json.dump(contracts, file, indent=4, ensure_ascii=False)

@app.route("/get_contract/<cliente>")
def get_contract(cliente):
    contracts = load_contracts()
    if cliente in contracts:
        return jsonify(contracts[cliente])
    return jsonify({"error": "Cliente não encontrado"}), 404

@app.route("/update_contract/<cliente>", methods=["POST"])
def update_contract(cliente):
    contracts = load_contracts()
    if cliente in contracts:
        data = request.json
        # Atualizar somente os campos existentes, evitando duplicação
        for key in contracts[cliente]:
            if key in data:
                contracts[cliente][key] = data[key]
        save_contracts(contracts)
        return jsonify({"message": "Contrato atualizado com sucesso!"})
    return jsonify({"error": "Cliente não encontrado"}), 404

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
                "clienteIndústria": request.form.get('clienteIndústria'),
                "clienteCapital": request.form.get('clienteCapital'),
                "clienteSenha": request.form.get('clienteSenha')
            }
        elif user_type == 'Funcionário':
            dados = {
                "tipo": "Funcionário",
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


@app.route("/att")
def att():
    return render_template("funcionario/att.html")

def load_att():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Função para salvar os contratos no arquivo JSON
def save_att(contracts):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as file:
        json.dump(contracts, file, indent=4, ensure_ascii=False)

@app.route("/get_all_contracts")
def get_all_contracts():
    contracts = load_att()
    return jsonify(contracts)

@app.route("/get_att/<user_type>/<identifier>")
def get_att(user_type, identifier):
    contracts = load_att()
    if user_type == 'Cliente':
        for cliente, data in contracts.items():
            if data.get("clienteCnpj") == identifier:
                return jsonify(data)
    elif user_type == 'Funcionário':
        for funcionario, data in contracts.items():
            if data.get("funcionarioCpf") == identifier:
                return jsonify(data)
    return jsonify({"error": "Identificador não encontrado"}), 404

@app.route("/update_att/<identifier>", methods=["POST"])
def update_att(identifier):
    contracts = load_att()
    for cliente, data in contracts.items():
        if data.get("clienteCnpj") == identifier or data.get("funcionarioCpf") == identifier:
            updated_data = request.json
            # Atualizar os dados do cliente ou funcionário
            for key in updated_data:
                if key in data:
                    data[key] = updated_data[key]
            save_att(contracts)
            return jsonify({"message": "Dados atualizados com sucesso!"})
    return jsonify({"error": "Cliente ou Funcionário não encontrado"}), 404
