import requests

url = "https://www.cinemaxx.de/compeso/getSeats"

headers = {
  "Content-Type": "application/x-www-form-urlencoded"
}
payload = "seance_id=7790B800023FVUVQLG"

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)