const url_playlist_demo = "https://www.youtube.com/playlist?list=PLP0aqyZ5GFdlb7MtCHYNZwUlGhY1BkMS_"

const ytb_playlist_video_xpath = '//*[@id="video-title"]';
// const my_xpath = '';
const vid_id_regex = /v\=(.{11})&/g;

var videos_thumbnails_names = [];
var videos_thumbnails_urls = [];

// xpath return an array of HTML TAGS
$x(ytb_playlist_video_xpath).forEach( function(curr_html_tag){
    var href = curr_html_tag.getAttribute("href");
    
    // vid_id_regex.test(href) == true;
    var myarr = [...href.matchAll(vid_id_regex)];
    // VIA REGEXP CAPTURING
    var curr_vid_id = myarr[0][1];
    
    const thumb_url_demo= "img.youtube.com/vi/n2D1o-aM-2s/maxresdefault.jpg";
    var curr_thumb_url= `https://img.youtube.com/vi/${curr_vid_id}/maxresdefault.jpg`;
    
    videos_thumbnails_urls.push(curr_thumb_url);
    videos_thumbnails_names.push(curr_html_tag.getAttribute("title"));
});

console.log(videos_thumbnails_names.join(separator="\n"));
console.log("\n")
console.log(videos_thumbnails_urls.join(separator="\n"));
