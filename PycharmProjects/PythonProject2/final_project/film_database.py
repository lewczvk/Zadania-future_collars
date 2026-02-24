import requests

def get_data_from_movie_api(title, year):
    api_key = 'my-api-key'
    # movie = get_movie_info('Avatar', 2009, api_key)
    url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={api_key}"
    response = requests.get(url=url)
    return response.json()

# def movie_classification(movie):
#     try:
#         rating = float(movie.get('imdbRating', 0))
#     except ValueError:
#             return "This film doesn't have an imdb rating"
#
#     if rating >= 7.0:
#         return "This is one of the best rated movies"
#     elif rating >= 5.0:
#         return "This is one of the average rated movies"
#     else:
#         return "This is one of the worst rated films."



