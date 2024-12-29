# criar as rotas da aplicação

from flask import render_template, url_for
from Fake_pintrest_projeto import app


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/perfil/<usuario>')
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
