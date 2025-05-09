#importar a classe Flask
from flask import Flask, render_template, request, listaUsuarios

#instanciar o servidor Flask
app = Flask(__name__)

#criar variável global (lista de usuários)
listaUsuarios = ["Gracilene"]

#rota padrão (ir para página principal)
@app.route("/")
def index():
    return render_template("index.html")

#rota para direcionar para página de cadastro
@app.route("/paginaCadastro")
def paginaCadastro():
    return render_template("cadastro.html")

#rota para direcionar para página de cadastro
@app.route("/paginaLista")
def paginaCadastro():
    return render_template("listar.html")

@app.route("/cadastrarUsuario", methods=["POST"])
def cadastrar():
    
    nome = request.form.get("nomeUsuario")
    login = request.form.get("loginUsuario")
    senha = request.form.get("senhaUsuario")
    
    listaUsuarios.append([nome, login, senha])
    mensagem="Usuário Cadastrado com Sucesso"
    return render_template("resultado.html", mensagem=mensagem)

#criar uma rota para verificar se o usuário está na lista de convidados
@app.route("/verificarUsuario", methods=['POST'])
def verificar():
    nome = request.form.get("nomeUsuario")
    if(nome in listaUsuarios):
        mensagem="você está convidado"
        return render_template("resultado.html", mensagem=mensagem)
    else:
        mensagem="você NÃO está convidado"
        return render_template("resultado.html", mensagem=mensagem)
    
@app.route("/listarConvidados")
def listar():
    return render_template("listar.html", convidados=listaUsuarios)

#executar o servidor Flask
app.run(debug=True)