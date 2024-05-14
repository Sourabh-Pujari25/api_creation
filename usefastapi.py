import requests


number = 20
url = f"http://127.0.0.1:8000/factorial?n={number}"
response = requests.get(url)
op = response.json()
print(op)