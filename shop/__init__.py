from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3306/myshop'
app.config['SECRET_KEY'] = 'jhgdsusd63t3yguydg387gu38'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes

