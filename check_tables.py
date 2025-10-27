import sqlite3

conn = sqlite3.connect('nutrition_data.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
tables = cursor.fetchall()
print('Tables:', tables)
conn.close()
