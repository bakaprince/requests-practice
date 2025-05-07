import requests

url=input("Enter image link to download: ")
response = requests.get(url,stream=True)
data=response.content
with open("img.jpg","wb") as file:
    file.write(data)
print("success")