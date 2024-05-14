import requests,json
payload = json.dumps({
    "number":12
})


number = 20
url = f"http://127.0.0.1:8000/factorial"
response = requests.put(url,data=payload)
op = response.json()
print(op)