const response = await fetch(
    'https://scraper-api.smartproxy.com/v2/scrape', {
        method: 'POST',
        body: {
            target: 'bing',
            parse: true,
            query: 'history'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)
