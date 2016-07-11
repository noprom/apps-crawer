<?php

$category_url = "http://app.xiaomi.com/category/1#page=0";

$category_html = `curl -s $category_url`;
$category_html = preg_replace("/[\t\n\r]+/", "", $category_html);
$category_html = str_replace('data-pin-nopin="true"', "", $category_html);
$category_html = str_replace('width="72"', "", $category_html);
$category_html = str_replace('height="72"', "", $category_html);
print_r($category_html);

// 匹配正则
$partern = '@<ul id="all-applist" class="applist">([.*?]+)<\/ul>@';

// 匹配结果
preg_match_all($partern, $category_html, $result);

// 打印结果  
var_dump($result);

// ([^<>]+)

// // $partern = '~<li><a href="\/details?id=([^<>]+)"><img data-src="([^<>]+)" src="([^<>]+)" alt="([^<>]+)"  ><\/a><h5><a href="\/details?id=([^<>]+)">([^<>]+)<\/a><\/h5><p class="app-desc"><a href="([^<>]+)">([^<>]+)<\/a><\/p><\/li>~';
// $partern = '~<li><a href="/details?id=([^<>]+)"><img data-src="([^<>]+)" src="([^<>]+)" alt="([^<>]+)"  ></a><h5><a href="/details?id=([^<>]+)">([^<>]+)</a></h5><p class="app-desc"><a href="([^<>]+)">([^<>]+)</a></p></li>~';

// '<li><a href="/details?id=(.+)"><img data-src="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0d65a50b0d2434d592da6becf12ccebc03243a727" src="http://resource.xiaomi.net/miuimarket/app/lazyload.gif" alt="同花顺-股票炒股" width="72" height="72"></a><h5><a href="/details?id=com.hexin.plat.android">同花顺-股票炒股</a></h5><p class="app-desc"><a href="/category/1">金融理财</a></p></li>';

// $html='  
// <div class="goods">  
//     <a href="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0d65a50b0d2434d592da6becf12ccebc03243a727" target="_blank">  
//         <img data-ks-lazyload="http://1111.jpg" alt="金融理财" width="" height=""/>  
//     </a>  
// </div>  
// <div class="goods">  
//     <a href="http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0d65a50b0d2434d592da6becf12ccebxcas3243a727" target="_blank">  
//         <img data-ks-lazyload="http://2222.jpg" alt="金融理财2" width="" height=""/>  
//     </a>  
// </div>  
// <div class="goods">  
//     <a href="http://file.market.xiaomi.com/thumbnail/PNG/l63/AppStore/0d65a50b0d2434d592da6becf12ccebc03243a727" target="_blank">  
//         <img data-ks-lazyload="http://3333.jpg" alt="金融理财3" width="" height=""/>  
//     </a>  
// </div>';

// //去掉换行、制表等特殊字符，可以echo一下看看效果  
// $html = preg_replace("/[\t\n\r]+/", "", $html); 

// print_r($html);
// //匹配表达式，注意两点，一是包含在'/ /'里面，再就是/要做转义处理成\/
// $partern = '~<div class="goods">      <a href="([^<>]+)" target="_blank">          <img data-ks-lazyload="http://([^<>]+)" alt="([^<>]+)" width="" height=""/>      </a>  </div>~';

// //匹配结果
// preg_match_all($partern,$html,$result);   

// //打印结果  
// var_dump($result);