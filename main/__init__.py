from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_assets import Environment, Bundle
from flask_bcrypt import Bcrypt
from datetime import datetime # newly added
from flask_login import LoginManager


app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'sdfhjjguj^%&%786tfg7d6c7dfgfiudyfd87'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

assets = Environment(app)
login_manager.login_message_category = 'info'
js = Bundle('./js/script.js','./js/customScripts.js',
            output='gen/scripts.js')
assets.register('js_all', js)
css = Bundle('./css/styles.css', './css/dashboard.css' ,
            output='gen/styles.css')
assets.register('css_all', css)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dxeohiehtqctmb:46bdc29c50ac6d626bbc3255c1cda52732c161806d907c11a472bfe9eb73fea7@ec2-3-91-139-25.compute-1.amazonaws.com:5432/d68lllaljad3l6'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/klik'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from main import routes
