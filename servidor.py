import socket
import sqlite3
from datetime import datetime

#direccion local,puerto y Base Datos

HOST = "127.0.0.1"     # Dirección local (localhost)
PORT = 5000            # Puerto que va a usar el servidor
DB_PATH = "mensajes.db"  # Archivo de la base de datos

#Base de datos
def init_db():
    """Crea la base de datos y la tabla si no existen."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio TEXT NOT NULL,
            ip_cliente TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()

def save_message(contenido: str, ip_cliente: str) -> str:
    """Guarda un mensaje y devuelve la fecha/hora usada."""
    ts = datetime.now().isoformat(timespec="seconds")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
        (contenido, ts, ip_cliente),
    )
    conn.commit()
    conn.close()
    return ts

#Servidor Principal

def run_server():
    # inicia la base de datos
    init_db()

    # Crear el socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((HOST, PORT))
        srv.listen()
        print(f"[SERVIDOR] Escuchando en {HOST}:{PORT}...")

        while True:
            conn, addr = srv.accept()  # Espera conexión de un cliente
            with conn:
                print(f"[SERVIDOR] Cliente conectado: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break  # Si el cliente se desconectó
                    mensaje = data.decode("utf-8").strip()
                    print(f"[SERVIDOR] Recibido de {addr}: {mensaje}")

                    # Guardar en la base de datos
                    ts = save_message(mensaje, addr[0])

                    # Responder al cliente
                    respuesta = f"Mensaje recibido: {ts}"
                    conn.sendall(respuesta.encode("utf-8"))

if __name__ == "__main__":
    run_server()