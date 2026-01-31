import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name is {self.name}"


########################################
###### ROUTES ##########################
########################################

# Make '/' redirect to /home
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pups'))
    return render_template('add.html', form=form)

@app.route('/list')
def list_pups():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        if pup:
            db.session.delete(pup)
            db.session.commit()
        return redirect(url_for('list_pups'))
    return render_template('delete.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
