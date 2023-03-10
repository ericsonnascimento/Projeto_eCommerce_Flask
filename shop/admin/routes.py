from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt

from .forms import RegistrationForm, LoginForm
from .models import User

@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Por favor faça o login', 'atenção!')
        return redirect(url_for('login'))
    #products = Addproduct.query.all()
    return render_template('admin/index.html', tittle="Admin Page") #products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data) #hash recebendo dados do formulário através do form.password.data
        user = User(name=form.name.data, username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()        
        flash(f'Bem Vindo {form.name.data}, Obrigado por se registrar, sucesso!')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration Page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Ben vindo {form.email.data} Você está logado agora', 'sucesso!')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Email ou senha inválidos, por favor tente novamente', 'atenção!')
    return render_template('admin/login.html', form=form, tittle='Login Page')