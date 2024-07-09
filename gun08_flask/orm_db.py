from flask import Flask
from flask_sqlalchemy import *

app = Flask(__name__)

app.secret_key = b'dsafdsfkjkljretertjkl'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kitaplikdb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODİFİCATİONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Kitap(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_name = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()