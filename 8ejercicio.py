import threading
import time
import random

impresora_color = threading.Semaphore(2)

def imprimir_trabajo(id_job):
    with impresora_color:
        print(f"Trabajo {id_job} iniciando impresión a color...")
        time.sleep(random.uniform(1, 2))
        print(f"Trabajo {id_job} finalizado.")

# Simular 10 trabajos
hilos = [threading.Thread(target=imprimir_trabajo, args=(i,)) for i in range(10)]

for h in hilos: h.start()
for h in hilos: h.join()
