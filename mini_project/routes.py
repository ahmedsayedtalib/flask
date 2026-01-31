from forms import AddForm,DelForm
from model import app,db,Car,User
from flask import redirect,render_template,url_for


@app.route('/',methods=['GET'])
def index():
    return redirect(url_for('home'))

@app.route('/home',methods=['GET','POST'])
def home():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_user = User(name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template('home.html',form=form) 


@app.route('/list',methods=['GET'])
def list_users():
    list_usr = User.query.all()
    return render_template('list.html',list_usr=list_usr)


if __name__ == "__main__":
    app.run(debug=True)