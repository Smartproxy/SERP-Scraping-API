import requests

task_params = {
    'target': 'google_shopping_product',
    'query': '8129397700139936548',
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