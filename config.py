import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = 'loo@*aQutDaWMcVEKiFJ$0M9WE!EYgiNUVaNCMiYtlq4pDC3O3'

# MySql Config
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
MYSQL_SSL_VERIFY_IDENTITY = True
MYSQL_SSL_CA = os.path.dirname(os.path.abspath(__file__)) + '/config/ca-cert.pem'