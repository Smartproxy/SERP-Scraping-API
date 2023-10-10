const response = await fetch(
    'https://scraper-api.smartproxy.com/v2/scrape', {
        method: 'POST',
        body: {
                target:'google_trends_explore',
                query: 'pizza',
                search_type:'web_search',
                date_start: '2022-01-10',
                date_end: '2023-01-10',
                geo:'US',
                locale:'en-us',
                device_type:'desktop'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)
