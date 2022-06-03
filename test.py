import requests #module that allows us to make requests(post, get, patch etc.)

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + "video/1", {"likes": 10, "name": "chris", "views": 100000})
# print(response.json())
# input()
response = requests.get(BASE + "video/2")
print(response.json())
