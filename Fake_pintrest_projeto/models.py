# criar modelos do banco de dados

from Fake_pintrest_projeto import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False, unique=True)
    email = database.Column(database.String(120), nullable=False, unique=True)
    senha = database.Column(database.String(80), nullable=False)
    fotos = database.relationship('Foto', backref='usuario', lazy=True)


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(120), default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)