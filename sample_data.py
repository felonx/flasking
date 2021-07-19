import random
from datetime import datetime, timedelta
from collections import namedtuple


names = ['John Smith', 'Mark Kowalski', 'Abraham Lincoln', 'Ronaldo']
ccys = [x.upper() for x in ['usd', 'eur', 'gbp', 'pln', 'jpy', 'cad']]


Transaction = namedtuple('transaction', 'modified sender receiver amount ccy')


def _transaction_generator(n=10):
    for _ in range(n):
        modified = _random_date()
        sender, receiver = random.sample(names, 2)
        amount = round(random.uniform(0, 1000000), 2)
        ccy = random.choice(ccys)

        yield Transaction(modified=modified, sender=sender, receiver=receiver, amount=amount, ccy=ccy)


def _random_date() -> datetime:
    """returns a random datetime between 1/1/2000 0:00 and now ("naive" timezone)"""
    start = datetime(2000, 1, 1, 0, 0, 0)
    end = datetime.now()
    total_seconds = int((end-start).total_seconds())
    return start + timedelta(seconds=random.randint(0, total_seconds))


def generate_transactions(n=10):
    trans_generator = _transaction_generator(n)
    return [transaction for transaction in trans_generator]


if __name__ == '__main__':

    tg = _transaction_generator()

    for x in tg:
        print(x)
