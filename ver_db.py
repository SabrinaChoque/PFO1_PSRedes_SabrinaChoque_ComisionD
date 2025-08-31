import sqlite3

conn = sqlite3.connect("mensajes.db")
cur = conn.cursor()

print("Mensajes guardados en la base de datos:\n")
for fila in cur.execute("SELECT id, contenido, fecha_envio, ip_cliente FROM mensajes ORDER BY id"):
    print(fila)

conn.close()
