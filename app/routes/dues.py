from flask import Blueprint

due_bp = Blueprint('due', __name__)

@due_bp.route('/', methods=['GET'])
def get_dues():
    return {"message": "Dues route working"}
