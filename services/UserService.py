from database import db
from models import ResponseMessage

# Faz o login
def login(user):

    cursor = db.connection.cursor()
    cursor.execute('SELECT UserId, Email, FirstName, LastName, IsAdministrator FROM User WHERE Email=%s AND Password=%s', (user.email, user.password))
    
    row = cursor.fetchone()

    if row == None:
        return ResponseMessage(errors=['Email e/ou senha não localizado'])

    user.userId = row[0]
    user.email = row[1]
    user.firstName = row[2]
    user.lastName = row[3]
    user.isAdministrator = row[4]

    response = ResponseMessage(data=user.__dict__)

    return response
