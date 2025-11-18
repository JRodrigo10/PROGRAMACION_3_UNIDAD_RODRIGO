import threading
import time
import random

semaforo = threading.Semaphore(8)

def conexion_bd(id_hilo):
    with semaforo:
        print(f"Hilo {id_hilo} conectado a la BD")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Hilo {id_hilo} liberó la conexión")

# Crear 20 solicitudes simuladas
hilos = [threading.Thread(target=conexion_bd, args=(i,)) for i in range(20)]

for h in hilos: h.start()
for h in hilos: h.join()

print("Procesamiento finalizado")
