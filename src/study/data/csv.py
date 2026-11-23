import csv

class CSV:
    def __init__(self, path):
        self.path = self._validate_path(path)

    @staticmethod
    def _validate_path(path):
        if not path.strip():
            raise ValueError("Path cannot be empty.")
        elif len(path) > 255:
            raise ValueError("Path cannot exceed 255 characters.")
        else:
            return path.strip()

    def read_csv(self):
        with open(self.path, mode="r", newline="") as file:
            return list(csv.DictReader(file))

