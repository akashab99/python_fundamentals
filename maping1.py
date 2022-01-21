import folium
map = folium.Map(location=[13.107770194956931, 80.09736606793335],zoom_start=10, tiles="Stamen terrain")  

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[13.149617, 80.110622],popup="Hi This is my home", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[8.473853, 76.962236],popup="My home town", icon=folium.Icon(color='blue')))

map.add_child(fg)



map.save("Map1.html")
