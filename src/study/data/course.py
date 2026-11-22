class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = self.validate_course_name(course_name)

    @staticmethod
    def validate_course_name(course_name):
        if not course_name.strip():
            raise ValueError("Course name cannot be empty.")
        elif len(course_name) > 100:
            raise ValueError("Course name cannot exceed 100 characters.")
        elif len(course_name) < 2:
            raise ValueError("Course name must be at least 2 characters long.")
        else:
            return course_name.strip()

    # getters
    def get_course_id(self):
        return self.course_id

    def get_course_name(self):
        return self.course_name
    #pula pula 