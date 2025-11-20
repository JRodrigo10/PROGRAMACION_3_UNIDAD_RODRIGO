import threading
import time

usuario = {
    "email": "user@example.com",
    "telefono": "999999999"
}

lock = threading.Lock()

def actualizar_email():
    with lock:
        print("Hilo A leyendo usuario...")
        time.sleep(1)
        usuario["email"] = "jerssonrodrigoe7@gmail.com"
        print("Hilo A actualizó email.")

def actualizar_telefono():
    with lock:
        print("Hilo B leyendo usuario...")
        time.sleep(1)
        usuario["telefono"] = "988859873"
        print("Hilo B actualizó teléfono.")

h1 = threading.Thread(target=actualizar_email)
h2 = threading.Thread(target=actualizar_telefono)

h1.start()
h2.start()

h1.join()
h2.join()

print(f"Usuario final: {usuario}")
