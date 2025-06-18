from flask import Blueprint, request, jsonify
from app import db
from app.models.customer import Customer

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'phone': c.phone} for c in customers])

@customer_bp.route('/', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(name=data['name'], phone=data['phone'], email=data.get('email'))
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer added successfully'})

@customer_bp.route('/', methods=['GET'])
def list_customers():   
    customers = Customer.query.all()
    return jsonify([
        {'id': c.id, 'name': c.name, 'phone': c.phone, 'email': c.email}
        for c in customers
    ])
