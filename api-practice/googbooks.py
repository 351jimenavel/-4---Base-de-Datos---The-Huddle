import os
import time
import requests
import json


with open('libros_scrapeados.json', 'r', encoding='utf-8') as f:
    libros = json.load(f)

####################
# Testo 1 de la API. Objetivo: que devuelva un response 200 (todo ok)
'''def obtener_autor_por_titulo(titulo): # tendra titulo como parametero
    url_libro = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo}&key={API_KEY}"
    url_request= requests.get(url_libro)
    respuesta = url_request.json()
    #print(url_request)
    #print(respuesta)

    ### devuelve todos los authors del json
    # for item in respuesta['items']:
    #     volumen_info = item.get('volumeInfo', {})
    #     authors = volumen_info.get('authors', ['Desconocido'])
    #     print(authors)

    ###### devuelve la primera informacion rescatada del json

    if respuesta['items']:
        primer_resultado = respuesta['items'][0]['volumeInfo']
        if 'authors' in primer_resultado:
            autor = primer_resultado['authors']
            print(autor)
        else:
            autor = ['Desconocido']
            print(autor)
    else:
        print('No se encontro el libro')

obtener_autor_por_titulo('flowers')'''
####################

####################
# Testeo 2. Probar que devuelva los 3 autores de los 3 primeros libros
def obtener_autor_por_titulo(titulo):

    url_libro = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{titulo}&key={API_KEY}"
    try:
        url_request= requests.get(url_libro)
        respuesta = url_request.json()

        if respuesta['items']:
            autores = respuesta['items'][0]['volumeInfo'].get('authors',[])       # get es un metodo de diccionario que tiene la siguiente sintaxis --> 'dictionary.get(keyname, value)'
            return autores
        else:
            return ['Desconocido']

    except Exception as e:
        return [str(e)]
    
for libro in libros[:3]:  # Solo los 3 primeros
    titulo = libro['Titulo']
    autores = obtener_autor_por_titulo(titulo)
    libro['Autores'] = autores
    print(f"[yes!] {titulo} --> {autores}")

####################

####################
# Parte del testeo 3. Extraer todo los autores + guardarlos en un json (proximamente)
'''contador = 0
for libro in libros:
    contador +=1
    titulo = libro['Titulo']
    autores = obtener_autor_por_titulo(titulo)  # Acá es el llamado a la función
    libro['Autores'] = autores
    print(f"[{contador}] {titulo} → {autores}")
    time.sleep(1)

print('---- TERMINADO ----')

# crear el archivo json (abrirlo en modo de escritura)
with open("autores_googlebooks.json", "w", encoding="utf-8") as f:
    json.dump(libros, f, ensure_ascii=False, indent=2)

# Leer y mostrar uno para verificar
with open('autores_googlebooks.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
    print(f'Se guardaron {len(datos)} libros')
    print(datos[0])  # Validar estructura

# Abrir el archivo si estás en Windows
os.startfile('autores_googlebooks.json')'''

####################
