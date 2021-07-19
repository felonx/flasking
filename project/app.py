from flask import Flask, session, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'
db = SQLAlchemy(app)


class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.Column(db.String(80), nullable=False)
    modified = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ccy = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f'Transaction {self.id}: {self.ccy} {self.amount} from {self.sender}'


@app.route('/')
def index():
    return 'i\'m flasking!'


@app.route('/login')
def login():
    return


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return


@app.route('/transactions')
def transactions_page():
    transactions = Transaction.query.all()
    return render_template("transactions.html", transactions=transactions)


@app.route('/transactions/<int:id>')
def details_page(id):
    transaction = Transaction.query.get_or_404(id)
    return render_template("details.html", transaction=transaction)


if __name__ == '__main__':
    app.run(debug=True)
