from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from sqlalchemy import CheckConstraint
from model.boardgames import db, Boardgames

app = Flask(__name__)
Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///boardgames.sqlite3'
db.init_app(app)

#Rota principal com render para a página principal
@app.route('/')
def home():
    return render_template("home.html"), 200

#Rota para adicionar jogos ao BD
@app.route('/add_game', methods=['POST'])
def add():
    """
    Adicionar novo Boardgame.
    ---
    parameters:
      - name: nome
        in: formData
        type: string
        required: true
        description: O nome do Boardgame.
      - name: publisher
        in: formData
        type: string
        required: true
        description: A editora que publicou a versão que o usuário possui.
      - name: playtime
        in: formData
        type: integer
        required: true
        description: O tempo médio de uma partida em minutos.
      - name: min_players
        in: formData
        type: integer
        required: true
        description: O número mínimo de jogadores.
      - name: max_players
        in: formData
        type: integer
        required: true
        description: O número máximo de jogadores.
      - name: main_mechanic
        in: formData
        type: string
        required: true
        description: A mecânica principal do jogo.
    responses:
      200:
        description: Boardgame adicionado com sucesso
      400:
        description: Erro se alguma informação faltar ou alguma constraint for desrespeitada.
    """
    nome = request.form.get('nome')
    publisher = request.form.get('publisher')
    playtime = request.form.get('playtime')
    min_players = request.form.get('min_players')
    max_players = request.form.get('max_players')
    main_mechanic = request.form.get('main_mechanic')

    if min_players > max_players and int(playtime) < 0:
      return "Máximo de jogadores maior que o mínimo e tempo de jogo inválido"
    elif min_players > max_players:
      return "Máximo de jogadores menor que o mínimo", 400
    elif int(playtime) < 0:
      return "Tempo de jogo inválido", 400
    else:
      bg = Boardgames(nome, publisher, playtime, min_players, max_players, main_mechanic)
      db.session.add(bg)
      db.session.commit()

    return "Boardgame adicionado com sucesso"


#Rota para listar todos os boardgames do BD
@app.route('/list_all', methods=['GET'])
def list_boardgames():
    """
    Listar todos os Boardgames.
    ---
    responses:
      200:
        description: Uma lista de todos os Boardgames.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: O ID e Primary Key do Boardgame.
              Nome:
                type: string
                description: O nome do Boardgame.
              Publisher:
                type: string
                description: A editora que publicou o Boardgame.
              Tempo de Jogo:
                type: integer
                description: O tempo médio de uma partida em minutos.
              Mínimo de Jogadores:
                type: integer
                description: O número mínimo de jogadores.
              Máximo de Jogadores:
                type: integer
                description: O número máximo de jogadores.
              Mecânica Principal:
                type: string
                description: A mecânica principal do Boardgame.
    """


    boardgames = Boardgames.query.all()
    boardgames_list = []
    
    for game in boardgames:
        game_data = {
            'id': game.id,
            'Nome': game.nome,
            'Publisher': game.publisher,
            'Tempo de Jogo': game.playtime,
            'Mínimo de Jogadores': game.min_players,
            'Máximo de Jogadores': game.max_players,
            'Mecânica Principal': game.main_mechanic
        }
        boardgames_list.append(game_data)
    if len(boardgames_list) == 0:
      return "Não existem boardgames cadastrados", 200 

    return jsonify(boardgames_list)

#Rota para excluir boardgames do BD
@app.route('/boardgames/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Excluir um Boardgame pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: O ID do boardgame para ser deletado.
    responses:
      200:
        description: Boardgame deletado com sucesso.
      404:
        description: Boardgame não encontrado.
    """
    game_to_delete = Boardgames.query.get_or_404(id)
    db.session.delete(game_to_delete)
    db.session.commit()
    return jsonify({'message': 'Boardgame deletado com sucesso'})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
