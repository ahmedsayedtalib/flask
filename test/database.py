from basic import app,Customer,db

with app.app_context():
    hassan  = Customer('Hassan',17)
    laila   = Customer('Laila',15)
    mohamed = Customer('Mohamed',13)
    

    db.create_all()

    db.session.add_all([hassan,laila,mohamed])

    db.session.commit()


    