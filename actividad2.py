import requests
import json
import os

lat = input("ingrese la latitud de la ciudad o lugar")
lon = input("ingrese la longitud de la ciudad o lugar")
response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=current&appid=0d1ba8366475ed621225954b1b482734')
clim = response.json()
print(clim)
print(f"temperatura: {clim['temp']}")
print(f"sensacion termica: {clim['feels_like']}")
print(f"humedad: {clim['humidity']}")
print(f"descripcion del clima: {clim['description']}")