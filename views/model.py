import os
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KET'] = 'mysecretkey'

########################################
###########SETUP THE DATABASE###########
########################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/test'


db = SQLAlchemy(app)


class Puppy(db.Model):
    __tablename__ = 'puppies'

    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Puppy name is {self.name}"