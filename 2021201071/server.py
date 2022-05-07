from enum import unique
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_user, logout_user
from flask_login import login_required, UserMixin, current_user
from werkzeug.wrappers import response
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/flaskassign'
app.config['SECRET_KEY'] = 'password'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Customer(UserMixin, db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_chef = db.Column(db.Boolean, default=False, nullable=False)
    orders = db.relationship('Order', backref='customer')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    transaction = db.Column(db.String(100), nullable=False)
    bill = db.Column(db.String(2000), nullable=False)
    custid = db.Column(db.Integer, db.ForeignKey("customer.id"))


class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    half_plate = db.Column(db.Integer)
    full_plate = db.Column(db.Integer)


@login_manager.user_loader
def load_user(user_id):
    """[for user id]

    Args:
        user_id ([any]): [user id]

    Returns:
        [int]: [user id]
    """
    return Customer.query.get(int(user_id))


@app.route('/do_signin', methods=['POST'])
def do_signin():
    """[for sign in]

    Returns:
        [string]: [about signin]
    """
    if(request.method == 'POST'):
        response = request.get_json()
        username = response['username']
        password = response['password']
        check_user = Customer.query.filter_by(username=username).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "LOGGED in successfully"
            else:
                return "Incorrect Password"
        else:
            return "No such User exists"


@app.route('/do_signup', methods=['GET', 'POST'])
def do_signup():
    """[for signing up]

    Returns:
        [string]: [Register]
    """
    if(request.method == 'POST'):
        response = request.get_json()
        username = response['username']
        password = response['password']

        check_user = Customer.query.filter_by(username=username).first()
        if(check_user is not None):
            return "User already registered, please sign in"
        else:
            user = Customer(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return "Registered Successfully"


@app.route('/signout', methods=['GET'])
@login_required
def signout():
    """[function for signning out]

    Returns:
        [string]: [signout successful]
    """
    logout_user()
    return "Sign out successful"


@app.route('/menu', methods=['POST'])
@login_required
def add_menu():
    """[function for updating menu]

    Returns:
        [string]: [whether menu updated or not]
    """
    menurecvd = request.get_json()
    user = load_user(current_user.id)
    if user.is_chef:
        new_item = Menu(id=menurecvd["id"], half_plate=menurecvd["half_plate"],
                        full_plate=menurecvd["full_plate"])
        db.session.add(new_item)
        db.session.commit()
        return "Menu updated Successfully"
    else:
        return "You are not a Chef. Menu not updated"


@app.route('/menu', methods=['GET'])
@login_required
def get_menu():
    """[function for returning menu list]

    Returns:
        [dict]: [menu list]
    """
    menulist = {}
    menu = Menu.query.all()
    if len(menu) == 0:
        menulist = {
            "response": "No Data"
        }
        return menulist
    for element in menu:
        menulist[str(element.id)] = {
            "half_plate": element.half_plate, "full_plate": element.full_plate}
    return menulist


@app.route('/make-chef/<username>', methods=['PUT'])
@login_required
def make_chef(username):
    """[function for making any user as chef]

    Args:
        username ([string ]): [username of user]

    Returns:
        [string ]: [to make user chef]
    """
    user = Customer.query.filter_by(username=username).first()
    if user is not None:
        user.is_chef = True
        db.session.commit()
        return "User " + str(username) + " is chef now!!"
    else:
        return "User not exist"


@app.route('/order', methods=['POST'])
@login_required
def add_order():
    """[function for adding order ]

    Returns:
        [string ]: [About order placed]
    """
    req_content = request.get_json()
    new_order = Order(custid=current_user.id,
                      bill=req_content["bill"],
                      transaction=req_content["transaction"])
    db.session.add(new_order)
    db.session.commit()
    return "Order Placed successfully"


@app.route('/is-chef', methods=['GET'])
@login_required
def is_chef():
    """[check whether user is chef]

    Returns:
        [string ]: [Yes or No]
    """
    user = load_user(current_user.id)
    if user.is_chef:
        return "Yes"
    else:
        return "No"


@app.route('/order', methods=['GET'])
@login_required
def get_order():
    """[function for getting order]

    Returns:
        [dictionary]: [details of order]
    """
    order_detail = {"response": []}
    user = load_user(current_user.id)
    if len(user.orders) == 0:
        return order_detail
    else:
        order_detail["response"] = []
        for index in range(len(user.orders)):
            order_detail["response"].append({"transaction":
                                             user.orders[index].transaction,
                                             "bill": user.orders[index].bill
                                             })
        return order_detail


if __name__ == '__main__':
    """[running server]
    """
    app.run(port=8000, debug=True)
