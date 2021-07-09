import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#variables
pos = 18
jumps = 7
count = 0
i= 0

while i != jumps:
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        count+=1;
        #print(count)
        if count == pos:
            holder = tag.get('href', None)
            count = 0
            i+= 1
            print(holder)
            html = urllib.request.urlopen(holder, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            break
