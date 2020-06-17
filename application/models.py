#Here we will work with database and create tables like user,customer
import flask
from application import db,app
class User(db.Document):
    user_id=db.StringField(Unique=True,min_length=8)
    password=db.StringField()
    work=db.StringField()

class Customer(db.Document):
    ssn_id=db.StringField(Unique=True)
    customer_id=db.StringField(Unique=True)
    customer_name=db.StringField()
    age=db.StringField()
    address=db.StringField()
    state=db.StringField()
    city=db.StringField()
    customer_status=db.StringField()

class Account(db.Document):
    customer_id=db.StringField()
    account_id=db.StringField()
    account_type=db.StringField()
    deposit_amount=db.StringField()
    account_status=db.StringField()
