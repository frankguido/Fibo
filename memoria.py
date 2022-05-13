#importa la libreria para poder calcular el tiempo de ejecucion
from timeit import default_timer

#rango global para el uso de memoria 
dp = [-1 for i in range(5000)]

#fibonacci usando memoria
def fib(n):
    if (n <= 1):
        return n;
      
    #uso de la funcion global
    global dp;
  
    #dos primeros fibonacci
    first = 0;
    second = 0;
 
    if (dp[n - 1] != -1):
        first = dp[n - 1];
    else:
        first = fib(n - 1);
    if (dp[n - 2] != -1):
        second = dp[n - 2];
    else:
        second = fib(n - 2);
    dp[n] = first + second;
 
    # Uso de memorizacion
    return dp[n] ;
 
#tiempo de ejecucion y resultado de fibonacci
if __name__ == '__main__':
    n = 33;
    inicio = default_timer()
    fib(33)
    fin = default_timer()
    print(fin - inicio)
    print(fib(33))

