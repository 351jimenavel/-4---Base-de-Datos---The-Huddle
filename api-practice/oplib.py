import os
import time
import requests
import json

with open('libros_scrapeados.json', 'r', encoding='utf-8') as f:
    libros = json.load(f)

'''def obtener_autor_por_titulo(titulo): # tendra titulo como parametero
    #url_libro = "https://openlibrary.org/search.json?title={'A Light in the Attic'}"
    url_libro = f"https://openlibrary.org/search.json?title={titulo}"
    url_request= requests.get(url_libro)
    respuesta = url_request.json()
    #print(url_request)

    # for clave in respuesta['docs']:
    #     author = clave['author_name'][0]
    #     print(author)
    if respuesta['docs']:
        primer_resultado = respuesta['docs'][0]
        if 'author_name' in primer_resultado:
            autor = primer_resultado['author_name']
            print(autor)
        else:
            autor = 'Desconocido'   # o le pongo como []?
            print(autor)
    else:
        print('No se encontro el libro')'''

def obtener_autor_por_titulo(titulo): # tendra titulo como parametero

    url_libro = f"https://openlibrary.org/search.json?title={titulo}"
    try:
        url_request= requests.get(url_libro)
        respuesta = url_request.json()

        if respuesta['docs']:
            autores = respuesta['docs'][0].get('author_name',[])       # get es un metodo de diccionario que tiene la siguiente sintaxis --> 'dictionary.get(keyname, value)'
            return autores
        else:
            return ['Desconocido']

    except Exception as e:
        return [str(e)]
    
contador = 0
for libro in libros:
    contador +=1
    titulo = libro['Titulo']
    autores = obtener_autor_por_titulo(titulo)  # Acá es el llamado a la función
    libro['Autores'] = autores
    print(f"[{contador}] {titulo} → {autores}")
    time.sleep(1)

print('---- TERMINADO ----')

# crear el archivo json (abrirlo en modo de escritura)
with open("autores_extraidos_openlibrary.json", "w", encoding="utf-8") as f:
    json.dump(libros, f, ensure_ascii=False, indent=2)

# Leer y mostrar uno para verificar
with open('autores_extraidos_openlibrary.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)
    print(f'Se guardaron {len(datos)} libros')
    print(datos[0])  # Validar estructura

# Abrir el archivo si estás en Windows
os.startfile('autores_extraidos_openlibrary.json')

#### testeo de solo los 3 primeros
'''
for libro in libros[:3]:  # Solo los 3 primeros
    titulo = libro['Titulo']
    autores = obtener_autores(titulo)
    libro['Autores'] = autores
    print(f"[msg] {titulo} → {autores}")
'''
'''        
obtener_autor_por_titulo('A Light in the Attic')
obtener_autor_por_titulo('Tipping the Velvet')
obtener_autor_por_titulo('Reskilling America: Learning to Labor in the Twenty-First Century')   # output: No se encontro el libro
obtener_autor_por_titulo('Everydata: The Misinformation Hidden in the Little Data You Consume Every Day')   # output: No se encontro el libro
'''