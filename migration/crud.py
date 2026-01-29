from database import app, Customer, db



with app.app_context():

    db.create_all()
    Customer.query.delete()

    ali     = Customer('Ali', 22,'ali@hotmail.com')
    maha    = Customer('Maha', 28,'maha@gmail.com')
    mohamed = Customer('Mohamed', 22,'mohamed@outlook.com')
    roaa    = Customer('Roaa', 16,'roaa@yahoo.com')
 
    db.session.add_all([ali, maha, mohamed,roaa])

    roaa.age = 26

    db.session.commit()

    print(Customer.query.all())


