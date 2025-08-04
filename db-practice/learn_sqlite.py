# 1. Import the SQLite3 module
import sqlite3      #sqlite version 3

# 2. Connect to a (new or existing) databse
conn = sqlite3.connect("mi_base_practica.db")

# 4. Create a cursor (que es un cursor?)
cur = conn.cursor()

# 6. Test Data
names_list = [
    ("Roderick", "Watson"),
    ("Roger", "Hom"),
    ("Petri","Halonen"),
    ("Jussi",""),
    ("James","McCann")
]

# 5. Create a 'people' table
'''Se usa el cursor para ejecutar el SQL query
Se puede llamar al metodo Execute directamente en el objeto Connection, este obejeto crea un Cursor y lo usa para ejecutar el query, tambien retorna el cursor para acceso a datos'''
cur.execute('''CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)''')
conn.commit()   # commit this query 

# 7. Insert data into database
#### que hace el (?,?) ??
#### para el metodo 'executemany' el segundo argumento debe ser un objeto iterable
cur.executemany('''
        INSERT INTO people (first_name, last_name) VALUES (?,?)
''', names_list)
conn.commit()

# 3. ALWAYS close db objects/connection           (why?)
cur.close()
conn.close()
