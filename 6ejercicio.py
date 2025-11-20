import threading
import time

def cargar_cache():
    print("Cargando configuración en caché...")
    time.sleep(2)
    print("Caché cargada correctamente.")

def hilo_dependiente():
    print("Hilo dependiente iniciando, pero esperando la caché...")
    # Este hilo avanza solo después del join
    print("Caché lista. Continuando ejecución del hilo dependiente.")

# Crear hilos
hilo_cache = threading.Thread(target=cargar_cache)
hilo_dep = threading.Thread(target=hilo_dependiente)

hilo_cache.start()
hilo_cache.join()   # 🔥 Bloquea hasta que termine cargar_cache()

hilo_dep.start()
hilo_dep.join()
