const response = await fetch(
    'https://scraper-api.smartproxy.com/v2/scrape', {
        method: 'POST',
        body: {
            target: 'baidu',
            parse: false,
            url: 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=donuts&fenlei=256&rsv_pq=dc12cef9000cecd5&rsv_t=eb7dbdneGaOeG8buqmqpjMaLZ8tiygOJCtkEqqboaIRy1vnbiFlpef4ieJg&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=6940&rsv_sug4=6940'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)
