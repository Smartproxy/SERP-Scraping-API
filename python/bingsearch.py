import requests

task_params = {
    'target': 'bing',
    'url': 'https://www.bing.com/search?q=history',
    'parse': True,
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    json = task_params,
    auth = (username, password)
)

print(response.text)
