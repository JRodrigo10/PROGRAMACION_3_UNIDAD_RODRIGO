import threading
import time
import random

buffer = []
condicion = threading.Condition()

def receptor():
    global buffer
    while True:
        time.sleep(random.uniform(0.5, 1.5))
        paquete = random.randint(100, 999)

        with condicion:
            buffer.append(paquete)
            print(f"Receptor: paquete recibido {paquete}")
            condicion.notify()  # avisar al procesador

def procesador():
    global buffer
    while True:
        with condicion:
            while not buffer:
                condicion.wait()  # esperar sin gastar CPU

            paquete = buffer.pop(0)
            print(f"Procesador: procesando paquete {paquete}")

        time.sleep(1)

h1 = threading.Thread(target=receptor, daemon=True)
h2 = threading.Thread(target=procesador, daemon=True)

h1.start()
h2.start()

time.sleep(10)  # correr 10 segundos para la demo
print("Fin de la simulación")
