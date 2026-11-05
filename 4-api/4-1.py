import requests 
import pandas as pd

uri = "https://portal.app.cent-su.org/api/funnyname/random?n=5"
response = requests.get(uri)
# print(response.text)

#deserialize the response to a Python object
response.raise_for_status() #says to throw an excpetion if you don not get a valid response 
data = response.json() #parses for you
# for name in data: 
#     print(name['first'], name['last'])


import os
import requests

url = "https://portal.app.cent-su.org/api/weather/geocode"
params = {
    "language": "en",
    "count": 2,
    "place": "Syracuse, NY",
}
headers = {
    "accept": "application/json",
    "X-API-KEY": "6f8517d137a6ef5b59e0e7ac",
}

response = requests.get(url, params=params, 
                        headers=headers, timeout=30)
print(response.url)
response.raise_for_status()

data = response.json()
df = pd.json_normalize(data['results'])
print(df)
