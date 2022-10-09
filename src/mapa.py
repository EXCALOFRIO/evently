import webbrowser
import folium
# python -m pip install geopy
from geopy.geocoders import Nominatim

from baseDatosPrueba import getItemBaseDatos
geolocator = Nominatim(user_agent="evently")
mapa = folium.Map(location=[40.43518307438477, -
                  3.719169233367488], zoom_start=11)

tooltip = 'Click For More Info'

# markers de discotecas
popupNuit = folium.Popup(
    '<p><strong>NUIT</strong> <br> <strong>Dirección:</strong> Calle de Orense, 10 </p>', max_width=200)
popupBH = folium.Popup(
    '<p> <strong>BLACKHAUS</strong> <br> <strong>Dirección:</strong> Ctra. de La Coruña, Km. 8.700 </p>', max_width=200)
popupLemon = folium.Popup(
    '<p><strong>LEMON</strong> <br> <strong>Dirección:</strong> C. de Orense, 14, 28020 Madrid </p>', max_width=200)
popupPanda = folium.Popup(
    '<p><strong>PANDA CLUB</strong> <br> <strong>Dirección:</strong> C. de Hernani, 75, 28020 Madrid </p>', max_width=200)
popupKapital = folium.Popup(
    '<p><strong>KAPITAL CLUB</strong> <br> <strong>Dirección:</strong> C. de Atocha, 125, 28012 Madrid</p>', max_width=200)
popupFabrik = folium.Popup(
    '<p><strong>FABRIK CLUB</strong> <br> <strong>Dirección:</strong> Av. de la Industria, 82, 28970 Humanes de Madrid, Madrid</p>', max_width=200)
popupRiviera = folium.Popup(
    '<p><strong>RIVIERA CLUB</strong> <br> <strong>Dirección:</strong> P.º Bajo de la Virgen del Puerto, S/N, 28005 Madrid</p>', max_width=200)


def getUbicacion():
    lista = []
    for i in range(len(getItemBaseDatos('discotecasEficientes', 'nombre', 'data'))):
        lista.append(getItemBaseDatos(
            'discotecasEficientes', 'ubicacion', 'data')[i])
    return lista


def getCoordenadas():
    lista = []
    for i in range(len(getUbicacion())):
        location = geolocator.geocode(getUbicacion()[i])
        # añaade las coordenadas al mapa
        lista.append([location.latitude, location.longitude])
    return lista


coor = [[40.4461059, -3.6884419], [40.6433958, -4.0390833], [40.42256315, -3.690900189817708], [40.4096055, -3.6926831], [40.4292084, -3.7846342], [40.4096995, -3.6930939], [40.4146728, -3.7212828], [40.4483338, -3.695367], [40.4121176, -3.703293399641577], [40.4513098, -3.6949808],
        [40.4483338, -3.695367], [40.4379481, -3.6921857], [40.4480236, -3.6969828], [40.4483338, -3.695367], [40.40881795, -3.7108497418300646], [40.4269645, -3.6995815], [40.4262559, -3.6957287], [40.4485507, -3.6791346], [40.4203055, -3.7074769], [40.4361601, -3.7165013], [40.5975457, -3.695774]]
# metodo para agarrar lospares de coordenadas y añadirlos al mapa


def pintarPuntos():
    print(len(coor))
    for i in range(len(coor)):
        folium.Marker(coor[i], popup=getItemBaseDatos(
            'discotecasEficientes', 'nombre', 'data')[i], tooltip=tooltip).add_to(mapa)


pintarPuntos()

mapa.save('mapa.html')
webbrowser.open('mapa.html')
