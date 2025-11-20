import threading

contador = 0
lock = threading.Lock()

def registrar_descarga():
    global contador
    with lock:
        contador += 1
        print(f"Descargas totales: {contador}")

hilos = [threading.Thread(target=registrar_descarga) for _ in range(100)]

for h in hilos: h.start()
for h in hilos: h.join()

print(f"Total final de descargas: {contador}")
