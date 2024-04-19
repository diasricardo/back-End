from flask import Flask
from rotas.apiLivraria import livros_bp
from rotas.apiUsuarios import usuarios_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#REgistrar as rotas dos livros
app.register_blueprint(livros_bp, url_prefix='/livros')

#Registrar rotas de usuarios
app.register_blueprint(usuarios_bp, url_prefix='/usuarios')

#Inicia o servidor Flask
if __name__ == '__main__':
    app.run(port=5000, host='192.168.0.226', debug=True)