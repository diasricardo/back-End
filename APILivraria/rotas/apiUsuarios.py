from flask import Blueprint, jsonify, request
from conexao  import criar_conexao, fechar_conexao

usuarios_bp = Blueprint('usuarios', __name__)