import os
from flask import Flask
from flask_cors import CORS
from database import db

from controllers.UserController import user_bp
from controllers.CourseController import course_bp
from controllers.LessonController import lesson_bp

# App Config
app = Flask(__name__)
app.config.from_pyfile('config.py')

cors_config = {
  "origins": ["*"],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ['Content-Type', 'Authorization']
}
CORS(app, resources={r"/*": cors_config})
# CORS(app)

print('teste')
print(app.config['MYSQL_HOST'])

db.init_app(app)

# Controllers
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(course_bp, url_prefix='/course')
app.register_blueprint(lesson_bp, url_prefix='/lesson')

# Index route
@app.route('/', methods=["GET"])
def login():
    return 'DigitAção v1.0.0'

if __name__ == '__main__':
    app.run(debug=True)