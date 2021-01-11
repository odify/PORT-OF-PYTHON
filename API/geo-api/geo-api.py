from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML

api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'

address = input('Enter location: ')
if len(address) < 1:
    address = "Langenfeld, Germany"
url = api_url + ENCODE({'sensor': 'false', 'address': address})
print ('\nRetrieving location for:', address)
data = OPEN(url).read()
tree = XML.fromstring(data)

res = tree.findall('result')

lat = res[0].find('geometry').find('location').find('lat').text
lng = res[0].find('geometry').find('location').find('lng').text
lat = float(lat)
lng = float(lng)
if lat < 0:
    lat_c = chr(167)+'S'
else:
    lat_c = chr(167)+'N'
if lng < 0:
    lng_c = chr(167)+'W'
else:
    lng_c = chr(167)+'E'

location = res[0].find('formatted_address').text
location_type = res[0].find('geometry').find('location_type').text
place_id = res[0].find('place_id').text

url = 'http://maps.googleapis.com/maps/api/place/details/xml?'

data = OPEN(url).read()
tree = XML.fromstring(data)
res = tree.findall('status')[0].text


print("\n==>", location, "<==")
print('Latitude: {0:.3f}{1}'.format(abs(lat), lat_c))
print('Longitude: {0:.3f}{1}'.format(abs(lng), lng_c))
print('Location type:', location_type)
print('Place ID:', place_id)
print('Rating:', res)
