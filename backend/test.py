import requests

data = {
    "height": 180,
    "weight": 75,
    "level": "intermediate"
}

response = requests.post("http://127.0.0.1:8000/recommend-equipment", json=data)
print("Status:", response.status_code)
print("Response:", response.json())
