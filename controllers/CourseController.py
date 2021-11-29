from flask import Blueprint, request, jsonify, json
import services.CourseService as course_service
from models import User

course_bp = Blueprint('course_bp', __name__)

@course_bp.route('/', methods=["GET"])
def get_all():

    responseMessage = course_service.get_all()

    return jsonify(responseMessage.__dict__)