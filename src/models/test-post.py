import requests
import json

url = "http://127.0.0.1:8080/predict"

payload = json.dumps({
  "data": [
    7,
    0.56,
    0.17,
    1.7,
    0.065,
    15,
    24,
    0.99514,
    3.44,
    0.68,
    10.55
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)