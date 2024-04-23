import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import os

# Obtener la ruta al directorio actual donde se encuentra el código para guardar despues en esta misma ruta la imagen y el txt
current_directory = os.path.dirname(os.path.abspath(__file__))

arduino = serial.Serial('COM9', 9600, timeout=0.01)  # Especifica el puerto serial y la velocidad de transmisión 
time.sleep(2)

numero_datos = 2000  # Número de datos a adquirir #Usamos 200 para el ECG y 3000 para EMG
EMG = np.ndarray((0), dtype=int)  # Aquí se almacenará la señal

# Mientras el arreglo no tenga los datos que requiero, los solicito
while EMG.shape[0] < numero_datos: 
    datos = arduino.readlines(arduino.inWaiting())
    datos_por_leer = len(datos)
  
    if len(datos) > numero_datos:
        datos = datos[0:numero_datos]
        valores_leidos = np.zeros(numero_datos, dtype=int)
    else:
        valores_leidos = np.zeros(datos_por_leer, dtype=int)
    
    posicion = 0
    # Se convierten los datos a valores numéricos de voltaje
    for dato in datos:
        try:
            # Elimino los saltos de línea y el caracter de retorno y convierto a entero
            valores_leidos[posicion] = int(dato.decode().strip())
        except:
            # Si no puedo convertir, completo la muestra con el anterior
            valores_leidos[posicion] = valores_leidos[posicion-1]
        posicion += 1
    # Agrego los datos leídos al arreglo
    EMG = np.append(EMG, valores_leidos)
    # Introduzco un delay para que se llene de nuevo el buffer
    time.sleep(2)

# Como la última lectura puede tener más datos de los que necesito, descarto las muestras restantes
EMG = EMG[:numero_datos]

# Graficar la señal
plt.plot(EMG)

# Guardar la señal como un archivo de texto
file_path_txt = os.path.join(current_directory, 'señal_captada.txt')
np.savetxt(file_path_txt, EMG)

# Guardar la señal como un archivo de imagen JPG
file_path_jpg = os.path.join(current_directory, 'señal_captada.jpg')
plt.savefig(file_path_jpg)

# Mostrar la gráfica
plt.show()

# Cerrar puerto serial, siempre debe cerrarse
arduino.close()
