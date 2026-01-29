import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id   = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text,nullable = True)
    age  = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age  = age
    
    def __repr__(self):
        return f"Name:- {self.name}, Age:- {self.age}"