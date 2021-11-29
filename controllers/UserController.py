from flask import Blueprint, request, jsonify, json
import services.UserService as user_service
from models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/login', methods=["POST"])
def login():

    json = request.get_json()
    
    user = User(
        email=json['email'],
        password=json['password']
    )

    responseMessage = user_service.login(user)

    return jsonify(responseMessage.__dict__)
