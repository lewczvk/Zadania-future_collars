from file_handler import FileHandler
import requests

def get_data_from_movie_api(title, year, api_key):
    api_key = 'ed95e196'
    # movie = get_movie_info('Avatar', 2009, api_key)
    url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={api_key}"
    response = requests.get(url=url)
    # movie_info = response.json().get("runtime").get("genre").get("director").get("writer").get("plot").get("awards")
    print(response)

# def movie_info_into_message(movie_info):
#     if movie_info.ratings > 7/10:
#         return "This is one of the best rated movies"
#     elif movie_info.ratings < 7/10:
#         return "Here is one of the average rated movies"
#     elif movie_info.ratings <= 4/10:
#         return "Here is one of the low rated movies"
#
# file_name = FileHandler("data.json")
title = input("Enter title: ")
year = int(input("Enter year: "))
#
# info_in_file = file_name.check_if_info_exist_in_data(title, year)
# if info_in_file:
#     print(f"The data is already in the system: {info_in_file}")
# else:
#
#     movie_info = get_data_from_movie_api(title, year)
#     message = movie_info_into_message(movie_info)
#     print(message)
#     file_name.add_new_entry_to_data(title, year, message)
#     file_name.write_file()


#?????? robic z zadaniem z api z szkolenia moze bedzie jasniej



