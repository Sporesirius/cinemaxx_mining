import requests

api_endpoint = "https://www.cinemaxx.de/data/films/"

response = requests.request("GET", api_endpoint)

print(response.text)
