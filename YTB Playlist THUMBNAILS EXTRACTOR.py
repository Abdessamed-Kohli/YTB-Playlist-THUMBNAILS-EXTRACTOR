# Author : Mr. ABDESSAMED Kohli
# Degree : MASTER Degree in Info Security, from USTHB Algiers, Algeria
# Source Code Name : 'ABDOU YTB Playlist THUMBNAILS EXTRACTOR'
# Programing Language : Python
# Source Code Description :
#     1. execute first 'web_browser_youtube_playlist_extractor.js' in your web browser console
#     2. save the 2 outputs in 'videos_names.txt' and 'thumbnails_urls.txt'
#     3. this Python script will download and save All the playlist THUMBNAILS inside a new Folder
# Source Code Version : 1.0
# Source Code Last updated : 2021-09-18
# Welcome to Contact Us : 
#     Social Media : www.facebook.com/abdessamed.kohli.certified

import os
import re
import requests
import tqdm

# def Extract_videos_URLS_via_youtube_dl_get_thumbnails():
#     cmd = "youtube-dl {playlist_url} --get-thumbnails"
#     # Optional save them into a file
#     return


# def getFilename_from_cd(http_content_disposition_header):
#     if not http_content_disposition_header:
#         return "No content-disposition http header"
#     fname = re.findall('filename=(.+)', cd)
#     if len(fname) == 0:
#         return "no filename"
#     return fname[0]

print("\n\n")
print("---- WELCOME to << ABDOU YTB Playlist THUMBNAILS EXTRACTOR >> V 1.0 ----\n")

# GETITNG REQUIRED INPUT
print('[Getting Configuration Ready ...]')

# VIA GOOGLE CHROME JS CONSOLE and XPATH $().
# Manually Extract / SAVE / Prepare :
# + VIDEO NAMES for ex to "videos_names.txt"
# + URLS for ex to "thumbnails_urls.txt"

VIDEOS_NAMES_TXT_FILE = "videos_names.txt"  # this is to put manually
THUMBNAILS_URLS_TXT_FILE = "thumbnails_urls.txt"  # this is to put manually

answer = input(
    f'if {VIDEOS_NAMES_TXT_FILE} and {THUMBNAILS_URLS_TXT_FILE} are ready press [Yes]: ')
if answer != "Yes":
    print('[Error] your Configuration was not ready.\n')
    exit()

default_playlist_url = "https://www.youtube.com/playlist?list=PLP0aqyZ5GFdlb7MtCHYNZwUlGhY1BkMS_"

playlist_url = input("Enter Playlist URL [Press Enter for default] : ")
if not playlist_url:
    playlist_url = default_playlist_url
else:
    playlist_url = str(playlist_url).strip()

print('\n\n')

print('[ALL REQUIRED INPUTS WAS GATHERED, PROCESSING IS STARTING ... ]')

# get_list_of_lines_from_file
VIDEO_NAMES_LIST = open(VIDEOS_NAMES_TXT_FILE, 'rt').read().strip().split("\n")

# get_list_of_lines_from_file
THUMBNAILS_URLS_LIST = open(
    THUMBNAILS_URLS_TXT_FILE, 'rt').read().strip().split("\n")
# some thumbnails are available in other format like
# https://img.youtube.com/vi/YSl6bordSh8/0.jpg
# and not available as
# https://img.youtube.com/vi/6Swt51w3EjY/maxresdefault.jpg

PLAYLIST_ID = re.findall(r"list\=(.{34})", playlist_url)[0]

# MAKING AND PREPARING A NEW FOLDER FOR LOCAL STORAGE
# PARENT_FOLDER = f"./my_playlist_demo/"
PARENT_FOLDER = f"./Playlist_{PLAYLIST_ID}/"
try:
    os.makedirs(PARENT_FOLDER, 0o777, exist_ok=True)
    print(f'[SUCCESS] {PARENT_FOLDER} folder was created')
except Exception as e:
    print('[Error], {PARENT_FOLDER} folder could not be created ')
    raise e

i = 0
url_errors = []
error_indexes = []
for url in tqdm.tqdm(THUMBNAILS_URLS_LIST):
    url = url.strip()
    # if is_downloadable(url) and req.headers.get('content-type') == "image/png":
    req = requests.get(url, allow_redirects=True)
    # if (req.status_code != "200")
    if not (req.ok):
        print("\n\n error : not (req.ok)")
        url_errors.append(url)
        error_indexes.append(i+1)
        continue

    # REMOVE BAD CHARS iN ORDER TO BE A VALID WINDOWS FILENAME
    VIDEO_NAMES_LIST[i] = re.sub(r'[\\/:"*?<>|]+', "", VIDEO_NAMES_LIST[i])
    newfilename = PARENT_FOLDER + VIDEO_NAMES_LIST[i] + '.jpeg'
    fd = open(newfilename, "wb")
    fd.write(req.content)
    fd.close()
    i += 1

if len(url_errors) != 0:
    print(error_indexes)
    for mytuple in enumerate(url_errors):
        print(mytuple)
    print(
        f"[{len(url_errors)} Errors encountered], only {i} files have been downladed.")
else:
    print(f"[SUCESS], All {i} files have been downladed")

print("[Program Ended] \n")
