import requests

api="https://icanhazdadjoke.com/"
response = requests.get(api,headers={"Accept":"application/json"})
jokes = response.json()
print(jokes['joke'])