import requests

api_endpoint = "https://www.cinemaxx.de/data/labels/"

response = requests.request("GET", api_endpoint)

print(response.text)
