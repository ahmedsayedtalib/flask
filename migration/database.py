import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/migration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Migrate(app,db)
#After connecting the app to the db, we need to execute the following command from the terminal:-
# windows:- set FLASK_APP = database.py, linux:- export FLASK_APP = database.py
# then:- 
# flask db init
# flask db migrate -m "created migration customer's table" the -m parameter is optional but recommended
# flask db upgrade


class Customer(db.Model):

    __tablename__ = 'customers'
    id    = db.Column(db.Integer,primary_key=True)
    name  = db.Column(db.Text,nullable=False)
    age   = db.Column(db.Integer)
    email = db.Column(db.Text)

    def __init__(self,name,age,email):
        self.name  = name
        self.age   = age
        self.email = email

    def __repr__(self):
        return f"Name:- {self.name}, Age:- {self.age} \n Email:- {self.email}"