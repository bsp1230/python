import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
data = {
    "userId": 8,
    "title": "Python Books",
    "completed": False
}
response = requests.post(api_url, json=data)
response.json()
print(response.status_code)




