import threading
import time

condicion = threading.Condition()
pdf_listo = False

def fabrica():
    global pdf_listo
    time.sleep(2)
    with condicion:
        print("Fábrica: PDF terminado.")
        pdf_listo = True
        condicion.notify()  # avisar al inspector

def inspector():
    with condicion:
        print("Inspector: esperando el PDF...")
        condicion.wait()  # bloqueo hasta recibir señal
        print("Inspector: PDF recibido, iniciando inspección.")

h1 = threading.Thread(target=fabrica)
h2 = threading.Thread(target=inspector)

h2.start()
h1.start()

h1.join()
h2.join()
