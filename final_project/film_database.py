from file_handler import FileHandler
import requests

def get_data_from_movie_api(title, year):
    url = f"http://www.omdbapi.com/"
    response = requests.get(url=url)
    print(response)

title = input("Enter title: ")
year = int(input("Enter year: "))

get_data_from_movie_api(title, year)

