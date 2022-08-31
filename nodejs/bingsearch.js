curl --request POST \
     --url https://scrape.smartproxy.com/v1/tasks \
     --header 'Accept: application/json' \
     --header 'Authorization: Basic U1B1c2VybmFtZTpTUHBhc3N3b3Jk' \
     --header 'Content-Type: application/json' \
     --data '
{
     "target": "bing",
     "parse": true,
     "url": "https://www.bing.com/search?q=history"
}
'