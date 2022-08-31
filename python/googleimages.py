import requests

task_params = {
    'target': 'google_images',
    'query': 'https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg',
    'parse': False,
    'geo': 'London,England,United Kingdom'
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scrape.smartproxy.com/v1/tasks',
    json = task_params,
    auth = (username, password)
)

print(response.text)