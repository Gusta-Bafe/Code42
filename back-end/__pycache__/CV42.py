from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt=Bcrypt(app)

from viewsGames import *
from viewsUsers import *
from viewshistorias import *
from viewsPerso import *

if __name__ == '__main__':
    app.run(port=3000, debug=True)

