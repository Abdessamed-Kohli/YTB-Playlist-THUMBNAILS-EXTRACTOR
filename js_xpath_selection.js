var arr1 = [];
var xpath_selector = '//*[@id="video-title"]'
$x(xpath_selector).forEach( function(curr_html_tag){
    arr1.push(curr_html_tag.getAttribute("title"));
});
console.log(arr1.join(separator="\n"));