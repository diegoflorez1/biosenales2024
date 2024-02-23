#PRACTICA 1 - LABORATORIO DE BIOSEÑALES Y SISTEMAS
#NOMBRE: DIEGO ANDRÉS FLÓREZ RUANO
#--------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("INTRODUCCION AL USO DE PYTHON Y NUMPY\nPROCEDIMIENTO:")
#A)
print("\nA) Par de vectores a y b")
a = [67.1, 1, -0.3, 5.2, -6]
b = [1, 3, 2.2, 5.1, 1]
print("a = ", a)
print("b = ", b)

#B)
resultado = np.dot(a, b)
print("\nB) El resultado de la multiplicación escalar de a.b es:", resultado)

#C)
producto_punto= np.multiply(a, b)
print("\nC) La multiplicación punto a punto de a.b es:", producto_punto)

#D)
matrizA= np.array([(2,-1,-3), (4,-1.5,-2.5), (7.3,-0.9,-0.2)])
print("\nD) Matriz A\nA = ")
print(matrizA)

#E)
traspuesta = np.transpose(matrizA)
print("\nE) Traspuesta AT:\nAT = ")
print(traspuesta)

#F)
#np.ones(): 
print("\nF) Función  de  los comandos ones,  round,  ceil y floor,de  la  librería  numpy: ")
print("\n - Comando ones: Esta función se utiliza para crear un array de cierta forma y tipo, lleno de unos.")
array_ones = np.ones((4, 4))
print("\nArray de unos:")
print(array_ones)

#np.round(): 
print("\n - Comando round: Esta función redondea los elementos de un array al número entero más cercano")
array_decimal = np.array([1.5, 2.8, 3.6, 4.5])
print("\nArray decimal:")
print(array_decimal)


# Redondear los valores del array
array_redondeado = np.round(array_decimal)
print("\nArray redondeado:")
print(array_redondeado)

#np.floor():
print("\n - Comando floor: Esta función redondea hacia abajo los elementos de un array",
      "es decir, hacia el entero más cercano que sea menor o igual al valor original.")

# Ejemplo:
print("\nArray decimal:")
print(array_decimal)
array_floor = np.floor(array_decimal)
print("\nArray redondeado hacia abajo:")
print(array_floor)

#G)

valor = matrizA[0, 2]
print("\nG) El valor de la primera fila y la tercera columna de la matriz A es: ")
print(valor)

#H)
fila2 = matrizA[1, :]
print("\nH) El valor de la segunda fila es: ")
print(fila2)

#I)
dimensiones = matrizA.shape
print("\nI) Las dimensiones de la matriz A son:", dimensiones)

#J)
def y1(n):
    return np.sin(np.pi * 0.18 * n)

# Crear un array de valores de n en el intervalo 0 <= n <= 80
valores_n = np.arange(81)

# Calcular y[n] para cada valor de n
señal_y1= y1(valores_n)

#K)
def y2(n):
    return np.cos(2 * np.pi * 0.03 * n)

# Calcular y2[n] para cada valor de n
señal_y2 = y2(valores_n)

#L)
# Calcular la tercera señal s[n] (suma de y[n] y y2[n])
señal_s = señal_y1 + señal_y2

# Calcular la cuarta señal t[n] (producto de y[n] y y2[n])
señal_t = señal_y1 * señal_y2

#M)
# Graficar las señales y[n] y y2[n]
plt.plot(valores_n, señal_y1, label='y[n]', color='blue')
plt.plot(valores_n, señal_y2, label='y2[n]', color='red')

# Asignar títulos a los ejes y a la figura
plt.title('Gráfica de las señales y[n] y y2[n]')
plt.xlabel('n')
plt.ylabel('Amplitud')

# Agregar leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()

#N)
# Graficar las señales s[n] y t[n]
plt.plot(valores_n, señal_s, label='s[n]', color='green')
plt.plot(valores_n, señal_t, label='t[n]', color='orange')

# Asignar títulos a los ejes y a la figura
plt.title('Gráfica de las señales s[n] y t[n]')
plt.xlabel('n')
plt.ylabel('Amplitud')

# Agregar leyenda
plt.legend()

# Mostrar la gráfica con cuadrícula
plt.grid(True)
plt.show()

#¡RETO!
print("\n¡RETO!")
def notas_curso(notas_estudiantes):
    # Convertir el diccionario de notas a una serie
    notas_serie = pd.Series(notas_estudiantes)
    
    # Calcular la nota mínima, máxima y media
    nota_minima = notas_serie.min()
    nota_maxima = notas_serie.max()
    nota_media = notas_serie.mean()
    
    # Calcular la desviación típica
    desviacion_tipica = notas_serie.std()
    
    # Crear una serie con las estadísticas
    estadisticas = pd.Series({
        'Nota mínima': nota_minima,
        'Nota máxima': nota_maxima,
        'Nota media': nota_media,
        'Desviación típica': desviacion_tipica})
    return estadisticas

# Ejemplo de notas de los alumnos
notas_estudiantes = {'Juan': 7, 'María': 8, 'Pedro': 6, 'Ana': 9, 'Luis': 5}

# Obtener las estadísticas de las notas
resultado = notas_curso(notas_estudiantes)

# Imprimir las estadísticas
print("\nEstadísticas de las notas de los alumnos:\n")
print(resultado)
