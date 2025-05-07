import requests
import random

url = "https://type.fit/api/quotes"
response = requests.get(url)
quotes = response.json()

quote = random.choice(quotes)
print(f"{quote['text']} — {quote['author']}")