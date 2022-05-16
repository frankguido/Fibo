#librerias para la graficadora
import numpy as np
import matplotlib.pyplot as plt
# importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer


# fibonacci de manera iterativa
def iterativo(n):
    # dos primeros numeros de fibonacci

    terminos = [0, 1]

    i = 2

    while i <= n:
        terminos.append(terminos[i - 1] + terminos[i - 2])
        i = i + 1
    return terminos[n]


def nums(x):
    lista=[]
    for i in range(x):
        # calculando el tiempo de ejecuccion del fibo
        inicio = default_timer()
        iterativo(i)
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

