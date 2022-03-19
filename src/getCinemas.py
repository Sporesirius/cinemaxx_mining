import requests

api_endpoint = "https://www.cinemaxx.de/compeso/getCinemas"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}
payload = {"film_id": "26692", "setStart": "true"}

response = requests.request("POST", api_endpoint, data=payload, headers=headers)

print(response.text)
