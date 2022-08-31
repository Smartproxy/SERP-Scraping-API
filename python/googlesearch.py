import requests

task_params = {
    'target': 'google_search',
    'query': 'history',
    'parse': True,
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