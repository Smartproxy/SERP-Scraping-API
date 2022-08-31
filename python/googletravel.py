import requests

task_params = {
    'target': 'google_travel_hotels',
    'query': 'hilton',
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