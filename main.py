from tkinter import *
from crud_operations import *

def add_course_gui():
    def submit():
        course_name = entry_course_name.get()
        content = entry_description.get()
        duration = int(entry_duration.get())
        add_course(course_name, content, duration)
        top.destroy()

    top = Toplevel()
    top.title("Add Course")

    Label(top, text="Course Name").grid(row=0, column=0)
    entry_course_name = Entry(top)
    entry_course_name.grid(row=0, column=1)

    Label(top, text="Content").grid(row=1, column=0)
    entry_description = Entry(top)
    entry_description.grid(row=1, column=1)

    Label(top, text="Duration").grid(row=2, column=0)
    entry_duration = Entry(top)
    entry_duration.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def update_course_gui():
    def submit():
        cid = int(entry_cid.get())
        course_name = entry_course_name.get()
        content = entry_description.get()
        duration = entry_duration.get()
        update_course(cid, course_name if course_name else None, content if content else None, int(duration) if duration else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Course")

    Label(top, text="Course ID").grid(row=0, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=0, column=1)

    Label(top, text="Course Name").grid(row=1, column=0)
    entry_course_name = Entry(top)
    entry_course_name.grid(row=1, column=1)

    Label(top, text="Content").grid(row=2, column=0)
    entry_description = Entry(top)
    entry_description.grid(row=2, column=1)

    Label(top, text="Duration").grid(row=3, column=0)
    entry_duration = Entry(top)
    entry_duration.grid(row=3, column=1)

    Button(top, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

def delete_course_gui():
    def submit():
        cid = int(entry_cid.get())
        delete_course(cid)
        top.destroy()

    top = Toplevel()
    top.title("Delete Course")

    Label(top, text="Course ID").grid(row=0, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_courses_gui():
    display_courses()

# Similarly define GUI functions for other CRUD operations
def add_instructor_gui():
    def submit():
        iname = entry_iname.get()
        email = entry_email.get()
        add_instructor(iname, email)
        top.destroy()

    top = Toplevel()
    top.title("Add Instructor")

    Label(top, text="Instructor Name").grid(row=0, column=0)
    entry_iname = Entry(top)
    entry_iname.grid(row=0, column=1)

    Label(top, text="Email").grid(row=1, column=0)
    entry_email = Entry(top)
    entry_email.grid(row=1, column=1)

    Button(top, text="Submit", command=submit).grid(row=2, column=0, columnspan=2)

def update_instructor_gui():
    def submit():
        instructor_id = int(entry_instructor_id.get())
        iname = entry_iname.get()
        email = entry_email.get()
        update_instructor(instructor_id, iname if iname else None, email if email else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Instructor")

    Label(top, text="Instructor ID").grid(row=0, column=0)
    entry_instructor_id = Entry(top)
    entry_instructor_id.grid(row=0, column=1)

    Label(top, text="Instructor Name").grid(row=1, column=0)
    entry_iname = Entry(top)
    entry_iname.grid(row=1, column=1)

    Label(top, text="Email").grid(row=2, column=0)
    entry_email = Entry(top)
    entry_email.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def delete_instructor_gui():
    def submit():
        instructor_id = int(entry_instructor_id.get())
        delete_instructor(instructor_id)
        top.destroy()

    top = Toplevel()
    top.title("Delete Instructor")

    Label(top, text="Instructor ID").grid(row=0, column=0)
    entry_instructor_id = Entry(top)
    entry_instructor_id.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_instructors_gui():
    display_instructors()

def add_student_gui():
    def submit():
        student_name = entry_student_name.get()
        email = entry_email.get()
        add_student(student_name, email)
        top.destroy()

    top = Toplevel()
    top.title("Add Student")

    Label(top, text="Student Name").grid(row=0, column=0)
    entry_student_name = Entry(top)
    entry_student_name.grid(row=0, column=1)

    Label(top, text="Email").grid(row=1, column=0)
    entry_email = Entry(top)
    entry_email.grid(row=1, column=1)

    Button(top, text="Submit", command=submit).grid(row=2, column=0, columnspan=2)

def update_student_gui():
    def submit():
        sid = int(entry_sid.get())
        student_name = entry_student_name.get()
        email = entry_email.get()
        update_student(sid, student_name if student_name else None, email if email else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Student")

    Label(top, text="Student ID").grid(row=0, column=0)
    entry_sid = Entry(top)
    entry_sid.grid(row=0, column=1)

    Label(top, text="Student Name").grid(row=1, column=0)
    entry_student_name = Entry(top)
    entry_student_name.grid(row=1, column=1)

    Label(top, text="Email").grid(row=2, column=0)
    entry_email = Entry(top)
    entry_email.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def delete_student_gui():
    def submit():
        sid = int(entry_sid.get())
        delete_student(sid)
        top.destroy()

    top = Toplevel()
    top.title("Delete Student")

    Label(top, text="Student ID").grid(row=0, column=0)
    entry_sid = Entry(top)
    entry_sid.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_students_gui():
    display_students()

def add_enrollment_gui():
    def submit():
        sid = int(entry_sid.get())
        cid = int(entry_cid.get())
        edate = entry_edate.get()
        add_enrollment(sid, cid, edate)
        top.destroy()

    top = Toplevel()
    top.title("Add Enrollment")

    Label(top, text="Student ID").grid(row=0, column=0)
    entry_sid = Entry(top)
    entry_sid.grid(row=0, column=1)

    Label(top, text="Course ID").grid(row=1, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=1, column=1)

    Label(top, text="Enrollment Date").grid(row=2, column=0)
    entry_edate = Entry(top)
    entry_edate.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def update_enrollment_gui():
    def submit():
        eid = int(entry_eid.get())
        sid = entry_sid.get()
        cid = entry_cid.get()
        edate = entry_edate.get()
        update_enrollment(eid, int(sid) if sid else None, int(cid) if cid else None, edate if edate else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Enrollment")

    Label(top, text="Enrollment ID").grid(row=0, column=0)
    entry_eid = Entry(top)
    entry_eid.grid(row=0, column=1)

    Label(top, text="Student ID").grid(row=1, column=0)
    entry_sid = Entry(top)
    entry_sid.grid(row=1, column=1)

    Label(top, text="Course ID").grid(row=2, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=2, column=1)

    Label(top, text="Enrollment Date").grid(row=3, column=0)
    entry_edate = Entry(top)
    entry_edate.grid(row=3, column=1)

    Button(top, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

def delete_enrollment_gui():
    def submit():
        eid = int(entry_eid.get())
        delete_enrollment(eid)
        top.destroy()

    top = Toplevel()
    top.title("Delete Enrollment")

    Label(top, text="Enrollment ID").grid(row=0, column=0)
    entry_eid = Entry(top)
    entry_eid.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_enrollments_gui():
    display_enrollments()

def add_assessment_gui():
    def submit():
        cid = int(entry_cid.get())
        aname = entry_aname.get()
        duedate = entry_duedate.get()
        add_assessment(cid, aname, duedate)
        top.destroy()

    top = Toplevel()
    top.title("Add Assessment")

    Label(top, text="Course ID").grid(row=0, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=0, column=1)

    Label(top, text="Assessment Name").grid(row=1, column=0)
    entry_aname = Entry(top)
    entry_aname.grid(row=1, column=1)

    Label(top, text="Due Date").grid(row=2, column=0)
    entry_duedate = Entry(top)
    entry_duedate.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def update_assessment_gui():
    def submit():
        aid = int(entry_aid.get())
        cid = entry_cid.get()
        aname = entry_aname.get()
        duedate = entry_duedate.get()
        update_assessment(aid, int(cid) if cid else None, aname if aname else None, duedate if duedate else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Assessment")

    Label(top, text="Assessment ID").grid(row=0, column=0)
    entry_aid = Entry(top)
    entry_aid.grid(row=0, column=1)

    Label(top, text="Course ID").grid(row=1, column=0)
    entry_cid = Entry(top)
    entry_cid.grid(row=1, column=1)

    Label(top, text="Assessment Name").grid(row=2, column=0)
    entry_aname = Entry(top)
    entry_aname.grid(row=2, column=1)

    Label(top, text="Due Date").grid(row=3, column=0)
    entry_duedate = Entry(top)
    entry_duedate.grid(row=3, column=1)

    Button(top, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

def delete_assessment_gui():
    def submit():
        aid = int(entry_aid.get())
        delete_assessment(aid)
        top.destroy()

    top = Toplevel()
    top.title("Delete Assessment")

    Label(top, text="Assessment ID").grid(row=0, column=0)
    entry_aid = Entry(top)
    entry_aid.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_assessments_gui():
    display_assessments()

def add_grade_gui():
    def submit():
        eid = int(entry_eid.get())
        aid = int(entry_aid.get())
        grade = entry_grade.get()
        add_grade(eid, aid, grade)
        top.destroy()

    top = Toplevel()
    top.title("Add Grade")

    Label(top, text="Assessment ID").grid(row=0, column=0)
    entry_eid = Entry(top)
    entry_eid.grid(row=0, column=1)

    Label(top, text="Student ID").grid(row=1, column=0)
    entry_aid = Entry(top)
    entry_aid.grid(row=1, column=1)

    Label(top, text="Grade").grid(row=2, column=0)
    entry_grade = Entry(top)
    entry_grade.grid(row=2, column=1)

    Button(top, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def update_grade_gui():
    def submit():
        gid = int(entry_gid.get())
        eid = entry_eid.get()
        aid = entry_aid.get()
        grade = entry_grade.get()
        update_grade(gid, int(eid) if eid else None, int(aid) if aid else None, grade if grade else None)
        top.destroy()

    top = Toplevel()
    top.title("Update Grade")

    Label(top, text="Grade ID").grid(row=0, column=0)
    entry_gid = Entry(top)
    entry_gid.grid(row=0, column=1)

    Label(top, text="Assessment ID").grid(row=1, column=0)
    entry_eid = Entry(top)
    entry_eid.grid(row=1, column=1)

    Label(top, text="Student ID").grid(row=2, column=0)
    entry_aid = Entry(top)
    entry_aid.grid(row=2, column=1)

    Label(top, text="Grade").grid(row=3, column=0)
    entry_grade = Entry(top)
    entry_grade.grid(row=3, column=1)

    Button(top, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

def delete_grade_gui():
    def submit():
        gid = int(entry_gid.get())
        delete_grade(gid)
        top.destroy()

    top = Toplevel()
    top.title("Delete Grade")

    Label(top, text="Grade ID").grid(row=0, column=0)
    entry_gid = Entry(top)
    entry_gid.grid(row=0, column=1)

    Button(top, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def display_grades_gui():
    display_grades()

# Main GUI window
root = Tk()
root.title("EduSchema Management System")

# Courses
Label(root, text="Courses").grid(row=0, column=0, columnspan=2)
Button(root, text="Add Course", command=add_course_gui).grid(row=1, column=0)
Button(root, text="Update Course", command=update_course_gui).grid(row=1, column=1)
Button(root, text="Delete Course", command=delete_course_gui).grid(row=2, column=0)
Button(root, text="Display Courses", command=display_courses_gui).grid(row=2, column=1)

# Instructors
Label(root, text="Instructors").grid(row=3, column=0, columnspan=2)
Button(root, text="Add Instructor", command=add_instructor_gui).grid(row=4, column=0)
Button(root, text="Update Instructor", command=update_instructor_gui).grid(row=4, column=1)
Button(root, text="Delete Instructor", command=delete_instructor_gui).grid(row=5, column=0)
Button(root, text="Display Instructors", command=display_instructors_gui).grid(row=5, column=1)

# Students
Label(root, text="Students").grid(row=6, column=0, columnspan=2)
Button(root, text="Add Student", command=add_student_gui).grid(row=7, column=0)
Button(root, text="Update Student", command=update_student_gui).grid(row=7, column=1)
Button(root, text="Delete Student", command=delete_student_gui).grid(row=8, column=0)
Button(root, text="Display Students", command=display_students_gui).grid(row=8, column=1)

# Enrollments
Label(root, text="Enrollments").grid(row=9, column=0, columnspan=2)
Button(root, text="Add Enrollment", command=add_enrollment_gui).grid(row=10, column=0)
Button(root, text="Update Enrollment", command=update_enrollment_gui).grid(row=10, column=1)
Button(root, text="Delete Enrollment", command=delete_enrollment_gui).grid(row=11, column=0)
Button(root, text="Display Enrollments", command=display_enrollments_gui).grid(row=11, column=1)

# Assessments
Label(root, text="Assessments").grid(row=12, column=0, columnspan=2)
Button(root, text="Add Assessment", command=add_assessment_gui).grid(row=13, column=0)
Button(root, text="Update Assessment", command=update_assessment_gui).grid(row=13, column=1)
Button(root, text="Delete Assessment", command=delete_assessment_gui).grid(row=14, column=0)
Button(root, text="Display Assessments", command=display_assessments_gui).grid(row=14, column=1)

# Grades
Label(root, text="Grades").grid(row=15, column=0, columnspan=2)
Button(root, text="Add Grade", command=add_grade_gui).grid(row=16, column=0)
Button(root, text="Update Grade", command=update_grade_gui).grid(row=16, column=1)
Button(root, text="Delete Grade", command=delete_grade_gui).grid(row=17, column=0)
Button(root, text="Display Grades", command=display_grades_gui).grid(row=17, column=1)

root.mainloop()
