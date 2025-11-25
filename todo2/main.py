import requests

url = "https://dummyjson.com/todos"

response = requests.get(url)
print(response.status_code)
print(response.json())
print(type(response.json()))