from database import db
from models import ResponseMessage, Lesson

# Recupera todos Lessons por CourseId
def get_all(courseId):

    cursor = db.connection.cursor()

    query = '''
        SELECT
            L.LessonId,
            L.CourseId,
            LV.LessonLevelName,
            L.LessonContent,
            L.Order
        FROM
            Lesson L
            JOIN LessonLevel LV ON LV.LessonLevelId = L.LessonLevelId
        WHERE
            L.CourseId = %s
        ORDER BY
            L.Order;
    '''
    data = (courseId, )

    cursor.execute(query, data)

    rows = cursor.fetchall()

    if rows == None:
        return ResponseMessage(errors=['Nenhum registro localizado'])
    
    result = list()
    
    for row in rows:
        result.append(Lesson(
            lessonId=row[0],
            courseId=row[1],
            lessonLevelName=row[2],
            lessonContent=row[3],
            order=row[4]
        ).__dict__)

    response = ResponseMessage(data=result)

    return response


# Recupera Lesson por LessonId
def get(lessonId):

    cursor = db.connection.cursor()

    query = '''
        SELECT
            L.LessonId,
            L.CourseId,
            LV.LessonLevelName,
            L.LessonContent,
            L.Order,
            (
                SELECT
                    NL.LessonId
                FROM
                    Lesson NL
                WHERE
                    NL.CourseId = L.CourseId
                    AND NL.Order > L.Order
                ORDER BY
                    NL.Order
                LIMIT 0, 1
            ) NextLessonId
        FROM
            Lesson L
            JOIN LessonLevel LV ON LV.LessonLevelId = L.LessonLevelId
        WHERE
            L.LessonId = %s;
    '''
    data = (lessonId, )

    cursor.execute(query, data)

    row = cursor.fetchone()

    if row == None:
        return ResponseMessage(errors=['Nenhum registro localizado'])

    result = Lesson(
        lessonId=row[0],
        courseId=row[1],
        lessonLevelName=row[2],
        lessonContent=row[3],
        order=row[4],
        nextLessonId=row[5]
    ).__dict__

    response = ResponseMessage(data=result)

    return response
