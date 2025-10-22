import requests

api_url = "http://api.open-notify.org/astros.json"

try:
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()  # Raises an exception for bad status codes

    json_data = response.json()
    print("Number of people in space: ", json_data["number"])

    people = json_data["people"]

    for person in people:
        print(f"{person['name']} - {person['craft']}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
