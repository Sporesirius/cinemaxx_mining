import requests

api_endpoint = "https://www.cinemaxx.de/compeso/getVersions"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}
payload = {"cinema_id": "73", "film_id": "26692"}

response = requests.request("POST", api_endpoint, data=payload, headers=headers)

print(response.text)
