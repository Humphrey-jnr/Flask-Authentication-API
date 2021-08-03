from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='ecc436c6cb247e6808ea7b31'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from package import routes