<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://scrape.smartproxy.com/v1/tasks', [
  'body' => '{"target":"google_suggest","query":"world","parse":false}',
  'headers' => [
    'Content-Type' => 'application/json',
    'accept' => 'application/json',
    'authorization' => 'Basic U1B1c2VybmFtZTpTUHBhc3N3b3Jk',
  ],
]);

echo $response->getBody();