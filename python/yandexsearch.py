import requests

task_params = {
    'target': 'yandex',
    'url': 'https://yandex.com/search/?text=cookies&lr=10393',
    'parse': False,
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    json = task_params,
    auth = (username, password)
)

print(response.text)
