const response = await fetch(
    'https://scrape.smartproxy.com/v1/tasks', {
        method: 'POST',
        body: {
            target: 'google_search',
            query: 'Adidas',
            parse: true,
            domain: 'com',
            page_from: 1,
            num_pages: 10,
            locale: 'en-us',
            geo: 'Detroit,Maine,United States',
            device_type: 'desktop',
            google_results_language: 'en'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)