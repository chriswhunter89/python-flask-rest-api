import requests #module that allows us to make requests(post, get, patch etc.)
import random
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")
print(response.json())