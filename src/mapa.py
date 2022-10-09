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
    for i in range(len(getItemBaseDatos('discotecasEficientes', 'nombre','data'))):
        lista.append(getItemBaseDatos('discotecasEficientes', 'ubicacion', 'data')[i])
    return lista

def getCoordenadas():
    lista = []
    for i in range(len(getUbicacion())):
        location = geolocator.geocode(getUbicacion()[i])
        lista.append([location.latitude, location.longitude])
    return lista



print(getCoordenadas())
mapa.save('mapa.html')
webbrowser.open('mapa.html')
