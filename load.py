import requests

while True:
    requests.get("http://13.66.163.95/")
    requests.post("http://13.66.163.95/", data={"vote":"Cats"})