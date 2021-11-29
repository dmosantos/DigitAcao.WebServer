import os
from flask import Flask
from flask_cors import CORS
from database import db, params

from controllers.UserController import user_bp
from controllers.CourseController import course_bp
from controllers.LessonController import lesson_bp

# App Config
app = Flask(__name__)
app.secret_key = 'DigitAção'
CORS(app)

# MySql Config
app.config[params.MYSQL_HOST] = "tw7rbs8cuouf.us-east-1.psdb.cloud"
app.config[params.MYSQL_USER] = "1376q1bawnyg"
app.config[params.MYSQL_PASSWORD] = "pscale_pw_x2voHGr722sBcfcnlOP00QUgOWuNqYTF1P8izJwaHBg"
app.config[params.MYSQL_DATABASE] = "digitacao"
app.config[params.MYSQL_SSL_VERIFY_IDENTITY] = True
app.config[params.MYSQL_SSL_CA] = os.path.dirname(os.path.abspath(__file__)) + '/config/ca-cert.pem'

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