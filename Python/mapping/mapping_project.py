import folium
import pandas

data = pandas.read_csv("Oregon-Volcanoe.csv")
#Create a Python list for the latitude variables from the data
lat = list(data["LAT"])
#Creates a Python list for the longitude variable list from data
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_icon(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 2000:
        return 'orange'
    else:
        return 'red'

#Creates a map object Places Portland, OR at center of map with 10x zoom
map = folium.Map(location=[45.410088, -122.639920],zoom_start=6, tiles="Mapbox Bright")

#Makes a child Feature Group for all of the markers and calls it "My Map"
fgv = folium.FeatureGroup(name="Volcanoes")

#Iterating with for loop with list of coordinates to place markers
for lt, ln, el, nm in zip(lat, lon, elev, name):
    #The popup needs the variable to be a string, so str must be associated with el to convert to string
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=nm+" - "+str(el)+" meters", fill_color=color_icon(el),color='grey', fill_opacity=0.6))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig'),
                            style_function=lambda x: {'fillColor':'yellow' if x ['properties']['POP2005'] < 9999999
                            else 'blue' if 10000000 <= x ['properties']['POP2005'] < 100000000
                            else 'orange' }))

#Ask the user to input what name to call the file
map_name = input("What name would you like to save the map to?: ")
#Makes the user input name into a html file
name_map = map_name+".html"
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
#Saves the map to user inputted name
map.save(name_map)