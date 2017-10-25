import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address})

    url = urllib.parse.urlencode({address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print(data)
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)
    print(tree)

    results = tree.findall('result')
    #print(results)
