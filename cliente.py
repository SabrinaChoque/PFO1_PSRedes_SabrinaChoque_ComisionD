import socket

HOST = "127.0.0.1"
PORT = 5000

def normalizar_fin(s: str)-> bool:
    """Devuelve true si finaliza el usuario."""
    s= s.strip().lower()
    return s in ("éxito", "exito") # aceptamos con y sin tilde

def main():
    # Crear socket TCP/IP
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado a {HOST}:{PORT}")
    except ConnectionRefusedError:
        print("[CLIENTE] No pude conectar. ¿Arrancaste el servidor primero?")
        return

    with sock:
        while True:
            texto = input("Escribí un mensaje (o 'éxito' para salir): ").strip()
            if normalizar_fin(texto):
                print("[CLIENTE] Cerrando conexión...")
                break
            if not texto:
                continue  # ignorar vacío

            # Enviar mensaje al servidor
            sock.sendall(texto.encode("utf-8"))

            # Recibir respuesta
            data = sock.recv(1024)
            if not data:
                print("[CLIENTE] Servidor cerró la conexión.")
                break
            print(data.decode("utf-8"))

if __name__ == "__main__":
    main()