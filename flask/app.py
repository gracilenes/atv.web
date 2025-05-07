#importar a classe Flask
from flask import Flask, render_template

#instanciar o servidor Flask
app = Flask(__name__)

#criar variável global (lista de usuários)
convidados = ["Gracilene"]

#rota padrão (ir para página principal)
@app.route("/")
def index():
    return render_template("index.html")

#rota para direcionar para página de cadastro
@app.route("/registre", methods=["GET", "POST"])
def registre():
    return render_template("cadastro.html")

#rota para direcionar para página de lista de convidados