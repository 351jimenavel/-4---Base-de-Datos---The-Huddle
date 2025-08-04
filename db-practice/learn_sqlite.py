# 1. Import the SQLite3 module
import sqlite3      #sqlite version 3

# 2. Connect to a (new or existing) databse
conn = sqlite3.connect("mi_base_practica.db")

# 4. Create a cursor (que es un cursor?)
cur = conn.cursor()

# 5. Create a 'people' table
'''Se usa el cursor para ejecutar el SQL query
Se puede llamar al metodo Execute directamente en el objeto Connection, este obejeto crea un Cursor y lo usa para ejecutar el query, tambien retorna el cursor para acceso a datos'''
cur.execute('''CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)''')
conn.commit()   # commit this query 

# 3. ALWAYS close db objects/connection           (why?)
cur.close()
conn.close()
