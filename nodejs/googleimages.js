const response = await fetch(
    'https://scraper-api.smartproxy.com/v2/scrape', {
        method: 'POST',
        body: {
            target: 'google_images',
            parse: false,
            query: 'https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)
