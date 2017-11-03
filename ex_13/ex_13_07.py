import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json

url = input('Enter location: ')



print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(data)

try:
    js= json.loads(data)
except:
    js = None

print(js)

i=0
length = len(js["comments"])
sum = 0
print(length)
while i < length:
    count=js["comments"][i]["count"]
    counts=int(count)
    sum = sum + counts
    #print(count)
    i=i + 1


print(sum)
