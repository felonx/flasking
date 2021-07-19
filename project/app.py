from flask import Flask, session, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///test.db'
db = SQLAlchemy(app)


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
def transactions():
    return


@app.route('/transactions/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
