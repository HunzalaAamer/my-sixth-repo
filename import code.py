import requests
from bs4 import Beautifulsoup
url = "https://import code.com"
response = requests.get(url)
soup = Beautifulsoap (response.text, "html.parser")

print(soup.find("h1").text)
print(soup.find("p").text)