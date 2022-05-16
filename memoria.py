#librerias para la graficadora
import numpy as np
import matplotlib.pyplot as plt
# importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer

# rango global para el uso de memoria
dp = [-1 for i in range(5000)]


# fibonacci usando memoria
def memoria(n):
    if (n <= 1):
        return n;

    # uso de la funcion global
    global dp;

    # dos primeros fibonacci
    first = 0;
    second = 0;

    if (dp[n - 1] != -1):
        first = dp[n - 1];
    else:
        first = memoria(n - 1);
    if (dp[n - 2] != -1):
        second = dp[n - 2];
    else:
        second = memoria(n - 2);
    dp[n] = first + second;

    # Uso de memorizacion
    return dp[n];


def nums(x):
    lista=[]
    for i in range(x):
        # calculando el tiempo de ejecuccion del fibo memoria
        inicio = default_timer()
        memoria(i)
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
