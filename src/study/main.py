from pathlib import Path

from study.data.csv import CSV
from study.data.school import School
from study.data.course import Course
from study.data.result import Result
from study.data.student import Student
from study.data.teacher import Teacher

def process():
    # create the CSV
    csv = CSV(str(Path(__file__).resolve().with_name("student_performance.csv")))

    data = csv.read_csv()

    schools = []
    students = []
    teachers = []
    courses = []
    results = []

    for row in data:
        # create new school
        school = School(
            row["school_id"],
            row["school_name"],
            row["school_city"]
        )

        schools.append(school)

        # create new student
        student = Student(
            row["student_id"],
            row["student_name"],
            row["gender"],
            int(row["age"])
        )

        students.append(student)

        # create new teacher
        teacher = Teacher(
            row["teacher_id"],
            row["teacher_name"]
        )

        teachers.append(teacher)

        # create new course
        course = Course(
            row["course_id"],
            row["course_name"]
        )

        courses.append(course)

        # create new result
        result = Result(
            int(row["record_id"]),
            row["student_id"],
            float(row["study_hours_week"]),
            int(row["absences"]),
            float(row["final_grade"])
        )

        results.append(result)

    for school in schools:
        print(f"School ID: {school.get_school_id()}, Name: {school.get_school_name()}, City: {school.get_school_city()}")