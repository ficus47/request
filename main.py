import requests
import json

url = 'http://172.167.226.145:8080'
data = {
    'username': 'utilisateur',
    'password': 'motdepasse'
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
