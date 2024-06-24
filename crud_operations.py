from database import create_connection, close_connection

# CRUD operations for Courses
def add_course(course_name, description, duration):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Courses (CourseName, Content, Duration) VALUES (%s, %s, %s)"
    data = (course_name, description, duration)
    cursor.execute(query, data)
    connection.commit()
    print("Course added successfully")
    close_connection(connection)

def update_course(cid, course_name=None, description=None, duration=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Courses SET "
    data = []
    if course_name:
        query += "CourseName = %s, "
        data.append(course_name)
    if description:
        query += "Content = %s, "
        data.append(description)
    if duration:
        query += "Duration = %s, "
        data.append(duration)
    query = query.rstrip(", ")
    query += " WHERE CID = %s"
    data.append(cid)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Course updated successfully")
    close_connection(connection)

def delete_course(cid):
    connection = create_connection()
    cursor = connection.cursor()

    # Archive the course before deleting
    archive_query = "INSERT INTO Courses_Archive (CID, CourseName, Content, Duration) SELECT CID, CourseName, Content, Duration FROM Courses WHERE CID = %s"
    cursor.execute(archive_query, (cid,))

    # Delete the course
    delete_query = "DELETE FROM Courses WHERE CID = %s"
    cursor.execute(delete_query, (cid,))
    connection.commit()
    print("Course deleted successfully")
    close_connection(connection)

def display_courses():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Courses"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)

# CRUD operations for Instructors
def add_instructor(iname, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Instructors (Iname, email) VALUES (%s, %s)"
    data = (iname, email)
    cursor.execute(query, data)
    connection.commit()
    print("Instructor added successfully")
    close_connection(connection)

def update_instructor(instructor_id, iname=None, email=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Instructors SET "
    data = []
    if iname:
        query += "Iname = %s, "
        data.append(iname)
    if email:
        query += "email = %s, "
        data.append(email)
    query = query.rstrip(", ")
    query += " WHERE InstructorID = %s"
    data.append(instructor_id)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Instructor updated successfully")
    close_connection(connection)

def delete_instructor(instructor_id):
    connection = create_connection()
    cursor = connection.cursor()

    # Archive the instructor before deleting
    archive_query = "INSERT INTO Instructors_Archive (InstructorID, Iname, email) SELECT InstructorID, Iname, email FROM Instructors WHERE InstructorID = %s"
    cursor.execute(archive_query, (instructor_id,))

    # Delete the instructor
    delete_query = "DELETE FROM Instructors WHERE InstructorID = %s"
    cursor.execute(delete_query, (instructor_id,))
    connection.commit()
    print("Instructor deleted successfully")
    close_connection(connection)

def display_instructors():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Instructors"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)

# CRUD operations for Students
def add_student(student_name, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Students (StudentName, email) VALUES (%s, %s)"
    data = (student_name, email)
    cursor.execute(query, data)
    connection.commit()
    print("Student added successfully")
    close_connection(connection)

def update_student(sid, student_name=None, email=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Students SET "
    data = []
    if student_name:
        query += "StudentName = %s, "
        data.append(student_name)
    if email:
        query += "email = %s, "
        data.append(email)
    query = query.rstrip(", ")
    query += " WHERE SID = %s"
    data.append(sid)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Student updated successfully")
    close_connection(connection)

def delete_student(sid):
    connection = create_connection()
    cursor = connection.cursor()

    # Archive the student before deleting
    archive_query = "INSERT INTO Students_Archive (SID, SName, email) SELECT SID, StudentName, email FROM Students WHERE SID = %s"
    cursor.execute(archive_query, (sid,))

    # Delete the student
    delete_query = "DELETE FROM Students WHERE SID = %s"
    cursor.execute(delete_query, (sid,))
    connection.commit()
    print("Student deleted successfully")
    close_connection(connection)

def display_students():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Students"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)

# CRUD operations for Enrollments
def add_enrollment(sid, cid, edate):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Enrollments (SID, CID, EDate) VALUES (%s, %s, %s)"
    data = (sid, cid, edate)
    cursor.execute(query, data)
    connection.commit()
    print("Enrollment added successfully")
    close_connection(connection)

def update_enrollment(eid, sid=None, cid=None, edate=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Enrollments SET "
    data = []
    if sid:
        query += "SID = %s, "
        data.append(sid)
    if cid:
        query += "CID = %s, "
        data.append(cid)
    if edate:
        query += "EDate = %s, "
        data.append(edate)
    query = query.rstrip(", ")
    query += " WHERE EID = %s"
    data.append(eid)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Enrollment updated successfully")
    close_connection(connection)

def delete_enrollment(eid):
    connection = create_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM Enrollments WHERE EID = %s"
    cursor.execute(delete_query, (eid,))
    connection.commit()
    print("Enrollment deleted successfully")
    close_connection(connection)

def display_enrollments():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Enrollments"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)

# CRUD operations for Assessments
def add_assessment(cid, aname, duedate):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Assessments (CID, AName, DueDate) VALUES (%s, %s, %s)"
    data = (cid, aname, duedate)
    cursor.execute(query, data)
    connection.commit()
    print("Assessment added successfully")
    close_connection(connection)

def update_assessment(aid, cid=None, aname=None, duedate=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Assessments SET "
    data = []
    if cid:
        query += "CID = %s, "
        data.append(cid)
    if aname:
        query += "AName = %s, "
        data.append(aname)
    if duedate:
        query += "DueDate = %s, "
        data.append(duedate)
    query = query.rstrip(", ")
    query += " WHERE AID = %s"
    data.append(aid)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Assessment updated successfully")
    close_connection(connection)

def delete_assessment(aid):
    connection = create_connection()
    cursor = connection.cursor()

    # Archive the assessment before deleting
    archive_query = "INSERT INTO Assessments_Archive (AID, CID, AssessmentName, DueDate) SELECT AID, CID, AName, DueDate FROM Assessments WHERE AID = %s"
    cursor.execute(archive_query, (aid,))

    # Delete the assessment
    delete_query = "DELETE FROM Assessments WHERE AID = %s"
    cursor.execute(delete_query, (aid,))
    connection.commit()
    print("Assessment deleted successfully")
    close_connection(connection)

def display_assessments():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Assessments"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)

# CRUD operations for Grades
def add_grade(eid, aid, grade):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Grades (AID, SID, Grade) VALUES (%s, %s, %s)"
    data = (eid, aid, grade)
    cursor.execute(query, data)
    connection.commit()
    print("Grade added successfully")
    close_connection(connection)

def update_grade(gid, eid=None, aid=None, grade=None):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Grades SET "
    data = []
    if eid:
        query += "AID = %s, "
        data.append(eid)
    if aid:
        query += "SID = %s, "
        data.append(aid)
    if grade:
        query += "Grade = %s, "
        data.append(grade)
    query = query.rstrip(", ")
    query += " WHERE GID = %s"
    data.append(gid)
    cursor.execute(query, tuple(data))
    connection.commit()
    print("Grade updated successfully")
    close_connection(connection)

def delete_grade(gid):
    connection = create_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM Grades WHERE GID = %s"
    cursor.execute(delete_query, (gid,))
    connection.commit()
    print("Grade deleted successfully")
    close_connection(connection)

def display_grades():
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Grades"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    close_connection(connection)
