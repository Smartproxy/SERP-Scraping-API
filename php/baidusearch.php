<?php

$params = array(
    'target' => 'baidu',
    'url' => 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=donuts&fenlei=256&rsv_pq=dc12cef9000cecd5&rsv_t=eb7dbdneGaOeG8buqmqpjMaLZ8tiygOJCtkEqqboaIRy1vnbiFlpef4ieJg&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=6940&rsv_sug4=6940',
    'parse' => False
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://scraper-api.smartproxy.com/v2/scrape');
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
