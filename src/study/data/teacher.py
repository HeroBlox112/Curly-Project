class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = self.validate_teacher_name(teacher_name)

    @staticmethod
    def validate_teacher_name(teacher_name):
        if not teacher_name.strip():
            raise ValueError("Teacher name cannot be empty.")
        elif len(teacher_name) > 100:
            raise ValueError("Teacher name cannot exceed 100 characters.")
        elif len(teacher_name) < 2:
            raise ValueError("Teacher name must be at least 2 characters long.")
        elif len(teacher_name.split()) != 2:
            raise ValueError("Teacher name must contain first and last name")
        else:
            return teacher_name.strip()

    # getters
    def get_teacher_id(self):
        return self.teacher_id

    def get_teacher_name(self):
        return self.teacher_name