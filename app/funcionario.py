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

@app.route('/att', methods=['GET', 'POST'])
def att():
    if request.method == 'POST':
        search_key = request.form.get('searchKey')
        novos_dados = {
            "email": request.form.get('email'),
            "telefone": request.form.get('telefone'),
        }

        # Carrega os dados existentes
        dados_existentes = carregar_dados()
        registro_encontrado = False

        for registro in dados_existentes:
            if registro.get("clienteNome") == search_key or registro.get("funcionarioNome") == search_key:
                registro_encontrado = True
                # Atualiza apenas os campos não vazios
                for chave, valor in novos_dados.items():
                    if valor:
                        registro[chave] = valor

        if registro_encontrado:
            try:
                with open(ARQUIVO_JSON, 'w') as arquivo:
                    json.dump(dados_existentes, arquivo, indent=4)
                return jsonify({"mensagem": "Dados atualizados com sucesso!"}), 200
            except Exception as e:
                return jsonify({"erro": f"Erro ao atualizar os dados: {e}"}), 500
        else:
            return jsonify({"erro": "Registro não encontrado"}), 404

    return render_template('funcionario/att.html')