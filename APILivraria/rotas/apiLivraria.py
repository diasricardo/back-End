from flask import Blueprint, jsonify, request
from conexao  import criar_conexao, fechar_conexao

livros_bp = Blueprint('livros', __name__)

#rota ou endpoint obterlivros
@livros_bp.route('/obterLivros', methods=['GET'])
def obterLivros():
    #criar conexao e um novo cursor
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)

    #Executa a consulta SQL para obter Livros
    cursor.execute('SELECT * FROM LIVROS')
    livros = cursor.fetchall()

    cursor.close()
    fechar_conexao(conexao)
    return jsonify(livros)


@livros_bp.route('/incluirLivro', methods=['POST'])
def incluirLivro():
    #recupera dados do livro
    novoLivro = request.get_json()

    #validação de dados
    #verifica se os campos 'tiulo' e 'autor' estão no objeto
    if 'titulo' not in novoLivro or 'autor' not in novoLivro:
        return jsonify({'status': 'error', 'message': 'Dados Incompletos'}), 400
    
    conexao = criar_conexao()
    cursor = conexao.cursor()

    try: 
        #insere o novo livro no banco
        comando = 'INSERT INTO LIVROS(TITULO, AUTOR) VALUES(%s, %s)' 
       # %f para ponto flutuante
       # %d para valores inteiros
       # %t para datas e horas
       # %b para booleanos
       # %s para strings

        cursor.execute(comando, (novoLivro['titulo'], novoLivro['autor']))
        #confirma ainserção do novo livro
        conexao.commit()

        #retorna um jSon com status
        status = {'status': 'success', 'code': 201}

    except Exception as e:
        # em caso de erro, desfaz as alterações e retornar o erro
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
    
    finally:
        cursor.close()
        fechar_conexao(conexao)
    
    return jsonify(status)


@livros_bp.route('/alterarLivro/<int:id>', methods=['PUT'])
def alterarLivroId(id):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    
    dados = request.get_json()

    try:
       # lista de campos a serem atualizados e lista de valores correspondentes
       campos_para_atualizar = []
       valores_para_atualizar = []
       
       if 'titulo' in dados:
           campos_para_atualizar.append('titulo = %s')
           valores_para_atualizar.append(dados['titulo'])
        
       if 'autor' in dados:
           campos_para_atualizar.append('autor = %s')
           valores_para_atualizar.append(dados['autor'])
       if not campos_para_atualizar:
           return jsonify({'status': 'error', 'message': 'Nenhum campo Fornecido'}), 400
       
       #constroi uma consulta de atualização
       comando = "UPDATE LIVROS SET " + ", ".join(campos_para_atualizar) + " WHERE ID_LIVROS = %s"
       valores = valores_para_atualizar + [id]

       #executar a consulta de atualização
       cursor.execute(comando, valores)
       conexao.commit()

       status = {'status': 'success', 'message': 'Livro alterado com sucesso'}
       return jsonify(status), 201

    except Exception as e:
        # em caso de erro, desfaz as alterações e retornar o erro
        conexao.rollback()
        status = {'status': 'error', 'message': comando}
        return jsonify(status)
    finally:
        cursor.close()
        fechar_conexao(conexao)


@livros_bp.route('/apagarLivro/<int:id>', methods=['DELETE'])
def deletarLivro(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    livro_existe = cursor.execute('SELECT COUNT(*) FROM LIVROS WHERE ID_LIVROS = %s', (id,))
    #consumir o resultado
    cursor.fetchone()

    if livro_existe == 0:
        return jsonify({'status': 'error', 'message': "livro não encontrado"}), 404
    
    try:
        #deleta o livro com o ID especifico
        comando = 'DELETE FROM LIVROS WHERE ID_LIVROS = %s'
        cursor.execute(comando, (id,))

        conexao.commit()
        status = {'status': 'success', 'message': 'Livro deletado com sucesso'}, 201

    except Exception as e:
        # Em caso de erro, desfaz as alterações e retorna uma mensagem de erro
        conexao.rollback()
        status = {'status': 'error', 'message': str(e)}
    finally:
        # Fecha o cursor e a conexão
        cursor.close()
        conexao.close()

    # Retorna o status da operação
    return jsonify(status)   

