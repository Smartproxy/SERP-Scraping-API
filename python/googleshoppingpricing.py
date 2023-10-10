import requests

task_params = {
    'target': 'google_shopping_pricing',
    'query': '1487724521556311753',
    'parse': True,
    'geo': 'London,England,United Kingdom'
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    json = task_params,
    auth = (username, password)
)

print(response.text)
