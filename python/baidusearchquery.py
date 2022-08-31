import requests

task_params = {
    'target': 'baidu_search',
    'query': 'donuts',
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