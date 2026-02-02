from file_handler import FileHandler
import requests

def get_data_from_api(title):
    url = f"http://www.omdbapi.com/?title={title}&"
    response = requests.get(url=url)

title = input("Enter title: ")
data = response.json()