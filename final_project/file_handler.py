import json

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_file()

    def read_file(self):
        with open(self.filename, 'r') as file:
            return json.loads(file.read())

    def write_file(self):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.data, indent=4))