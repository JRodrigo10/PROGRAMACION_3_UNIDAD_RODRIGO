import threading

stock = 50
lock = threading.Lock()

def disminuir_stock(cantidad):
    global stock
    with lock:  # sección crítica protegida
        valor_lectura = stock
        valor_lectura -= cantidad
        stock = valor_lectura
        print(f"Stock actualizado: {stock}")

# Crear dos hilos que modifican al mismo tiempo
hilo1 = threading.Thread(target=disminuir_stock, args=(1,))
hilo2 = threading.Thread(target=disminuir_stock, args=(1,))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Stock final correcto: {stock}")
