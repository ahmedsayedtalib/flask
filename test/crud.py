from basic import db, Customer, app


with app.app_context():

    Customer.query.delete()

    hassan  = Customer('Hassan', 17)
    laila   = Customer('Laila', 15)
    mohamed = Customer('Mohamed', 13)
    maha    = Customer('Maha', 28)
    ali     = Customer('Ali', 22)
    roaa    = Customer('Roaa', 8)

    db.session.add_all([hassan, laila, mohamed, maha, ali])
    db.session.commit()

    db.session.add(roaa)

    db.session.delete(hassan)
    roaa.age = 22



    db.session.commit()


    print(Customer.query.all())
    print(Customer.query.filter_by(name='Maha').first())
