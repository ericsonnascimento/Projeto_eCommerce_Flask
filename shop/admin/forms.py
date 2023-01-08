from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome', [validators.Length(min=4, max=25)])
    username = StringField('Nome de Usuário', [validators.Length(min=4, max=25)])
    email = StringField('Endereço de email', [validators.Length(min=6, max=35), validators.Email("Endereço de email inválido!")])
    password = PasswordField('Nova senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha diferente!')
    ])
    confirm = PasswordField('Repita a senha')
    
class LoginForm(Form):
    email = StringField('Endereço de email', [validators.Length(min=6, max=35), validators.Email("Endereço de email inválido!")])
    password = PasswordField('Nova senha', [validators.DataRequired()])
    