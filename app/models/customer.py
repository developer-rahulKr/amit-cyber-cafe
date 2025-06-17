from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), nullable=True)
    dues = db.relationship('Due', backref='customer', lazy=True)
