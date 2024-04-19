#1 - Objetivo criar uma api que disponibiliza 
#a consulta, Criação edição e exclusão de livros.
#2 - URL Bases - localhost
# 3 - Endpoints - 
#               localhost/livros    (GET)  Obter os dados 
#               localhost/livros    (POST) Criar um novo registro
#               localhost/livros/id (PUT)  Atualizar dados de um registro
#               localhost/livros/id (DELETE) Excluir um registro

from flask import Flask, jsonify, request
from flask_cors import CORS

#criando instancia do flask
app = Flask(__name__)
CORS(app)

#criando uma lista com vários objetos
livros = [
    {"id": 1, "titulo": "O senhor dos Anéis", "autor": "J.R.R Tolkien"},
    {"id": 2, "titulo": "Harry Potter", "autor": "J.K Roling"},
    {"id": 3, "titulo": "O pequeno Principe", "autor": "Antonie De saint-exupéry"}
]
filmes = [
    {"id" : 1, 'nome' : 'Vingadores'},
    {"id" : 2, 'nome' : 'Velozes e Furiosos'},
    {"id" : 3, 'nome' : 'Kung Fu Panda'},
    {"id" : 4, 'nome' : 'John Wick'},
    {"id" : 5, 'nome' : 'Tropa de Elite'},
]

ceps = [
    {'id': 1, 'cep' : '16900119', 'rua': 'Rua Paes Leme'},
    {'id': 2, 'cep' : '16901190', 'rua': 'Rua Arlindo Monteverde'},
    {'id': 3, 'cep' : '16900534', 'rua': 'Rua A'},
]

@app.route('/cep/<string:cep>', methods=['GET'])
def obterCEP(cep):
    for end in ceps:
        if end.get('cep') == cep:
            return jsonify(end)

#Endpoint para obter todos os livros
@app.route('/obterLivros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

#Endpoint para obter livro randomico
@app.route('/obterLivroAleatorio', methods=['GET'])
def obterLivroAleatorio():
    import random
    livro = random.choice(livros)
    return jsonify(livro)

#endpoint  para obter livros por ID
@app.route('/obterLivroId/<int:id>', methods=['GET'])
def obterLivroId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#endpoint para incluir um  novo livro
@app.route('/incluirLivro', methods=['POST'])
def incluirLivro():
    #obtem os dados JSOn enviados na solicitação 
    novoLivro = request.get_json()
    #Adiciona o novo livro à lista de livros
    livros.append(novoLivro)
    return jsonify(livros)

#endpoint para editar livro por ID
@app.route('/editarLivros/<int:id>', methods=['PUT'])
def editarLivroId(id):
    livroAlterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            #atualiza os detalhes do livro com os novos dados
            livros[indice].update(livroAlterado)
            #retorna o livro atualizado
            return jsonify(livros[indice])

#endpoint para excluir um livro por ID
@app.route('/apagarLivro/<int:id>', methods=['DELETE'])
def apagarLivroId(id):
    for indice , livro in enumerate(livros):
        if livro.get('id') == id:
            #remover o livro da lista
            del livros[indice]
            return "Excluido com sucesso"
            break

#inicia o servidor Flask
if __name__ == '__main__':
    app.run(port=5000, host='192.168.0.226', debug=True)