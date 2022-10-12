import requests

task_params = {
    'target': 'google_suggest',
    'query': 'world',
    'parse': False
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scrape.smartproxy.com/v1/tasks',
    json = task_params,
    auth = (username, password)
)

print(response.text)