#!/usr/bin/python3

import requests


resp_1 = requests.get("https://jsonplaceholder.typicode.com/todos/", params={"userId": 2})
# resp = requests.get("https://jsonplaceholder.typicode.com/todos/")
print(resp_1.json())
# print(resp.json())