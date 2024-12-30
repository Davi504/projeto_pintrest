# criar os formulários da aplicação
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Fake_pintrest_projeto.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    senha = PasswordField('Senha', Validators=[DataRequired(), Length(min=6)], render_kw={'placeholder': 'Senha'})
    botao = SubmitField('Fazer Login')

class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    username = StringField('Nome de usuario', validators=[DataRequired(), Length(min=2, max=20)], render_kw={'placeholder': 'Username'})
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)], render_kw={'placeholder': 'Senha'})
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')], render_kw={'placeholder': 'Confirmar senha'})
    botao_confirmacao = SubmitField('Criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError('Email já cadastrado, tente outro, ou faça login') 