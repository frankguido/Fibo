#librerias para la graficadora
import numpy as np
import matplotlib.pyplot as plt
# importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer


# fibonacci de manera recursiva
def recursivo(n):
    if n == 0:
        return 0

    # recursividad
    if n == 1:
        return 1
    return recursivo(n - 1) + recursivo(n - 2)


def nums(x):
    lista=[]
    for i in range(x):
        # calculando el tiempo de ejecuccion del fibo memoria
        inicio = default_timer()
        recursivo(i)
        fin = default_timer()

        # guardando los tiempos en un array
        lista.append(fin-inicio)
    print(lista)
        # imprimir el resultado del fibonacci

#imprimir los primeros tiempos de n fibonacci
print(nums(32))
'''
#graficadora
x = np.array(range(40)) * 1

y = np.zeros(lista)

# controlar tamaño
plt.ion()
plt.plot(x, y)
'''