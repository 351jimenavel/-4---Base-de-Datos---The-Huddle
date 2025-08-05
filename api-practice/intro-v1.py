'''Archivo para practicar el uso de APIs en Python'''
import requests
import json

response = requests.get("https://dogapi.dog/api/v2/breeds")
print(response.status_code)

#res = json.loads(response.text)
#print(res)
res = response.json()

# Recorrer los datos y extraer el nombre y la descripción
for breed in res['data']:
    name = breed['attributes']['name']
    description = breed['attributes']['description']
    print(f"Name: {name}")
    print(f"Description: {description}")
    print()  # Solo para separar cada raza
    