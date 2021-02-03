import requests
import json

url = 'https://api.namefake.com/'

response = requests.get(url)
json_data = json.loads(response.text)

for i in json_data:
    print(i+ ' : ' + str(json_data[i]))
