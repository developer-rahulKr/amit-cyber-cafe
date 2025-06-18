from flask import Blueprint, request, jsonify
from app import db
from app.models.due import Due
from app.models.customer import Customer
from datetime import datetime

due_bp = Blueprint('due', __name__)

@due_bp.route('/', methods=['GET'])
def get_dues():
    dues = Due.query.all()
    result = []
    for due in dues:
        customer = Customer.query.get(due.customer_id)
        result.append({
            'id': due.id,
            'amount': due.amount,
            'due_date': due.due_date.strftime('%Y-%m-%d'),
            'status': due.status,
            'customer_id': due.customer_id,
            'customer_name': customer.name if customer else 'Unknown'
        })
    return jsonify(result)

@due_bp.route('/', methods=['POST'])
def create_due():
    data = request.get_json()
    new_due = Due(
        customer_id=data['customer_id'],
        amount=data['amount'],
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d'),
        status='Pending'
    )
    db.session.add(new_due)
    db.session.commit()
    return jsonify({'message': 'Due created successfully'}), 201

# Existing routes
@due_bp.route('/<int:id>', methods=['GET'])
def get_due(id):
    due = Due.query.get_or_404(id)
    return jsonify({
        'id': due.id,
        'amount': due.amount,
        'due_date': due.due_date.strftime('%Y-%m-%d'),
    })

@due_bp.route('/<int:id>', methods=['PUT'])
def update_due(id):
    data = request.get_json()
    due = Due.query.get_or_404(id)
    due.amount = data['amount']
    due.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d')
    db.session.commit()
    return jsonify({'message': 'Due updated successfully'})

@due_bp.route('/<int:id>', methods=['DELETE'])
def delete_due(id):
    due = Due.query.get_or_404(id)
    db.session.delete(due)
    db.session.commit()
    return jsonify({'message': 'Due deleted successfully'})
