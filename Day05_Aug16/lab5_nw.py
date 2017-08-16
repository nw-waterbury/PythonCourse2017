# pip install googlemaps
from googlemaps import Client
from datetime import datetime


api_key = 'yourkey'
gmaps = Client('a key')
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whitehouse_geoloc = gmaps.geocode(whitehouse)
print whitehouse_geoloc

destination = gmaps.reverse_geocode((38.897096, -77.036545))
print destination

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

lat_long = (gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lat'], gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lng'])
print lat_long
duke = gmaps.reverse_geocode(lat_long)[0]['formatted_address']
print duke

local = gmaps.places('restaurant near ' + duke)
print local['results'][0]['formatted_address']
print local['results'][0]['name']

directions = gmaps.directions(duke, whitehouse)
print directions[0]['legs'][0]['distance']

for step in directions[0]['legs'][0]['steps']:
	print step['html_instructions']
embassies= [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427],
	[38.916944, -77.048739] ]

def nearest_embassy(wh, embassy_list):
    e_dist = distances(wh, embassy_list)
    shortest = min(e_dist)
    identify = e_dist.index(shortest)
    print "This is the closest location: %s."  %(embassy_list[identify])
    adres=address(embassy_list[identify])
    print "It is located at this address: %s." % (adres)
    return identify


def distances(wh, embassy_list):
	wh_emb_dist = []
	if type(wh) != str:
		wh = gmaps.reverse_geocode(wh)[0]['geometry']['location']
	for place in embassy_list:
		latlong = gmaps.reverse_geocode(place)[0]['geometry']['location']
		dist = gmaps.distance_matrix(wh, latlong)
		wh_emb_dist.append(dist['rows'][0]['elements'][0]['distance']['value'])
	return wh_emb_dist

def address(embassy):
	return gmaps.reverse_geocode(embassy)[0]['formatted_address']

def nearest_venue(wh, embassy_list, venue):
    near = nearest_embassy(wh, embassy_list)
    embassy = wh[near]
    search = gmaps.places(query = venue, location = embassy)['results']
    possibilities = []
    for hit in search:
        location = hit['geometry']['location']
        latlong = [location['lat'], location['lng']]
        possibilities.append(latlong)
    near_venue = nearest_embassy(embassy, possibilities)
    venue_name=str(search[near_venue]['name'])
    return venue_name



nearest_venue(whitehouse, embassies, 'cafe in DC')


nearest_venue(whitehouse, embassies, 'bars in DC')
