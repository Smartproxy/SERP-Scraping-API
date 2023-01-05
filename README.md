
# SERP Scraping API

[<img src="https://i.ibb.co/qFJN8HD/SERP.png">](https://dashboard.smartproxy.com/register?utm_source=Github&utm_medium=banner&utm_campaign=Serp-scraping)


## List of contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Google](#google)
- [Baidu](#baidu)
- [Bing](#bing)
- [Yandex](#yandex)
- [Parameters](#parameters)
- [Targets](#targets)
- [Languages](#languages)
- [Response Codes](#response-codes)
- [Postman Collection](#postman-collection)
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

### Target: ```google_search``` (parseable)
Required parameters: ```query``` (history in this example)

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

### Target: ```google``` (parseable)
Required parameters: ```url```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Google Search URL |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googlesearchurl.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googlesearchurl.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googlesearchurl.py > googlesearchurl.py ``` |
| PHP                 | [php/googlesearchurl.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googlesearchurl.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googlesearchurl.php > googlesearchurl.php ``` |
| Node.js                 | [nodejs/googlesearchurl.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googlesearchurl.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googlesearchurl.js > googlesearchurl.js ``` |

### Target: ```google_hotels``` (not parseable)
Required parameters: ```query```

Returns search results from Google hotels. This target is not parseable, meaning it will return HTML.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googlehotels.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googlehotels.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googlehotels.py > googlehotels.py ``` |
| PHP                 | [php/googlehotels.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googlehotels.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googlehotels.php > googlehotels.php ``` |
| Node.js                 | [nodejs/googlehotels.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googlehotels.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googlehotels.js > googlehotels.js ``` |

### Target: ```google_travel_hotels``` (not parseable)
Required parameters: ```query```

Returns hotel search results from Google Travel service in HTML.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |
| `stars` | `integer` | Star rating, 1-5 stars |
| `guests` | `integer` | Guest count |
| `date_range` | `string` | Y-m-d,Y-m-d |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googletravel.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googletravel.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googletravel.py > googletravel.py ``` |
| PHP                 | [php/googletravel.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googletravel.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googletravel.php > googletravel.php ``` |
| Node.js                 | [nodejs/googletravel.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googletravel.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googletravel.js > googletravel.js ``` |

### Target: ```google_shopping_search``` (parseable)
Required parameters: ```query```

Returns results from Google Shopping search.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googleshopping.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googleshopping.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googleshopping.py > googleshopping.py ``` |
| PHP                 | [php/googleshopping.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googleshopping.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googleshopping.php > googleshopping.php ``` |
| Node.js                 | [nodejs/googleshopping.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googleshopping.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googleshopping.js > googleshopping.js ``` |

### Target: ```google_shopping_product``` (parseable)
Required parameters: ```query``` (as item ID from Google Shopping)

Returns results from Google Shopping based on supplied item ID.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googleshoppingproduct.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googleshoppingproduct.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googleshoppingproduct.py > googleshoppingproduct.py ``` |
| PHP                 | [php/googleshoppingproduct.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googleshoppingproduct.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googleshoppingproduct.php > googleshoppingproduct.php ``` |
| Node.js                 | [nodejs/googleshoppingproduct.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googleshoppingproduct.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googleshoppingproduct.js > googleshoppingproduct.js ``` |

### Target: ```google_shopping_pricing``` (parseable)
Required parameters: ```query``` (as item ID from Google Shopping)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googleshoppingpricing.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googleshoppingpricing.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googleshoppingpricing.py > googleshoppingpricing.py ``` |
| PHP                 | [php/googleshoppingpricing.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googleshoppingpricing.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googleshoppingpricing.php > googleshoppingpricing.php ``` |
| Node.js                 | [nodejs/googleshoppingpricing.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googleshoppingpricing.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googleshoppingpricing.js > googleshoppingpricing.js ``` |

### Target: ```google_images``` (not parseable)
Required parameters: ```query```

Returns links of images similar to the provided image link.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `url` |  Image URL |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googleimages.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googleimages.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googleimages.py > googleimages.py ``` |
| PHP                 | [php/googleimages.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googleimages.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googleimages.php > googleimages.php ``` |
| Node.js                 | [nodejs/googleimages.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googleimages.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googleimages.js > googleimages.js ``` |

### Target: ```google_suggest``` (not parseable)
Required parameters: ```query```, ```geo``` in ISO 2 format

Returns Google keyword suggestions based on the supplied query.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `geo` | `string` |  Geo-targeting location |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googlesuggest.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googlesuggest.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googlesuggest.py > googlesuggest.py ``` |
| PHP                 | [php/googlesuggest.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googlesuggest.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googlesuggest.php > googlesuggest.php ``` |
| Node.js                 | [nodejs/googlesuggest.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googlesuggest.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googlesuggest.js > googlesuggest.js ``` |

### Target: ```google_ads``` (parseable)
Required parameters: ```query```

Returns Google search results with paid ads.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Google Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/googleads.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/googleads.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/googleads.py > googleads.py ``` |
| PHP                 | [php/googleads.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/googleads.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/googleads.php > googleads.php ``` |
| Node.js                 | [nodejs/googleads.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/googleads.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/googleads.js > googleads.js ``` |

## Baidu
Baidu can be targeted either using direct URL or by using the query parameter to the Baidu search bar.

### Target: ```baidu``` (not parseable)
Required parameters: ```url```

Target by supplying direct URL link.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Baidu Search URL |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/baidusearch.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/baidusearch.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/baidusearch.py > baidusearch.py ``` |
| PHP                 | [php/baidusearch.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/baidusearch.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/baidusearch.php > baidusearch.php ``` |
| Node.js                 | [nodejs/baidusearch.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/baidusearch.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/baidusearch.js > baidusearch.js ``` |

### Target: ```baidu_search```(not parseable)
Required parameters: ```query```

Target by supplying your query to the Baidu search bar.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Baidu Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/baidusearchquery.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/baidusearchquery.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/baidusearchquery.py > baidusearchquery.py ``` |
| PHP                 | [php/baidusearchquery.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/baidusearchquery.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/baidusearchquery.php > baidusearchquery.php ``` |
| Node.js                 | [nodejs/baidusearchquery.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/baidusearchquery.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/baidusearchquery.js > baidusearchquery.js ``` |

## Bing

Bing can be targeted either using direct URL or by using the query parameter to the Bing search bar.

### Target: ```bing``` (parseable)
Required parameters: ```url```

Target by supplying direct URL link.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Bing Search URL |
| `target` | `url` | Scraping target |

### Response

```
{
  "results": [
    {
      "content": {
        "url": "https://www.bing.com/search?q=history",
        "page": 1,
        "results": {
          "paid": [],
          "organic": [
            {
              "pos": 1,
              "url": "https://www.history.com/",
              "desc": "Watch full episodes of your favorite HISTORY series, and dive into thousands of historical articles and videos. To know History is to know life. By submitting your information, you agree to ...",
              "title": "HISTORY | Watch Full Episodes of Your Favorite Shows",
              "url_shown": "https://www.history.com",
              "pos_overall": 1
            },
            {
              "pos": 2,
              "url": "https://ejje.weblio.jp/content/history",
              "desc": "history とは 意味・読み方・使い方. 発音を聞く. プレーヤー再生. ピン留め. 単語を追加. 意味・対訳. 歴史、史学、歴史書、史書、史劇、 (学問・言語などの)発達史、変遷、経歴、来歴、沿革. 音節 his・to・ry 発音記号・読み方.",
              "title": "英語「history」の意味・使い方・読み方 | Weblio英和 …",
              "url_shown": "https://ejje.weblio.jp/content/history",
              "pos_overall": 2
            },
            {
              "pos": 3,
              "url": "https://www.bing.com/profile/history",
              "desc": "Microsoft gives you tools to manage your privacy and data. L e a r n m o r e. S i g n i n to see your search history on different browsers and computers.",
              "title": "Search - Search History - Bing",
              "url_shown": "https://www.bing.com/profile/history",
              "pos_overall": 3
            },
            {
              "pos": 4,
              "url": "https://jp.history.com/",
              "desc": "ヒストリーチャンネルは、上質な番組を放送する世界最大で日本唯一の歴史＆エンターテインメント専門チャンネルです。 長期刑の判決を受けた犯罪者たちは、刑務所に収監される前の最後の24時間をどう過ごすのか？過ちを謝罪する者、幼い子どもの親権を手放す者、崩壊した家族を修 …",
              "title": "日本・世界の歴史＆エンタメ | THE HISTORY CHANNEL JAPAN ...",
              "url_shown": "https://jp.history.com",
              "pos_overall": 4
            },
            {
              "pos": 5,
              "url": "https://history.google.com/",
              "desc": "Welcome to My Activity. Data helps make Google services more useful for you. Sign in to review and manage your activity, including things you’ve searched for, websites you’ve visited, and videos you’ve watched. Learn more.",
              "title": "Welcome to My Activity",
              "url_shown": "https://history.google.com",
              "pos_overall": 5
            },
            {
              "pos": 6,
              "url": "https://www.youtube.com/HISTORYjp",
              "desc": "世界最大の歴史エンターテイメントブランド「HISTORY」ヒストリーチャンネル の公式YouTubeチャンネルです。人気シリーズを続々公開！最新情報は ...",
              "title": "HISTORY公式 - YouTube",
              "url_shown": "https://www.youtube.com/HISTORYjp",
              "pos_overall": 6
            },
            {
              "pos": 7,
              "url": "https://eow.alc.co.jp/search?q=history",
              "desc": "history 【名】 歴史、歴史学 過去のこと[もの]・I'm history. : 私の時代は終わった。／私は過去の人間...【発音】hístəri【カナ】ヒストリィ【変化】《複》histories - アルクがお届けするオンライン英和・和英辞書検索サービス。",
              "title": "historyの意味・使い方・読み方｜英辞郎 on the WEB",
              "url_shown": "https://eow.alc.co.jp/search?q=history",
              "pos_overall": 7
            },
            {
              "pos": 8,
              "url": "https://history.gt/index.html",
              "desc": "2022年07月22日 『HISTORY Advanced』新発売！. 他シリーズとの違いを徹底比較！. 2022年04月26日 新商品「Performanceシリーズ」についてYouNiqueのお二人に語って頂きました！. 2022年04月01日 皆様のおかげで10万本販売達成！. 感謝キャンペーンスタート！. 2021年11 …",
              "title": "HISTORY ヒストリー HISTORY -島村楽器",
              "url_shown": "https://www.history.gt",
              "pos_overall": 8
            },
            {
              "pos": 9,
              "url": "https://jp.history.com/timetable/",
              "desc": "ヒストリーチャンネルは、上質な番組を放送する世界最大で日本唯一の歴史＆エンターテインメント専門チャンネルです。 TEL： 0570-001-607（ナビダイヤル） ヒストリーチャンネルカスタマーセンター 受付時間（10:00 – 20:00/年中無休） ※PHS・IP電話等からは、03-4333-1031",
              "title": "日別番組表 | ヒストリーチャンネル",
              "url_shown": "https://jp.history.com/timetable",
              "pos_overall": 9
            }
          ]
        },
        "parse_status_code": 12000
      },
      "status_code": 200,
      "url": "https://www.bing.com/search?q=history",
      "task_id": "6970716517377789953",
      "created_at": "2022-08-31 12:18:47",
      "updated_at": "2022-08-31 12:18:51"
    }
  ]
}
```

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/bingsearch.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/bingsearch.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/bingsearch.py > bingsearch.py ``` |
| PHP                 | [php/bingsearch.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/bingsearch.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/bingsearch.php > bingsearch.php ``` |
| Node.js                 | [nodejs/bingsearch.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/bingsearch.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/bingsearch.js > bingsearch.js ``` |

### Target: ```bing_search```(parseable)
Required parameters: ```query```

Target by supplying your query to the Bing search bar.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Bing Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/bingsearchquery.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/bingsearchquery.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/bingsearchquery.py > bingsearchquery.py ``` |
| PHP                 | [php/bingsearchquery.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/bingsearchquery.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/bingsearchquery.php > bingsearchquery.php ``` |
| Node.js                 | [nodejs/bingsearchquery.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/bingsearchquery.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/bingsearchquery.js > bingsearchquery.js ``` |

## Yandex

Yandex can be targeted either using direct URL or by using the query parameter to the Yandex search bar.

### Target: ```yandex``` (not parseable)
Required parameters: ```url```

Target by supplying direct URL link.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Yandex Search URL |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/yandexsearch.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/yandexsearch.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/yandexsearch.py > yandexsearch.py ``` |
| PHP                 | [php/yandexsearch.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/yandexsearch.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/yandexsearch.php > yandexsearch.php ``` |
| Node.js                 | [nodejs/yandexsearch.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/yandexsearch.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/yandexsearch.js > yandexsearch.js ``` |


### Target: ```yandex_search``` (not parseable)
Required parameters: ```query```

Target by supplying your query to the Yandex search bar.

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `query` | `string` |  Yandex Search query |
| `target` | `url` | Scraping target |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/yandexsearchquery.py](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/python/yandexsearchquery.py) |``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/python/yandexsearchquery.py > yandexsearchquery.py ``` |
| PHP                 | [php/yandexsearchquery.php](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/php/yandexsearchquery.php)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/php/yandexsearchquery.php > yandexsearchquery.php ``` |
| Node.js                 | [nodejs/yandexsearchquery.js](https://github.com/Smartproxy/SERP-Scraping-API/blob/main/nodejs/yandexsearchquery.js)   | ``` curl https://raw.githubusercontent.com/Smartproxy/SERP-Scraping-API/main/nodejs/yandexsearchquery.js > yandexsearchquery.js ``` |

## Parameters

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `target` | `string` |  Data source. Available targets are listed [here](#targets). |
| `url` | `url` | Direct URL (link) |
| `domain` | `url` | Any available Google Top-level domain. |
| `query` | `string` |  |
| `page_from` | `integer` | Starting page number. |
| `num_pages` | `integer` | Starting page number. |
| `locale` | `string` | This will change the Google search page web interface language (not the results). Example: – en-US – en-GB |
| `geo` | `string` | The geographical location that the result depends on. City location names, state names, country names, coordinates and radius, Google’s Canonical |
| `device_type` | `string` | Device type and browser. Supported: ```desktop```, ```desktop_chrome```, ```desktop_firefox```, ```mobile```, ```mobile_android```, ```mobile_ios```. |
| `parse` | `boolean` | 'true' will return parsed output in JSON format. Leave blank for HTML – not all data sources can be parsed. |
| `google_nfpr` | `boolean` | Auto-correction.|
| `google_results_language	` | `string` | Shows results in a particular language. All of the supported languages are listed [here](#languages).|
| `google_tbm	` | `string` | This parameter lets you filter Google Search results for specific types of content (news, apps, videos...). |
| `google_tbs` | `string` | This parameter contains parameters, like limiting/sorting results by date. |
| `google_safe_search` | `string` | Used to hide explicit content from the results. |
| `stars` | `integer` | 1-5 stars, used with ```google_travel_hotels``` target |
| `guests` | `integer` | Used with ```google_travel_hotels``` target |
| `date_range` | `string` | Y-m-d,Y-m-d used with ```google_travel_hotels``` target |
| `headless` | `string` | Enable JavaScript rendering. Supported: ```html```, ```png``` |

## Targets

### List of supported targets for the 'target' parameter
```
google_search
google_hotels
google_travel_hotels
google_shopping_search
google_shopping_product
google_shopping_pricing
google
google_images
google_suggest
google_ads
google_trends_explore
baidu
baidu_search
bing
bing_search
yandex
yandex_search
```

## Languages

| ISO 639-1 Code | Language     |
| :-------- | :------- |
| `af` |	`Afrikaans` |
| `ar` |	`Arabic` |
| `hy` |	`Armenian` |
| `be` |	`Belarussian` |
| `bg` |	`Bulgarian` |
| `ca` |	`Catalan` |
| `zh-CN` |	`Chinese - Simplified` |
| `zh-TW` |	`Chinese - Traditional` |
| `hr` | 	`Croatian` |
| `cs` |	`Czech` |
| `da` |	`Danish` |
| `nl` |	`Dutch` |
| `en` |	`English` |
| `eo` |	`Esperanto` |
| `et` |	`Estonian` |
| `tl` |	`Filipino` |
| `fi` |	`Finnish` |
| `fr` |	`French` |
| `de` |	`German` |
| `el` |	`Greek` |
| `ie` |	`Hebrew` |
| `hi` |	`Hindi` |
| `hu` |	`Hungarian` |
| `is` |	`Icelandic` |
| `id` |	`Indonesian` |
| `it` |	`Italian` |
| `ja` |	`Japanese` |
| `ko` |	`Korean` |
| `lv` |	`Latvian` |
| `lt` |	`Lithuanian` |
| `no` |	`Norwegian` |
| `fa` |	`Persian` |
| `pl` |	`Polish` |
| `pt` |	`Portuguese` |
| `ro` |	`Romanian` |
| `ru` |	`Russian` |
| `sr` |	`Serbian` |
| `sk` |	`Slovak` |
| `sl` |	`Slovenian` |
| `es` |	`Spanish` |
| `sw` |	`Swahili` |
| `sv` |	`Swedish` |
| `th` |	`Thai` |
| `tr` |	`Turkish` |
| `uk` |	`Ukrainian` |
| `vi` |	`Vietnamese` |

## Response Codes

### HTTP Response Codes

| Response | Description     | Solution                |
| :-------- | :------- | :------------------------- |
| **200** - Success | Server has replied and given requested response.	 | Celebrate! |
| **204** - No content | Job not completed yet. | Wait a few seconds before trying again. |
| **400** - Multiple error messages | Bad structure of the request. | Re-check your request to make sure it is in the correct format. |
| **401** - Invalid / not provided authorization header (client not found) | Incorrect login credentials or missing authorization. | Re-check your provided credentials for authorization. |
| **403** - Forbidden | Your account does not have access to this resource. | Make sure the target is supported by us |
| **404** - Not found | Your target was not found. | Re-check your targeted URL. |
| **429** - Too many requests | Exceeded rate limit for your subscription. | Make sure you still have at least one request left. Wait a couple minutes and try again. If you are encountering the error often – chat with us to see if your rate limit can be increased. |
| **500** - Internal error | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |
| **524** - Timeout | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |

### Parsed Result Response Codes

| Response | Description |
| :-------- | :------- | 
| **12000** - Success | Server has replied and given the requested response. |
| **12002** - Error | Parsing has failed completely. |
| **12003** - Not supported | Targeted website parsing is not supported. |
| **12004** - Response not full | Some fields were not parsed and are missing. |
| **12005** - Response not fully parsed | Some fields might not have been parsed and are returned unparsed. |
| **12006** - Error | Unexpected error. Let us know the task ID and we will check what went wrong. |
| **12007** - Unknown | We could not determine whether the data was parsed correctly. |
| **12008** - Error | Failed to parse all the data. |
| **12009** - Error | Target not found. Make sure the parameters you passed are correct and supported. |

## Postman Collection

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/23304112-1d93adb3-88f5-4dd5-ae14-22a52b99c6f9?action=collection%2Ffork&collection-url=entityId%3D23304112-1d93adb3-88f5-4dd5-ae14-22a52b99c6f9%26entityType%3Dcollection%26workspaceId%3D52705bab-433c-4fbf-afce-ccbfc97430fe)


## License

All code is released under [MIT License](https://github.com/Smartproxy/Smartproxy/blob/master/LICENSE)
