import requests

url = "https://www.cinemaxx.de/compeso/getSeats"

headers = {
  "cookie": "bookingsessionid=fbab8e4a-97ae-4355-acc2-68710df18c2a",
  "Content-Type": "application/x-www-form-urlencoded"
}
payload = "seance_id=A690B800023FVUVQLG"

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)