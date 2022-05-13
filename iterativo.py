def iterativo(n):
  terminos = [0,1]
  i = 2
  while i<= n:
    terminos.append(terminos[i-1]+terminos[i-2])
    i = i+1
  return terminos[n]