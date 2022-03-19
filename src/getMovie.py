import requests

api_endpoint = "https://www.cinemaxx.de/compeso/getMovie"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}
payload = {"film_id": "26692", "origin_url": "/26692/73"}

response = requests.request("POST", api_endpoint, data=payload, headers=headers)

print(response.text)
