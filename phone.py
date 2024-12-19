import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

Key="6d6f969fd9024ac8afde957f0c86a5ba"

check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)

from phonenumbers import carrier
service_number=phonenumbers.parse(number)
print(carrier.name_for_number(service_number,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(Key)
query=str(number_location)
result=geocoder.geocode(query)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
