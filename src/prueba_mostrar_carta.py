import itertools
import re
import time
import email
from operator import ge
from tkinter import N
from turtle import color
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="evently")
cred = credentials.Certificate("firebase/evently-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
})

def mostrar_carta(discoteca, ruta):
    ref = db.reference(ruta+ '/'+discoteca)
    snapshot = ref.equal_to(discoteca).get()
    for key in snapshot:
        print(key)

mostrar_carta('B12')