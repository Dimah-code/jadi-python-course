import requests

api_url = "http://api.open-notify.org/iss-now.json"

response = requests.get(api_url)

try:
    json_data = response.json()

    print(json_data)
except requests.exceptions.RequestException as e:
    print("Cannot connect to API:", e)
