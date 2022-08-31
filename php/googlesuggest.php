<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://scrape.smartproxy.com/v1/tasks', [
  'body' => '{"target":"google_images","query":"https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg","parse":false,"geo":"London,England,United Kingdom"}',
  'headers' => [
    'Accept' => 'application/json',
    'Authorization' => 'Basic U1B1c2VybmFtZTpTUGFzc3dvcmQ=',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();