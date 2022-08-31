import requests

task_params = {
    'target': 'baidu',
    'url': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=donuts&fenlei=256&rsv_pq=dc12cef9000cecd5&rsv_t=eb7dbdneGaOeG8buqmqpjMaLZ8tiygOJCtkEqqboaIRy1vnbiFlpef4ieJg&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=6940&rsv_sug4=6940',
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