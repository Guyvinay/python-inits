from flask import Blueprint, jsonify
from flask import request

product_bp = Blueprint("product_bp", __name__)

@product_bp.route('/users', methods=['GET'])
def get_users():
    # Logic to return a list of users
    return "Vinay kumar singh"

