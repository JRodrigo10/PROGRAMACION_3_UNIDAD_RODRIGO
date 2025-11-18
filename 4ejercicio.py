import threading
import time

lock = threading.Lock()

def escribir_log(mensaje):
    with lock:
        with open("log.txt", "a") as f:
            f.write(mensaje + "\n")
        print(f"Escribiendo: {mensaje}")

hilos = []
for i in range(10):
    h = threading.Thread(target=escribir_log, args=(f"Mensaje del hilo {i}",))
    hilos.append(h)
    h.start()

for h in hilos:
    h.join()

print("Escritura completada. Revisar log.txt")
