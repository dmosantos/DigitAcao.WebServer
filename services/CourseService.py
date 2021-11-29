from database import db
from models import ResponseMessage, Course

# Faz o login
def get_all():

    cursor = db.connection.cursor()

    query = '''
        SELECT
        	C.CourseId,
        	C.CourseName,
        	CL.CourseLevelName,
            CAST((
                ((
                    SELECT
                        COUNT(*)
                    FROM
                        Lesson L
                        JOIN UserLesson UL ON UL.LessonId = L.LessonId
                    WHERE
                        L.CourseId = C.CourseId
                        AND UL.UserId = 1
                ) / (
                    SELECT
                        COUNT(*)
                    FROM
                        Lesson L
                    WHERE
                        L.CourseId = C.CourseId
                )) * 100
            ) AS SIGNED) AS Progress
        FROM
        	Course C
            JOIN CourseLevel CL ON CL.CourseLevelId = C.CourseLevelId;
    '''

    cursor.execute(query)

    rows = cursor.fetchall()

    if rows == None:
        return ResponseMessage(errors=['Nenhum registro não localizado'])
    
    # fields = map(lambda x: x[0][0].lower() + x[0][1:], cursor.description)
    # result = [dict(zip(fields, row)) for row in rows]

    result = list()
    
    for row in rows:
        result.append(Course(
            courseId=row[0],
            courseName=row[1],
            courseLevelName=row[2],
            progress=row[3]
        ).__dict__)

    response = ResponseMessage(data=result)

    return response
