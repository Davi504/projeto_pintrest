from Fake_pintrest_projeto import app, database
from Fake_pintrest_projeto.models import Usuario, Foto


with app.app_context():
    database.create_all()