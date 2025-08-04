import sqlite3

# Connect to create SQLite database
conn = sqlite3.connect('members.db')

# Create a cursor
cur = conn.cursor()

# Load SQL script from file
with open("C:/Users/Jimena/Downloads/test.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Execute the script
cur.executescript(sql_script)
## no hace falta el commit ya que el script lo tiene

# Close db objects
cur.close()
conn.close()

