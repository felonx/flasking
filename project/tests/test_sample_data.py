import datetime
from ..app import Transaction, db
from ..sample_data import transaction_generator, names, ccys, _random_date, populate_data_to_db


def test_generator():
    """make sure transaction generator builds proper transactions"""
    tg = transaction_generator(5)
    count = 0
    for transaction in tg:
        assert isinstance(transaction, Transaction)
        assert transaction.sender in names
        assert transaction.receiver in names
        assert transaction.ccy in ccys
        assert 0 < transaction.amount < 1000000
        assert datetime.datetime(2000, 1, 1, 0, 0, 0) < transaction.date < datetime.datetime.now()
        count += 1
    assert count == 5


def test_random_date():
    """test if random_date returns correct date"""
    date = _random_date()
    assert isinstance(date, datetime.datetime)
    assert datetime.datetime(2000, 1, 1, 0, 0, 0) < date < datetime.datetime.now()


def test_populate_to_db(test_app):
    """check if our function to load data to test.db works ok"""
    populate_data_to_db(db, 5, drop=True)
    query = Transaction.query.all()
    assert len(query) == 5
    populate_data_to_db(db, 5, drop=False)
    query = Transaction.query.all()
    assert len(query) == 10
    populate_data_to_db(db, 3, drop=True)
    query = Transaction.query.all()
    assert len(query) == 3
