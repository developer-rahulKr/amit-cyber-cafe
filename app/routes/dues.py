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
        result.append({
            'id': due.id,
            'customer_name': due.customer.name,
            'amount': due.amount,
            'due_date': due.due_date.strftime('%Y-%m-%d'),
            'status': due.status
        })
    return jsonify(result)

@due_bp.route('/', methods=['POST'])
def add_due():
    data = request.json
    customer_id = data.get('customer_id')
    amount = data.get('amount')
    due_date_str = data.get('due_date')  

    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    except:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

    new_due = Due(customer_id=customer_id, amount=amount, due_date=due_date)
    db.session.add(new_due)
    db.session.commit()

    return jsonify({'message': 'Due added successfully'})
