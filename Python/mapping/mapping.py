import folium

map  = folium.Map
#Creates a map object Places Portland, OR at center of map with 10x zoom
map = folium.Map(location=[45.410088, -122.639920],zoom_start=10, tiles="Mapbox Bright")

#Makes a child Feature Group for all of the markers and calls it "My Map"
fg = folium.FeatureGroup(name="My Map")

#Iterating with for loop with list of coordinates to place markers
for coordinates in [[45.410088, -122.639920],[46.1, -123.12],[44.123, -121.5]]:
    map.add_child(folium.Marker(location=coordinates, popup="Marker", icon=folium.Icon(color="orange")))


#Ask the user to input what name to call the file
map_name = input("What name would you like to save the map to?: ")
#Makes the user input name into a html file
name_map = map_name+".html"
map.add_child(fg)
#Saves the map to user inputted name
map.save(name_map)