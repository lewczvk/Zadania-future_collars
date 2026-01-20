"""Napisz program, który sprawdzi, czy danego dnia będzie padać. Użyj do tego poniższego API. Aplikacja ma działać następująco:

Program pyta dla jakiej daty należy sprawdzić pogodę. Data musi byc w formacie YYYY-mm-dd, np. 2022-11-03. W przypadku nie podania daty, aplikacja przyjmie za poszukiwaną datę następny dzień.
Aplikacja wykona zapytanie do API w celu poszukiwania stanu pogody.
Istnieją trzy możliwe informacje dla opadów deszczu:
Będzie padać (dla wyniku większego niż 0.0)
Nie będzie padać (dla wyniku równego 0.0)
Nie wiem (gdy wyniku z jakiegoś powodu nie ma lub wartość jest ujemna)
Będzie padać
Nie będzie padać
Nie wiem
Wyniki zapytań powinny być zapisywane do pliku. Jeżeli szukana data znajduje sie juz w pliku, nie wykonuj zapytania do API, tylko zwróć wynik z pliku.

URL do API:
https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}

W URL należy uzupełnić parametry: latitude, longitude oraz searched_date"""

from file_handler import FileHandler
import requests
from geopy.geocoders import Nominatim

def get_data_from_weather_api(latitude, longitude, searched_date):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
    response = requests.get(url=url)
    rain_info = response.json().get("daily").get("rain_sum")[0]
    print(rain_info)
    return rain_info

def rain_info_into_message(rain_info):
    if rain_info < 0:
        return "Nie ma takiej możliwości"
    elif rain_info == 0:
        return "Nie będzie padać"
    else:
        return "Będzie padać"


file_name = FileHandler("data.json")
searched_date = input("Podaj datę do sprawdzenia pogody YYYY-MM-DD: ")
searched_city = input("Podaj nazwę miasta: ")
geolocator = Nominatim(user_agent="Aplikacja Wiktorii")
location = geolocator.geocode(searched_city)
latitude = location.latitude
longitude = location.longitude


info_in_file = file_name.check_if_info_exist_in_data(searched_city, searched_date)
if info_in_file:
    print(f"Dane istnieją już w systemie: {info_in_file}")
else:

    rain_info = get_data_from_weather_api(latitude, longitude, searched_date)
    message = rain_info_into_message(rain_info)
    print(message)
    file_name.add_new_entry_to_data(searched_city, searched_date, message)
    file_name.write_file()

