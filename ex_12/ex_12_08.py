# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter Count -')
position = input('Enter position -')

count = int(count)
position = int(position)

URLS = list()

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print("Retrieving:" , url)
# Retrieve all of the anchor tags
tags = soup('a')
c = 0

while c < count:
    p=1
    for tag in tags:
            #print(tag.get('href', None))
        URL = tag.get('href', None)
        if p == position :
            print("Retrieving:" , URL)
            html = urllib.request.urlopen(URL, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            c= c + 1
            break
        else :
            p = p + 1
