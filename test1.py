import requests

variable2 = input("test message: ")

url = "http://127.0.0.1:8080"

variable = requests.request("POST", url, data=variable2)