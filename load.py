import requests

while True:
    requests.get("http://52.137.106.60/")
    requests.post("http://52.137.106.60/", data={"vote":"Cats"})