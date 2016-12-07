#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os
import requests
import re

urls = []

def urlcheck():
    global urls
    s = requests.Session()
    s.headers.update({"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"})
    r = s.get("http://thecladdagh.com/webcam")
    for i in re.findall('rtmp:[\.\/:A-Za-z0-9]{,200}', str(r.content)):
        print(i)
        urls.append(i)

def pickplayer():
    if os.system("uname -m") == "armv61":
        print("is arm")
        return "omxplayer "
    else:
        print("not arm")
        return "mplayer " 

def play(command, stream):
    os.system(command + str(urls[stream]))

if not urls:
    urlcheck()
else:
    pass

#savedUrl = str(open("$USER/.config/whatsitlikeout").read())
print('Press 0 for shop street\nPress 1 for High\ Street')
stream = int(input())
command = pickplayer()
play(command, stream)
