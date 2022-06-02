import requests #module that allows us to make requests(post, get, patch etc.)

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/presto")
print(response.json())
