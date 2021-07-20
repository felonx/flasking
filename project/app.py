from functools import wraps

from flask import Flask, session, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///transactions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sdfh2309rsac'

db = SQLAlchemy(app)


class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ccy = db.Column(db.String(3), nullable=False)
    notes = db.Column(db.String(200), default='')

    def __repr__(self):
        return f'Transaction {self.id}: {self.ccy} {self.amount} from {self.sender}'


def login_required(page):
    """decorator for page functions to redirect unlogged user to login page"""
    @wraps(page)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return page(*args, **kwargs)
        else:
            return redirect('/login')
    return wrap


@app.route('/')
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
        try:
            transaction.notes = request.form['note']
            db.session.commit()
            flash('notes updated')
        except Exception as e:
            db.session.rollback()
            flash(f'update failed: {e}', 'error')
    return render_template("details.html", transaction=transaction)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user = request.form['login']
        session['user'] = user
        flash('login successful')
        return redirect('/')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout_page():
    session.pop('user', None)
    flash('logout successful')
    return redirect('/')


@app.route('/load')
@login_required
def load_data():
    try:
        # importing here to avoid circular import in top of module. will need refactoring of models/init to make it nice
        from project.sample_data import populate_data_to_db
        populate_data_to_db(db, 20)
        flash('20 records of data added')
    except Exception as e:
        flash(f'there was an issue uploading data: {e}', 'error')
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
