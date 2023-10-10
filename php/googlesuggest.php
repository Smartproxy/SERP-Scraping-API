<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://scraper-api.smartproxy.com/v2/scrape', [
  'body' => '{"target":"google_suggest","query":"world","parse":false}',
  'headers' => [
    'Content-Type' => 'application/json',
    'accept' => 'application/json',
    'authorization' => 'Basic AUTH',
  ],
]);

echo $response->getBody();
