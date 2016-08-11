#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import requests
import re

urls = []

def urlcheck():
    s = requests.Session()
    s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"})
    r = s.get("http://thecladdagh.com/webcam")
    global urls
    for i in re.findall('rtmp:[\.\/:A-Za-z0-9]{,200}', str(r.content)):
        urls.append(i)

def playstream():
    if os.system("uname -o") == "armv61":
        print("is arm")
    else:
        print("not arm")
        os.system("mplayer " +  str(urls[0]))
 
if not urls:
    urlcheck()
    playstream()
else:
    playstream()
