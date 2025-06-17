from app import db
from datetime import datetime

class Due(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), default='Pending')
