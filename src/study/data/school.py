from study.data.csv import CSV
from study.data.student import Student
from study.data.course import Course
from study.data.teacher import Teacher
from study.data.result import Result

class School:
    def __init__(self, school_id, school_name, school_city):
        self.set_school_id(school_id)
        self.set_school_name(school_name)
        self.set_school_city(school_city)
        self.__students = []
        self.__courses = []
        self.__teachers = []

    @staticmethod
    def __validate_school_id(school_id):
        if not isinstance(school_id, str) or not school_id.strip():
            raise ValueError("School ID cannot be empty")
        school_id = school_id.strip().upper()
        if not school_id.startswith("SCH"):
            raise ValueError("School Id must start with SCH (ex:SCH01).")
        return school_id

    @staticmethod
    def __validate_text(value, field):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field} cannot be empty.")
        value = value.strip()
        if len(value) < 2:
            raise ValueError(f"{field} must be at least 2 characters long.")
        if len(value) > 100:
            raise ValueError(f"{field} cannot exceed 100 characters.")
        return value

    # getters

    def get_school_id(self):
        return self.__school_id

    def get_school_name(self):
        return self.__school_name

    def get_school_city(self):
        return self.__school_city

    def get_students(self):
        return list(self.__students)

    def get_courses(self):
        return list(self.__courses)

    def get_teachers(self):
        return list(self.__teachers)

    def get_results(self):
        results = []
        for student in self.__students:
            results.extend(student.get_results())
        return results

    # setters

    def set_school_id(self, school_id):
        self.__school_id = self.__validate_school_id(school_id)

    def set_school_name(self, school_name):
        self.__school_name = self.__validate_text(school_name, "School name")

    def set_school_city(self, school_city):
        self.__school_city = self.__validate_text(school_city, "School city")

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be added.")
        if student not in self.__students:
            self.__students.append(student)

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("Only Course objects can be added.")
        if course not in self.__courses:
            self.__courses.append(course)

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Only Teacher objects can be added.")
        if teacher not in self.__teachers:
            self.__teachers.append(teacher)

    def find_student(self, student_id):
        student_id = str(student_id).strip().upper()
        for student in self.__students:
            if student.get_student_id() == student_id:
                return student
        return None

    def find_course(self, course_id):
        course_id = str(course_id).strip().upper()
        for course in self.__courses:
            if course.get_course_id() == course_id:
                return course
        return None

    def remove_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("Only Result objects can be removed")

        student = self.find_student(result.get_student_id())
        if student is None:
            raise ValueError("This result does not belong to a student of this school.")

        course = None
        for c in self.__courses:
            if result in c.get_results():
                course = c
                break
        if course is None:
            raise ValueError("This result is not linked to any course.")

        student.remove_result(result)
        course.remove_result(result)

    def __str__(self):
        return (f"{self.__school_name} ({self.__school_id}), {self.__school_city} - "
                f"{len(self.__students)} students, {len(self.__courses)} courses, "
                f"{len(self.__teachers)} teachers")

    def __eq__(self, other):
        if not isinstance(other, School):
            return NotImplemented
        return self.__school_id == other.get_school_id()

    def __hash__(self):
        return hash(self.__school_id)

    def __len__(self):
        return len(self.__students)

    def __contains__(self, student):
        return student in self.__students

    @staticmethod
    def load_from_csv(path):
        rows = CSV(path).read_csv()

        schools = {}
        students = {}
        teachers = {}
        courses = {}

        for line_number, row in enumerate(rows, start=2):
            try:
                school_id = row["school_id"].strip()
                if school_id not in schools:
                    schools[school_id] = School(school_id, row["school_name"], row["school_city"])
                school = schools[school_id]

                student_id = row["student_id"].strip()
                if student_id not in students:
                    students[student_id] = Student(student_id, row["student_name"],
                                                   row["gender"], int(row["age"]))
                student = students[student_id]

                teacher_id = row["teacher_id"].strip()
                if teacher_id not in teachers:
                    teachers[teacher_id] = Teacher(teacher_id, row["teacher_name"])
                teacher = teachers[teacher_id]

                course_id = row["course_id"].strip()
                if course_id not in courses:
                    courses[course_id] = Course(course_id, row["course_name"])
                    teacher.add_course(courses[course_id])
                course = courses[course_id]

                result = Result(int(row["record_id"]), student_id,
                                float(row["study_hours_week"]),
                                int(row["absences"]),
                                float(row["final_grade"]))
            except (KeyError, ValueError) as error:
                raise ValueError(f"Invalid data on line {line_number} of the CSV: {error}") from error

            school.add_student(student)
            school.add_course(course)
            school.add_teacher(teacher)
            student.add_result(result)
            course.add_result(result)

        return list(schools.values())

    # ---------- Part 2 (Person 4) ----------
