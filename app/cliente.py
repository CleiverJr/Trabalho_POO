from app import app
from flask import request, render_template, jsonify, make_response

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

@app.route ("/att")
def att():
    return render_template('att')

@app.route("/attContract.html") 
def attContract():
    return render_template('attContract.html')

@app.route("/contract")
def contract():
    return render_template('contract.html')

@app.route("/login", methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['pswrd']
    render_template('login')

@app.route("/predict") 
def predict():
    return render_template('predict.html')

@app.route("/signup", methods=['POST']) 
def signup():
    user = request.form['user']
    password = request.form['pswrd']
    return render_template('signup.html', user=user, password=password)

@app.route("/suport")
def suport():
    return render_template('suport')

#@app.route("/att", methods=['POST'])
#def att():
    #if request.is_json :
        #req = request.get_json()
        #resposta ={
           # 'name': req.get('name'), 
           # 'cpf': req.get('cpf'), 
           # 'user': req.get('user'),
           # 'pswrd': req.get('pswrd')
        #}
       # resp = make_response(jsonify(resposta), 200) #200 codiog indica que deu certo a requisição
       # return resp
   # else:
       # name = request.form['name']
       # cpf = request.form['cpf']
       # user = request.form['user']
       # password = request.form['pswrd']
       # return render_template('usuario.html', name=name, cpf=cpf, user=user,password=password)