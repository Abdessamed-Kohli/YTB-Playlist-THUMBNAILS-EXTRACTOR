// Author : Mr. ABDESSAMED Kohli
// Degree : Master Degree (Info Security), USTHB Algiers, Algeria
// Source Code Name : 'web_browser_youtube_playlist_extractor'
// Programing Language : JS
// Source Code Description : 
    // To Run it : Open the Youtube playlist you want, open your browser Dev Tools Console and execute this JS script
    // The Result : you will see 2 outputs : videos_titles_list + videos_thumbnails_urls
// Source Code Version : 1.0
// Source Code Last updated : 2021-09-18
// Welcome to Contact Us : 
//     Social Media : www.facebook.com/abdessamed.kohli.certified

url_playlist_demo = "https://www.youtube.com/playlist?list=PLP0aqyZ5GFdlb7MtCHYNZwUlGhY1BkMS_"

ytb_playlist_videos_xpath = '//*[@id="video-title"]';
// const my_xpath = '';
vid_id_regex = /v\=(.{11})&/g;

videos_titles_list = [];
videos_thumbnails_urls = [];

// xpath return an array of HTML TAGS
indexing = true;
index = 1;
$x(ytb_playlist_videos_xpath).forEach( function(curr_html_tag){
    
    video_title = curr_html_tag.getAttribute("title");
    
    if (indexing == true){
        video_title = index.toString().padStart(2,0) + '_' + video_title;
        index++;
    }

    videos_titles_list.push(video_title);

    href = curr_html_tag.getAttribute("href");

    // vid_id_regex.test(href) == true;
    // VIA REGEXP CAPTURING
    myarr = [...href.matchAll(vid_id_regex)];
    curr_vid_id = myarr[0][1];

    // THUMB_URL_DEMO= "img.youtube.com/vi/{VID_ID}/maxresdefault.jpg";
    // THUMB_URL_DEMO= "img.youtube.com/vi/n2D1o-aM-2s/maxresdefault.jpg";
    curr_thumb_url= `https://img.youtube.com/vi/${curr_vid_id}/maxresdefault.jpg`;
    
    videos_thumbnails_urls.push(curr_thumb_url);
});

console.log(videos_titles_list.join(separator="\n"));
console.log("\n")
console.log(videos_thumbnails_urls.join(separator="\n"));
console.log("\n")
