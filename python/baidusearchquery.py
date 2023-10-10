import requests

task_params = {
    'target': 'baidu_search',
    'query': 'donuts',
    'parse': False
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    json = task_params,
    auth = (username, password)
)

print(response.text)
