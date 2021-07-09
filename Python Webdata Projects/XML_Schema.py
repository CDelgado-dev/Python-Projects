import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

Sums=0

url = input('Enter - ')
print('Received - ', url)
html = urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')
data = ET.fromstring(html)
lst = data.findall('comments/comment')
print('Comment Count:', len(lst))
for item in lst:
    #print('Name',item.find('name').text)
    #print('Count', item.find('count').text)
    Sums= Sums+ int(item.find('count').text)
print('Sum of all Counts', Sums)
