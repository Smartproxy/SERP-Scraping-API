import requests

task_params = {

    'target':'google_trends_explore',
    'query': 'pizza',
    'search_type':'web_search',
    'date_start': '2022-01-10',
    'date_end': '2023-01-10',
    'geo':'US',
    'locale':'en-us',
    'device_type':'desktop'
}

username = 'SPusername'
password = 'SPpassword'

response = requests.post(
    'https://scraper-api.smartproxy.com/v2/scrape',
    json = task_params,
    auth = (username, password)
)

print(response.text)
