import requests

r = requests.get("https://www.codewithharry.com") # get request helps to get the data from the website

print(r.text)
with open("index.html", "w") as f:
    f.write(r.text)