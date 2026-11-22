class School:
    def __init__(self, school_id, school_name, school_city):
        self.school_id = school_id
        self.school_name = self.validate_school_name(school_name)
        self.school_city = self.validate_school_city(school_city)

    @staticmethod
    def validate_school_name(school_name):
        if not school_name.strip():
            raise ValueError("School name cannot be empty.")
        elif len(school_name) > 100:
            raise ValueError("School name cannot exceed 100 characters.")
        elif len(school_name) < 2:
            raise ValueError("School name must be at least 2 characters long.")
        else:
            return school_name.strip()

    @staticmethod
    def validate_school_city(school_city):
        if not school_city.strip():
            raise ValueError("School city cannot be empty.")
        elif len(school_city) > 100:
            raise ValueError("School city cannot exceed 100 characters.")
        elif len(school_city) < 2:
            raise ValueError("School city must be at least 2 characters long.")
        else:
            return school_city.strip()

    # getters
    def get_school_id(self):
        return self.school_id

    def get_school_name(self):
        return self.school_name

    def get_school_city(self):
        return self.school_city