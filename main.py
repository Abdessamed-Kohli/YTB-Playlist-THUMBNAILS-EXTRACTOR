import os
import re
import requests
import tqdm

from mylib import *

print("\n\n")
print("---- WELCOME TO YTB Playlist THUMBNAILS EXTRACTOR  -----------\n")

# GETITNG REQUIRED INPUT
p0 = "https://www.youtube.com/playlist?list=PLh94XVT4dq02frQRRZBHzvj2hwuhzSByN"
p1 = "https://www.youtube.com/playlist?list=PLP0aqyZ5GFdlb7MtCHYNZwUlGhY1BkMS_"

default_playlist_url = p1

playlist_url = input(
    "Go type xpath in ur browser, Enter Playlist URL [Press Enter for default] : ")
if not playlist_url:
    playlist_url = default_playlist_url
else:
    playlist_url = str(playlist_url).strip()

# VIA GOOGLE CHROME JS CONSOLE and XPATH $().
# Manually Extract/ SAVE / Prepare
    # + VIDEO NAMES to "videos_names.txt"
    # + URLS to "thumbnails_urls.txt"

path1 = "videos_names.txt"
# file1 --> 01_file1
# file2 --> 02_file2
path2 = "videos_names_index.txt"
add_index_in_lines(path1, path2)
video_names_list = get_list_of_lines_from_file(path2)

thumbnails_urls_txt_file = "thumbnails_urls.txt"
# some thumbnails are available in other format like
# https://img.youtube.com/vi/YSl6bordSh8/0.jpg
# and not available as
# https://img.youtube.com/vi/6Swt51w3EjY/maxresdefault.jpg
thumbnails_urls_list = get_list_of_lines_from_file(thumbnails_urls_txt_file)

playlist_ID = re.findall(r"list\=(.{34})", playlist_url)

# making and preparing a new folder for local storage
parent_folder = f"./{playlist_ID}/"
os.makedirs(parent_folder, 0o777, exist_ok=True)

i = 0
url_errors = []
error_indexes = []
for url in tqdm.tqdm(thumbnails_urls_list):
    url = url.strip()
    # if is_downloadable(url) and req.headers.get('content-type') == "image/png":
    req = requests.get(url, allow_redirects=True)
    # if (req.status_code != "200")
    if not (req.ok):
        print("\n\n error : not (req.ok)")
        url_errors.append(url)
        error_indexes.append(i+1)
        continue

    # SANITIZE IT TO BE A VALID WINDOWS FILENAME
    video_names_list[i] = re.sub(r'[\\/:"*?<>|]+', "", video_names_list[i])
    newfilename = parent_folder + video_names_list[i] + '.jpeg'
    fd = open(newfilename, "wb")
    fd.write(req.content)
    fd.close()
    i += 1

if len(url_errors) != 0:
    print(error_indexes)
    for mytuple in enumerate(url_errors):
        print(mytuple)
    print(f"{len(url_errors)} Errors encountered, only {i} files have been downladed.")
else:
    print(f"SUCESS, All {i} files have been downladed")

print("[Program Ended]")
