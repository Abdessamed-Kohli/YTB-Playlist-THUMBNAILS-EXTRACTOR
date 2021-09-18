// Author : Mr. ABDESSAMED Kohli
// Degree : MASTER Degree in Info Security, from USTHB Algiers, Algeria
// Programing Language : JS
// Source Code Description : this code will help you extract HTML tags via Xpath inside the browser console
// Source Code Version : 1.0
// Source Code Last updated : 2021-09-18
// Welcome to Contact Us : 
//     Social Media : www.facebook.com/abdessamed.kohli.certified

var arr1 = [];
var xpath_selector = '//*[@id="video-title"]'
$x( xpath_selector ).forEach( function( curr_html_tag ){
    arr1.push( curr_html_tag.getAttribute("title") );
});
console.log(arr1.join(separator="\n"));