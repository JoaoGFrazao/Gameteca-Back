from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Boardgames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    publisher = db.Column(db.String(20), nullable=False)
    playtime = db.Column(db.Integer, nullable=False)
    min_players = db.Column(db.Integer, nullable=False)
    max_players = db.Column(db.Integer, nullable=False)
    main_mechanic = db.Column(db.String(20), nullable=False)

    __table_args__ = (CheckConstraint('min_players < max_players', name='min_max_player_invalido'),
                      CheckConstraint('playtime > 0', name='invalid_playtime'))

    def __init__(self, nome, publisher, playtime, min_players, max_players, main_mechanic):
        self.nome = nome
        self.publisher = publisher
        self.playtime = playtime
        self.min_players = min_players
        self.max_players = max_players
        self.main_mechanic = main_mechanic
