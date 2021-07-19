from project.app import db


class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.COlumn(db.String(80), nullable=False)
    modified = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ccy = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f'Transaction {self.id}: {self.ccy} {self.amount} from {self.sender}'

