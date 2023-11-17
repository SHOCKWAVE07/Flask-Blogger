from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = '9622b37098c8b814b528f422a83cc4ed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
db = SQLAlchemy(app)

from flaskblog import routes

