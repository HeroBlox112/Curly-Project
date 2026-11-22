class Student:
    def __init__(self, student_id, student_name, gender, age):
        self.student_id = student_id
        self.student_name = self.validate_name(student_name)
        self.gender = self.validate_gender(gender)
        self.age = self.validate_age(age)

    # validate the provided name is not empty, contains only letters and spaces, and is between 2 and 50 characters long
    @staticmethod
    def validate_name(name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        # check if all are letters
        elif not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces.")
        elif len(name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        elif len(name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        elif len(name.split()) != 2:
            raise ValueError("Name must contain first and last name")
        else:
            return name.strip()

    # validate the provided gender is either "M" (male) or "F" (female)
    @staticmethod
    def validate_gender(gender):
        if gender not in ["M", "F"]:
            raise ValueError("Gender must be 'M' or 'F'.")
        else:
            return gender

    # validate the provided age is an integer between 14 and 18
    @staticmethod
    def validate_age(age):
        # check if age is of type int
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        elif age < 14 or age > 18:
            raise ValueError("Age must be between 14 and 18.")
        else:
            return age

    # getters
    def get_student_id(self):
        return self.student_id

    def get_student_name(self):
        return self.student_name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
