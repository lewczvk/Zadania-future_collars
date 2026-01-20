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

    def add_new_entry_to_data(self, city, date, info):
        if not self.data.get(city):
            self.data[city] = {}
        self.data[city][date] = info

    def check_if_info_exist_in_data(self, searched_city, searched_date):
        for city in self.data.keys():
            if city == searched_city:
                for date, info in self.data[city].items():
                    if date == searched_date:
                        return info








