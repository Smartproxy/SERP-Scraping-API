<?php

$params = array(
    'target' => 'google_trends_explore',
    'query' => 'pizza',
    'search_type' => 'web_search',
    'date_start' => '2022-01-10',
    'date_end' => '2023-01-10',
    'geo' => 'US',
    'locale' => 'en-us',
    'device_type' => 'desktop'
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://scrape.smartproxy.com/v1/tasks');
curl_setopt($ch, CURLOPT_USERPWD, 'SPusername' . ':' . 'SPpassword');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
curl_setopt($ch, CURLOPT_POST, 1);

$headers = array();
$headers[] = 'Content-Type: application/json';
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
echo $result;

if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close ($ch);
?>