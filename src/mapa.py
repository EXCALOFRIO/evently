import folium
import webbrowser

mapa = folium.Map(location=[40.43518307438477, -3.719169233367488], zoom_start=11)

tooltip = 'Click For More Info'

#markers de discotecas
popupNuit=folium.Popup('<p><strong>NUIT</strong> <br> <strong>Dirección:</strong> Calle de Orense, 10 </p>', max_width=200)
popupBH=folium.Popup('<p> <strong>BLACKHAUS</strong> <br> <strong>Dirección:</strong> Ctra. de La Coruña, Km. 8.700 </p>', max_width=200)
popupLemon=folium.Popup('<p><strong>LEMON</strong> <br> <strong>Dirección:</strong> C. de Orense, 14, 28020 Madrid </p>', max_width = 200)
popupPanda=folium.Popup('<p><strong>PANDA CLUB</strong> <br> <strong>Dirección:</strong> C. de Hernani, 75, 28020 Madrid </p>', max_width = 200)
popupKapital=folium.Popup('<p><strong>KAPITAL CLUB</strong> <br> <strong>Dirección:</strong> C. de Atocha, 125, 28012 Madrid</p>', max_width = 200)
popupFabrik=folium.Popup('<p><strong>FABRIK CLUB</strong> <br> <strong>Dirección:</strong> Av. de la Industria, 82, 28970 Humanes de Madrid, Madrid</p>', max_width = 200)
popupRiviera=folium.Popup('<p><strong>RIVIERA CLUB</strong> <br> <strong>Dirección:</strong> P.º Bajo de la Virgen del Puerto, S/N, 28005 Madrid</p>', max_width = 200)


folium.Marker([40.449073632580344, -3.695012540855487], 
    popup=popupNuit, 
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.4612885534134, -3.766631098984334], 
    popup=popupBH, 
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.4493493,-3.6970928],
    popup = popupLemon,
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.4481601,-3.6981713],
    popup = popupPanda,
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.4097611,-3.695297],
    popup = popupKapital,
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.2654555,-3.8449708],
    popup = popupFabrik,
    tooltip=tooltip).add_to(mapa)

folium.Marker([40.4129999,-3.7243401],
    popup = popupRiviera,
    tooltip=tooltip).add_to(mapa)

mapa.save('mapa.html')
webbrowser.open('mapa.html')
