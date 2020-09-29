#Import libraries
import folium
import pandas

#Load the data
data = pandas.read_csv("Volcanoes.txt")
latitude = list(data['LAT'])
longitude = list(data['LON'])
elevation = list(data['ELEV'])

#Function to create color ranges in
def colour_range(elevation):
        if elevation < 1200:
            return "darkgreen"
        elif 1200 <= elevation >2000:
            return "orange"
        else:
            return "red"

map = folium.Map(location = [38.58, -99.89], zoom_start=6, tiles = "Stamen Terrain")

#Create a feature group for volcano map
fgv = folium.FeatureGroup(name="Volcanoes")


for i,j,k in zip(latitude, longitude, elevation):
    fgv.add_child(folium.CircleMarker(location=[i,j], radius = 6, popup=str(k) +" M", fill_color=colour_range(k), color="grey", fill_opacity=0.7))

#Create another feature group for population map
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'yellow' if 10000000 > x['properties']['POP2005'] < 40000000 else
'orange' if 40000000 > x['properties']['POP2005'] < 80000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
