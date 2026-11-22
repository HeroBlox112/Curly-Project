class Result:
    def __init__(self, record_id, student_id, study_hours_week, absences, final_grade):
        self.record_id = self.validate_record_id(record_id)
        self.student_id = student_id
        self.study_hours_week = self.validate_study_hours_week(study_hours_week)
        self.absences = self.validate_absences(absences)
        self.final_grade = self.validate_final_grade(final_grade)

    @staticmethod
    def validate_record_id(record_id):
        if not isinstance(record_id, int):
            raise ValueError("Record ID must be an integer.")
        elif record_id < 1:
            raise ValueError("Record ID must be greater than or equal to 1.")
        elif record_id > 100:
            raise ValueError("Record ID must be less than or equal to 100.")
        else:
            return record_id

    @staticmethod
    def validate_study_hours_week(study_hours_week):
        if not isinstance(study_hours_week, float):
            raise ValueError("Study hours per week must be a float.")
        else:
            return study_hours_week

    @staticmethod
    def validate_absences(absences):
        if not isinstance(absences, int):
            raise ValueError("Absences must be an integer.")
        elif absences < 0:
            raise ValueError("Absences cannot be negative.")
        else:
            return absences

    @staticmethod
    def validate_final_grade(final_grade):
        if not isinstance(final_grade, float):
            raise ValueError("Final grade must be a float.")
        elif final_grade < 0.0 or final_grade > 100.0:
            raise ValueError("Final grade must be between 0.0 and 100.0.")
        else:
            return final_grade