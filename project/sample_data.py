"""quick script to generate some transactions data"""


import random
from datetime import datetime, timedelta

from project.app import Transaction

names = ['John Smith', 'Mark Kowalski', 'Abraham Lincoln', 'Ronaldo', 'Romario', 'Bebeto']
ccys = [x.upper() for x in ['usd', 'eur', 'gbp', 'pln', 'jpy', 'cad', 'aud', 'nzd', 'krw', 'sek', 'hkd']]

# drop duplicates
names = list(set(names))
ccys = list(set(ccys))


def transaction_generator(n=10):

    for _ in range(n):
        date = _random_date()
        sender, receiver = random.sample(names, 2)
        amount = round(random.uniform(0, 1000000), 2)
        ccy = random.choice(ccys)

        yield Transaction(date=date, sender=sender, receiver=receiver, amount=amount, ccy=ccy)


def _random_date() -> datetime:
    """returns a random datetime between 1/1/2000 0:00 and now ("naive" timezone)"""
    start = datetime(2000, 1, 1, 0, 0, 0)
    end = datetime.now()
    total_seconds = int((end-start).total_seconds())
    return start + timedelta(seconds=random.randint(0, total_seconds))


def populate_data_to_db(db, n=10, drop=True):

    if drop:
        db.session.close()
        db.drop_all()

    db.create_all()

    for transaction in transaction_generator(n):
        db.session.add(transaction)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise


if __name__ == '__main__':
    from project.app import db
    populate_data_to_db(db, 20)
