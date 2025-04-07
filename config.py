import sqlite3

conn = sqlite3.connect('ubicaciones.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ubicaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                latitud TEXT,
                longitud TEXT,
                hora TEXT)''')
conn.commit()
conn.close()