# cronometro.py
import time
import threading

# Función para mostrar el cronómetro en tiempo real
def mostrar_cronometro(start_time, fin_ejecucion):
    while not fin_ejecucion[0]:  # Usamos una lista para poder modificarla dentro del hilo
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)  # Calcula los minutos
        seconds = int(elapsed_time % 60)    # Calcula los segundos
        print(f"\rTiempo transcurrido: {minutes} minutos y {seconds} segundos", end="")
        time.sleep(1)  # Actualiza cada 1 segundo

def iniciar_cronometro():
    start_time = time.time()
    fin_ejecucion = [False]  # Usamos una lista para que el valor pueda cambiar dentro del hilo
    hilo_cronometro = threading.Thread(target=mostrar_cronometro, args=(start_time, fin_ejecucion))
    hilo_cronometro.start()
    
    return start_time, fin_ejecucion, hilo_cronometro

def detener_cronometro(start_time, fin_ejecucion, hilo_cronometro):
    # Detener el cronómetro
    fin_ejecucion[0] = True
    hilo_cronometro.join()  # Esperar a que el hilo termine

    # Calcular y mostrar el tiempo total de ejecución
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)  # Calcula los minutos
    seconds = int(elapsed_time % 60)    # Calcula los segundos
    print(f"\nTiempo total de ejecución: {minutes} minutos y {seconds} segundos")
