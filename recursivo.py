#importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer

#fibonacci de manera recursiva
def fib(n):
  
    if n == 0:
        return 0
      
    #recursividad
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


#Ejecucion del tiempo de fibonacci de manera recursiva
inicio = default_timer()
fib(22)
fin = default_timer()
print(fin - inicio)
#resultado de fibonnaci de n
print (fib(22))