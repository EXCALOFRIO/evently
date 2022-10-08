import folium
import webbrowser

mapa = folium.Map(location=[40.43518307438477, -3.719169233367488], zoom_start=10)

tooltip = 'Click For More Info'

#markers de discotecas
popupNuit=folium.Popup('<p><strong>NUIT</strong> <br> <strong>Dirección:</strong> Calle de Orense, 10 </p>', max_width=200)
popupBH=folium.Popup('<p> <strong>BLACKHAUS</strong> <br> <strong>Dirección:</strong> Ctra. de La Coruña, Km. 8.700 </p>', max_width=200)

folium.Marker([40.449073632580344, -3.695012540855487], 
              popup=popupNuit, 
              tooltip=tooltip).add_to(mapa)
folium.Marker([40.4612885534134, -3.766631098984334], 
              popup=popupBH, 
              tooltip=tooltip).add_to(mapa)

mapa.save('mapa.html')
webbrowser.open('http://127.0.0.1:5501/mapa.html')
