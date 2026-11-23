from study.data.csv import CSV
from study.data.student import Student
from study.data.course import Course
from study.data.teacher import Teacher
from study.data.result import Result

class School:
    def __init__(self, school_id, school_name, school_city):
        self.set_school_ID(school_id)
        self.set_school_name(school_name)
        self.set_school_city(school_city)
        self.__students = []
        self.__courses = []
        self.__teachers = []
        #de ce am pus listele astea aici? 
        #de ce nu am si pentru city, gen de ce am doar validate text?

    @staticmethod
    def __validate_school_id(self, school_id):
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


    # setters

    def set_school_id(self, school_id):
         self.__school_id = self.__validate_school_id(school_id)

    def set_school_name(self, school_name):
        self.__school_name = self.__validate_text(school_name, "School name")
        return self.__school_name

    def set_school_city(self, school_city):
        self.__school_city = self.__validate_text(school_city, "School city")
        return self.__school_city
    
    #getters

    def get_stundent(self):
        return list(self.__students)

    def get_courses(self):
         return list(self.__courses)
    def get_teachers(self):
         return list(self.__teachers)
    def get_results(self):
        results = []
        for student in self.__students:
             results.extend(student.get_results_())
        return results
