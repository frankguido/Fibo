from timeit import default_timer

def iterativo(n):
  terminos = [0,1]
  i = 2
  while i<= n:
    terminos.append(terminos[i-1]+terminos[i-2])
    i = i+1
  return terminos[n]


inicio = default_timer()
iterativo(34)
fin = default_timer()
print(fin - inicio)

print(iterativo(34))