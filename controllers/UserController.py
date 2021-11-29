from flask import Blueprint, request, jsonify, json
import services.UserService as user_service
from models import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('', methods=["POST"])
def sign_up():

    json = request.get_json()
    
    user = User(
        firstName=json['firstName'],
        email=json['email'],
        password=json['password']
    )

    response_message = user_service.sign_up(user)

    return jsonify(response_message.__dict__)


@user_bp.route('/login', methods=["POST"])
def login():

    json = request.get_json()
    
    user = User(
        email=json['email'],
        password=json['password']
    )

    response_message = user_service.login(user)

    return jsonify(response_message.__dict__)
