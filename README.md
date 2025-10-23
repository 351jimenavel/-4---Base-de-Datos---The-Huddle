# 📚 Books To Scrape – Data Challenge  
**The Huddle – Penguin Academy**

Autora: Jimena Velázquez  

---

## 🇪🇸 Español

### 🧠 Descripción del Proyecto  
Este desafío consistió en **extraer, estructurar y analizar datos de libros** desde el sitio web [Books to Scrape](https://books.toscrape.com/), con el objetivo de construir una **base de datos relacional completa**, realizar **consultas SQL avanzadas** y explorar el **impacto de la indexación en el rendimiento**.

El proyecto combinó **web scraping legal**, **API consumption**, **limpieza de datos**, y **modelado relacional**, permitiendo integrar información obtenida del sitio y de APIs externas como *Open Library* y *Google Books*.

---

### 🧩 Tecnologías y Herramientas
- **Python** → Web scraping y manejo de datos  
- **BeautifulSoup + Requests** → Extracción de información  
- **SQLite3** → Base de datos relacional  
- **SQLAlchemy** → ORM para manipulación estructurada  
- **APIs externas** → Open Library (prueba) y Google Books (implementación final)  
- **JSON** → Almacenamiento intermedio de los datos  
- **Jupyter Notebook** → Análisis, visualización y documentación

---

### ⚙️ Estructura del Proyecto
| Archivo / Carpeta | Descripción |
|--------------------|-------------|
| `1-scraping-bookstoscrape.ipynb` | Extrae todos los libros y categorías del sitio web. |
| `2-apigooglebooks.py` | Extrae todos los libros y categorías del sitio web. |
| `3-books-database.ipynb` | Crea y puebla DB |
| `4-queries.ipynb` | Contiene consultas, comparaciones con/sin índices y conclusiones. |
| `libros_scrapeados.json` | Contiene los datos brutos del scraping. |
| `autores_extraidos_openlibrary.json` | Resultados obtenidos al probar la API de Open Library (con varios autores desconocidos). |
| `autores_googlebooks.json` | Resultados finales con datos correctos desde la API de Google Books. |
| `diagram_uml.png` | Diagrama UML del modelo relacional. |

---

### 🧠 Ejecución del Proyecto

#### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/-4---Base-de-Datos---The-Huddle.git
cd -4---Base-de-Datos---The-Huddle/entrega
```

#### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows
pip install -r requirements.txt
```

#### 3️⃣ Scraping
Ejecutar el notebook `1-scraping-bookstoscrape.ipynb`
Salida esperada: `libros_scrapeados.json`

#### 4️⃣ Enriquecer los datos con APIs externas
- Opción A: Ejecutar la versión con Open Library dentro de api-practice (oplib.py)
Salida esperada: `autores_extraidos_openlibrary.json`

- Opción B: Ejecutar la versión final con Google Books (2-apigooglebooks.py)
```bash
python 2-apigooglebooks.py
```
Los resultados se guardan en archivos JSON separados para mantener independencia entre fuentes.
Salida esperada: `autores_googlebooks.json`

#### 5️⃣ Base de Datos — abrir el notebook 3-books-database.ipynb
Crea y puebla `books_data.db` (relaciones muchos-a-muchos).

#### 6️⃣ Consultas/Análisis — ejecutar 4-queries.ipynb
Contiene consultas, comparaciones con/sin índices y conclusiones.

---
### 🧬 Modelo Relacional

El modelo de datos implementa relaciones muchos-a-muchos entre libros y autores, además de claves foráneas que conectan categorías y ratings.

El diagrama UML muestra las entidades:
```lua
Autor  ---< LibroAutor >---  Libro  ---< Categoria
```

---
### 🧭 Flujo General del Proyecto
- Scraping: Extracción total de los libros, precios, ratings y categorías.

- Almacenamiento inicial: Datos en formato JSON.

- Integración de APIs: Prueba con Open Library (fallo parcial) → Google Books (éxito).

- Poblamiento de la base de datos: Inserción de libros y autores relacionados.

- Análisis en Notebook: Consultas SQL, tiempos, y resultados visuales.