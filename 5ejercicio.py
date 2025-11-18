import threading
import time

licencias = threading.Semaphore(3)

def usar_software(id_usuario):
    with licencias:
        print(f"Usuario {id_usuario} usando software")
        time.sleep(2)
        print(f"Usuario {id_usuario} terminó")

hilos = [threading.Thread(target=usar_software, args=(i,)) for i in range(15)]
for h in hilos: h.start()
for h in hilos: h.join()