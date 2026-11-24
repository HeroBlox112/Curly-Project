from pathlib import Path

from study.data.school import School
from study.data.result import Result

CSV_PATH = str(Path(__file__).resolve().with_name("student_performance.csv"))

def process():
    try:
        schools = School.load_from_csv(CSV_PATH)
    except FileNotFoundError:
        print("The CSV file was not found.")
        return
    except ValueError as error:
        print(error)
        return

    for school in schools:
        print(school)


def next_record_id(schools):
    ids = [r.get_record_id() for school in schools for r in school.get_results()]
    return max(ids, default=0) + 1



def add_new_result(schools):
    student_id = input("Student ID: ").strip().upper()
    school, student = None, None
    for s in schools:
        student = s.find_student(student_id)
        if student is not None:
            school = s
            break
    if student is None:
        print("No student with this ID.")
        return

    course = school.find_course(input("Course ID: "))
    if course is None:
        print("This course does not exist in the student's school.")
        return

    try:
        hours = float(input("Study hours per week: "))
        absences = int(input("Absences: "))
        grade = float(input("Final grade: "))
        result = Result(next_record_id(schools), student.get_student_id(), hours, absences, grade)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    student.add_result(result)
    course.add_result(result)
    print(f"Result added: {result}")


def remove_existing_result(schools):
    try:
        record_id = int(input("Record ID to remove: "))
    except ValueError:
        print("Record ID must be a whole number.")
        return

    for school in schools:
        for result in school.get_results():
            if result.get_record_id() == record_id:
                school.remove_result(result)
                print(f"Result {record_id} removed.")
                return
    print("No result with this record ID.")

    