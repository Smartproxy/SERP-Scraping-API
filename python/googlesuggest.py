import requests

url = "https://scrape.smartproxy.com/v1/tasks"

payload = {
    "target": "google_images",
    "query": "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg",
    "parse": False,
    "geo": "London,England,United Kingdom"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic U1B1c2VybmFtZTpTUGFzc3dvcmQ="
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)