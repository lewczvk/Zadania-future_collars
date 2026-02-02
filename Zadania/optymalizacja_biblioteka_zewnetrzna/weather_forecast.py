import json

class WeatherForecast:
    def __init__(self, file_path):
        self.file = file_path
        self.data = self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.file) as file:
            return json.loads(file.read())

    def __getitem__(self, item):
        city, date = item
        for searched_city, data in self.data.items():
            if city == searched_city:
                for searched_date, info in data.items():
                    if searched_date == date:
                        return info


    def __setitem__(self, key, value):
        city, date = key
        if city not in self.data.keys():
            self.data[city] = {}
        self.data[city][date] = value
        print(self.data)

    def __iter__(self):
        return iter(self.data)

    def items(self):
        for country in self.data:
            yield country, self.data[country]

weather_forecast = WeatherForecast("data_2.json")

# print(weather_forecast.data)

print(weather_forecast["Warszawa", "2026-01-20"])

weather_forecast["Warszawa", "2026-01-20"] = "Nie będzie padać"
weather_forecast["Raciborz", "2026-01-20"] = "Nie będzie padać"



