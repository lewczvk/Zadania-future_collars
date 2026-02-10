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

    # def add_new_entry_to_data(self, title, year, info):
    #     if not self.data.get(title):
    #         self.data[title] = {}
    #     self.data[title][year] = info
    #
    # def check_if_info_exist_in_data(self, title, year, info):
    #     for movie in self.data.keys():
    #         if movie == title:
    #             for year, info in self.data[movie].items():
    #                 if year == year:
    #                     return info
