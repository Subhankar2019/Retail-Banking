#Here we will write all of our routes

from application import app,db
from application.models import User,Customer,Account
from flask import render_template, request, Response,flash,redirect
from application.forms import LoginForm
while (Customer.objects.all().count()==0):
    Customer(ssn_id="111222333444",customer_id="900000000",customer_name="Subhankar Majumder",age="23",address="Sodepur",state="West Bengal",city="Kolkata",customer_status="Demo Customer created Successfully").save()
    Account(customer_id="900000000",account_id="101011000",account_type="Current Account",deposit_amount="1000",account_status="Demo Account created Successfully").save()
@app.route("/", methods=['POST','GET'])
@app.route("/login", methods=['POST','GET'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        id=form.user_id.data
        password=form.password.data
        user=User.objects(user_id=id).first()
        if user and password == user.password and user.work == "executive":
            return redirect("/executive")
        elif user and password == user.password and user.work == "cashier":
            return redirect("/cashier")
        else:
            flash("Sorry, something went wrong")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/executive")
def executive():
    return render_template("executive.html")

@app.route("/cashier")
def cashier():
    return render_template("cashier.html")

@app.route("/register_customer",methods=["POST","GET"])
def register_customer():
    if request.method=="POST":
        ssn_id=request.form["ssnid"]
        check=Customer.objects(ssn_id=ssn_id).first()
        customer_id=str(int(Customer.objects.order_by('-customer_id').first().customer_id)+2)
        customer_name=request.form["customerName"]
        age=request.form["age"]
        address=request.form["address"]
        state=request.form["state"]
        city=request.form["city"]
        if(check):
            message="Ssn Id Already Exist"
        else:
            message="Customer Created Successfully"
            customer=Customer(ssn_id=ssn_id,customer_id=customer_id,customer_name=customer_name,age=age,address=address,state=state,city=city,customer_status=message).save()
        return render_template("register_customer.html",message=message)
    return render_template("register_customer.html")


@app.route("/search_customer")
def search():
    return render_template("search_customer.html")

@app.route("/update_customer/search",methods=["GET","POST"])
def search_update():
    if request.method=="POST":
        ssn_id=request.form["ssnId"]
        customer_id=request.form["customerId"]
        check_ssn=Customer.objects(ssn_id=ssn_id).first()
        check_cusid=Customer.objects(customer_id=customer_id).first()
        print(check_cusid)
        print(check_ssn)
        if check_ssn or check_cusid:
            if check_cusid==None and check_ssn==None:
                return render_template("search_customer.html")
            elif check_cusid==None:
                return render_template("update_customer.html",form=check_ssn)
            else:
                return render_template("update_customer.html",form=check_cusid)
    return render_template("search_customer.html")

@app.route("/delete_customer/search",methods=["GET","POST"])
def search_delete():
    if request.method=="POST":
        ssn_id=request.form["ssnId"]
        customer_id=request.form["customerId"]
        check_ssn=Customer.objects(ssn_id=ssn_id).first()
        check_cusid=Customer.objects(customer_id=customer_id).first()
        print(check_cusid)
        print(check_ssn)
        if check_ssn or check_cusid:
            if check_cusid==None and check_ssn==None:
                return render_template("search_customer.html")
            elif check_cusid==None:
                return render_template("delete_customer.html",form=check_ssn)
            else:
                return render_template("delete_customer.html",form=check_cusid)
    return render_template("search_customer.html")


@app.route("/delete_customer/<id>",methods=["GET","POST"])
def delete(id):
    if request.method=="POST":
        Customer.objects(customer_id=id).delete()
        return render_template("executive.html",mes="data deleted successfully")


@app.route("/update_customer/<id>",methods=["GET","POST"])
def update(id):
    if request.method=="POST":
        customer=Customer.objects(customer_id=id).first()
        customer.customer_name=request.form["newcustomername"]
        customer.address=request.form["newaddress"]
        customer.age=request.form["newage"]
        customer.save()
        return render_template("executive.html",mes="data updated successfully")

@app.route("/create_account",methods=["GET","POST"])
def create_account():
    if request.method=="POST":
        customer_id=request.form["customerId"]
        check_cusid=Customer.objects(customer_id=customer_id).first()
        account_id=str(int(Account.objects.order_by('-customer_id').first().account_id)+2)
        account_type=request.form["account_type"]
        check_type=Account.objects(customer_id=customer_id,account_type=account_type).first()
        deposit_amount=request.form["depositAmount"]
        if(not check_cusid):
            message="Customer Id doesnot Exist"
        elif(check_type):
            message="Customer already has account of specific type"
            account=Account.objects(customer_id=customer_id,account_type=account_type).first()
            account.account_status=message
            account.save()

        else:
            message="Account Created Successfully"
            account=Account(customer_id=customer_id,account_id=account_id,account_type=account_type,deposit_amount=deposit_amount,account_status=message).save()
        return render_template("create_account.html",message=message)
    return render_template("create_account.html")


@app.route("/delete_account/search",methods=["GET","POST"])
def search_delete_account():
    if request.method=="POST":
        account_id=request.form["accountid"]
       
        customer_id=request.form["customerid"]
        check_id=Account.objects(account_id=account_id).first()
        
        check_cusid=Account.objects(customer_id=customer_id).all()
     
        if check_id or check_cusid:
            if not check_cusid and not check_id:
                return render_template("search_account.html")
            elif not check_cusid:
                return render_template("delete_account.html",form=check_id)
            else:
              
                return render_template("delete_account.html",form_list=check_cusid)
    return render_template("search_account.html")


@app.route("/delete_account/<id>",methods=["GET","POST"])
def delete_account(id):
    if request.method=="POST":
        Account.objects(account_id=id).delete()
        return render_template("executive.html",mes="data deleted successfully")

@app.route("/delete_account",methods=["GET","POST"])
def delete_account2():
    if request.method=="POST":
        account_id=request.form["accountid"]
        account_type=request.form["accounttype"]
        account=Account.objects(account_id=account_id,account_type=account_type).delete()
        if account==0:
            return render_template("delete_account.html",message="AccountId is and Account type is not matching")
        else:
            return render_template("executive.html",mes="data deleted successfully")
        
    return render_template("delete_account.html")


@app.route("/customer_status",methods=["GET","POST"])

def customer_status():
    customers=Customer.objects.all()
    return render_template("customer_status.html",customers=customers)


@app.route("/account_status",methods=["GET","POST"])

def account_status():
    accounts=Account.objects.all()
    return render_template("account_status.html",accounts=accounts)