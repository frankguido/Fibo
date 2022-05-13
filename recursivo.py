from timeit import default_timer
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)



inicio = default_timer()
fib(22)
fin = default_timer()
print(fin - inicio)

print (fib(22))