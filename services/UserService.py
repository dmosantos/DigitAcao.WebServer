from database import db
from models import ResponseMessage


# Faz o login
def email_exists(email):

    cursor = db.connection.cursor()
    cursor.execute('SELECT UserId FROM User WHERE Email=%s', (email, ))
    
    row = cursor.fetchone()

    return not (row == None)


# Cadastra um novo usuário
def sign_up(user):

    if email_exists(user.email):
        return ResponseMessage(errors=['alreadyRegistered'])

    cursor = db.connection.cursor()
    cursor.execute('INSERT INTO `User` (`FirstName`, `Email`, `Password`) VALUES (%s, %s, %s);', (user.firstName, user.email, user.password))

    user.userId = cursor.lastrowid
    db.connection.commit()

    if user.userId == None or user.userId == 0:
        return ResponseMessage(errors=['error'])
    
    return ResponseMessage(data=user.__dict__)

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

    return ResponseMessage(data=user.__dict__)

