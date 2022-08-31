
# SERP Scraping API



With our SERP Scraping API, you can scrape all popular search engines. Most notably and in depth, Google, but also Baidu, Bing, and Yandex.

## List of contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Google](#google)
- [Parameters](#parameters)
- [License](#license)

## Introduction

With our SERP Scraping API, you can scrape all popular search engines. Most notably and in depth, Google, but also Baidu, Bing, and Yandex.

## Authentication

Once you have an active SERP subscription, you can try sending a request right from the dashboard SERP > Authentication method tab simply by entering your username, password, and clicking on Generate. You will also see an example of curl request generated right below your entered ``` user:pass. ``` 

Note that this is only an example with preset values to get you on the right track for forming your own request, meaning you will not be able to change the request values in the dashboard itself – that will have to be done in your code.


## Google

Google can be scraped using multiple different targets, including the Google search bar, direct URL, or more specific targets like Google suggest, Google ads, etc.

Below you will find every target, whether it can be parsed to JSON, its required parameters, and ready to use code examples for cURL, Python and PHP, where you only need to change the username and password for your SERP Scraping API user for the code to work.

For available parameters, you can refer to [Parameters](#parameters).

### Google Search

API Link: https://scrape.smartproxy.com/v1/tasks

```http
  POST /tasks
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Response

First 2 organic results
```http
          "organic": [
            {
              "pos": 1,
              "url": "https://www.worldbank.org/en/home",
              "desc": "With 189 member countries, the World Bank Group is a unique global partnership fighting poverty worldwide through sustainable solutions.",
              "title": "World Bank Group - International Development, Poverty ...",
              "url_shown": "https://www.worldbank.org› ...",
              "pos_overall": 2
            },
            {
              "pos": 2,
              "url": "https://www.who.int/",
              "desc": "WHO's primary role is to direct international health within the United Nations' system and to lead partners in global health responses.",
              "title": "WHO | World Health Organization",
              "url_shown": "https://www.who.int",
              "pos_overall": 3
            }
        
```
### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googlesearch.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googlesearch.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googlesearch.py > googlesearch.py ``` |
| PHP                 | [php/googlesearch.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googlesearch.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googlesearch.php > googlesearch.php ``` |
| Node.js                 | [nodejs/googlesearch.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googlesearch.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googlesearch.js > googlesearch.js ``` |
