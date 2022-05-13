#importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer

#fibonacci de manera iterativa
def iterativo(n):
  #dos primeros numeros de fibonacci

  terminos = [0,1]
  
  i = 2
  while i<= n:
    terminos.append(terminos[i-1]+terminos[i-2])
    i = i+1
  return terminos[n]

#calculando el tiempo de ejecuccion del fibo de manera iterativa
inicio = default_timer()
iterativo(34)
fin = default_timer()

#imprimir el tiempo
print(fin - inicio)
#imprimir el resultado del fibonacci
print(iterativo(34))