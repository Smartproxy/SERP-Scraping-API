const response = await fetch(
    'https://scrape.smartproxy.com/v1/tasks', {
        method: 'POST',
        body: {
            target: 'google_shopping_pricing'
            parse: true,
            query: '1487724521556311753'
        },
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Basic AUTH'
        },
    }
).catch(error => console.log(error));

console.log(response)
