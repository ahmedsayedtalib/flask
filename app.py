from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/info')
def info():
    return '<h1>This is my first flask app!</h1>'

## DYNAMIC ROUTES

@app.route('/customers/<user>')
def customer(user):
    return "<h3>Hello, {}</h3>".format(user.title())

@app.route('/letter/<num>')
def letter_num(num):
    return "<h1>Letter number is {}</h1>".format(num[10])

if __name__ == "__main__":
    app.run(debug=True)