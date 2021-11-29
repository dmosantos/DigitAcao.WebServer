class ResponseMessage:
    def __init__(self, errors=None, data=None):
        self.errors = errors
        self.data = data


class Course:
    def __init__(self, courseId=None, courseName=None, courseLevelName=None, progress=None):
        self.courseId = courseId
        self.courseName = courseName
        self.courseLevelName = courseLevelName
        self.progress = progress

class Lesson:
    def __init__(self, lessonId=None, courseId=None, lessonLevelName=None, lessonContent=None, order=None, nextLessonId=None):
        self.lessonId = lessonId
        self.courseId = courseId
        self.lessonLevelName = lessonLevelName
        self.lessonContent = lessonContent
        self.order = order
        self.nextLessonId = nextLessonId

class User:
    def __init__(self, userId=None, email=None, password=None, firstName=None, lastName=None, insertedIn=None, lastLoginIn=None, isAdministrator=None, activationCode=None):
        self.userId = userId
        self.email = email
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.insertedIn = insertedIn
        self.lastLoginIn = lastLoginIn
        self.isAdministrator = isAdministrator
        self.activationCode = activationCode