from flask import Blueprint, request, jsonify, json
import services.LessonService as lesson_service
from models import User

lesson_bp = Blueprint('lesson_bp', __name__)


@lesson_bp.route('/', methods=["GET"])
def get_all():

    courseId = request.args.get('courseId')

    responseMessage = lesson_service.get_all(courseId)

    return jsonify(responseMessage.__dict__)


@lesson_bp.route('/<lessonId>', methods=["GET"])
def get(lessonId):

    responseMessage = lesson_service.get(lessonId)

    return jsonify(responseMessage.__dict__)
