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

## 🇬🇧 English

# 📚 Books To Scrape – Data Challenge  
**The Huddle – Penguin Academy**

Author: Jimena Velázquez  

---


### 🧠 Project Overview  
This challenge consisted of **extracting, structuring, and analyzing book data** from the website [Books to Scrape](https://books.toscrape.com/), with the goal of building a **complete relational database**, performing **advanced SQL queries**, and exploring the **impact of indexing on performance**.

The project combined **legal web scraping**, **API consumption**, **data cleaning**, and **relational modeling**, allowing integration of information obtained from the site and external APIs such as *Open Library* and *Google Books*.

---

### 🧩 Technologies & Tools
- **Python** → Data extraction and manipulation  
- **BeautifulSoup + Requests** → Web scraping  
- **SQLite3** → Relational database  
- **SQLAlchemy** → ORM for structured manipulation  
- **External APIs** → Open Library (test) and Google Books (final implementation)  
- **JSON** → Intermediate data storage  
- **Jupyter Notebook** → Analysis, visualization, and documentation  

---

### ⚙️ Project Structure
| File / Folder | Description |
|----------------|-------------|
| `1-scraping-bookstoscrape.ipynb` | Extracts all books and categories from the website. |
| `2-apigooglebooks.py` | Integrates the data with the Google Books API. |
| `3-books-database.ipynb` | Creates and populates the database. |
| `4-queries.ipynb` | Contains SQL queries, performance comparisons (with/without indexes), and conclusions. |
| `libros_scrapeados.json` | Raw scraped data. |
| `autores_extraidos_openlibrary.json` | Results from testing the Open Library API (many unknown authors). |
| `autores_googlebooks.json` | Final author data successfully extracted via Google Books API. |
| `diagram_uml.png` | UML diagram of the relational model. |

---

### 🧠 How to Run the Project

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/usuario/-4---Base-de-Datos---The-Huddle.git
cd -4---Base-de-Datos---The-Huddle/entrega
```

#### 2️⃣ Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate        # On Windows
pip install -r requirements.txt
```

#### 3️⃣ Scraping
Open and run the notebook `1-scraping-bookstoscrape.ipynb`
Expected output: `libros_scrapeados.json`

#### 4️⃣ Enrich data with external APIs
- Option A: Run the version using Open Library inside (oplib.py)

Expected output: `autores_extraidos_openlibrary.json`

- Option B: Run the final version using Google Books (2-apigooglebooks.py)
```bash
python 2-apigooglebooks.py
```
Results will be saved as separate JSON files to maintain independence between data sources.

Expected output: `autores_googlebooks.json`

#### 5️⃣ Database — open the notebook `3-books-database.ipynb`
Creates and populates `books_data.db` (many-to-many relationships).

#### 6️⃣ Queries / Analysis — run `4-queries.ipynb`
Includes queries, comparisons with/without indexes, and final conclusions.

---
### 🧬 Relational Model

The data model implements many-to-many relationships between books and authors, as well as foreign keys linking categories and ratings.

The UML diagram represents the entities as follows:
```lua
Author  ---< BookAuthor >---  Book  ---< Category
```

---
### 🧭 General Project Workflow
- Scraping: Extraction of all books, prices, ratings, and categories.

- Initial storage: Data saved in JSON format.

- API integration: Tested Open Library (partial failure) → switched to Google Books (successful).

- Database population: Insertion of books and related authors.

- Analysis in Notebook: SQL queries, timing tests, and visual results.