from functools import wraps

from flask import Flask, session, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'
app.secret_key = 'sdfh2309rsac'   # needed to use session
db = SQLAlchemy(app)


class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.Column(db.String(80), nullable=False)
    modified = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ccy = db.Column(db.String(3), nullable=False)
    notes = db.Column(db.String(200), default='')

    def __repr__(self):
        return f'Transaction {self.id}: {self.ccy} {self.amount} from {self.sender}'


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return view(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper


@app.route('/')
@login_required
def index():
    return redirect('/transactions')


@app.route('/transactions')
@login_required
def transactions_page():
    transactions = Transaction.query.all()
    return render_template("transactions.html", transactions=transactions)


@app.route('/transactions/<int:id>', methods=['GET', 'POST'])
@login_required
def details_page(id):
    transaction = Transaction.query.get_or_404(id)
    if request.method == 'POST':
        transaction.notes = request.form['note']
        db.session.commit()
    return render_template("details.html", transaction=transaction)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user = request.form['login']
        session['user'] = user
        return redirect('/')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout_page():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
