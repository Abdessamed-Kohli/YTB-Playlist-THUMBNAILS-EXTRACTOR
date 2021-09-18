import os, re, requests, tqdm

def Extract_videos_URLS_via_youtube_dl_get_thumbnails():
    cmd = "youtube-dl {playlist_url} --get-thumbnails"
    # Optional save them into a file
    return

def getFilename_from_cd(cd):
    """
    getFilename_from_content_disposition
    """
    if not cd:
        return "No content-disposition http header"
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return "no filename"
    return fname[0]

def get_list_of_lines_from_file(path):
    fd = open(path,"r")
    list = fd.read().strip().split("\n")
    fd.close()
    return list

def add_index_in_lines(path, new_filename):
    fd = open(path,"rt")
    new_fd = open(new_filename, "wt")
    i = 1
    for line in fd.readlines():
        new_fd.write(f"{i:02}_" + line)
        i +=1

    fd.close()
    new_fd.close()
    return
