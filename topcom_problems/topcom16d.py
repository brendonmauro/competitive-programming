n = int(input())

for i in range(n):
  entrada = input()
  pesos = [10,9,8,7,6,5,4,3,2]
  i = 0
  j = 0
  for letra in entrada:
    if letra == '.':
      continue
    elif letra == '-':
      break
    j += int(letra) * pesos[i]
    i+= 1
  #print(j)
  j %= 11
  if j < 2:
    j = 0
  else:
    j = 11 - j
  
  pesos = [11,10,9,8,7,6,5,4,3]
  i = 0
  k = 0

  for letra in entrada:
    if letra == '.':
      continue
    elif letra == '-':
      break
    k += int(letra) * pesos[i]
    i+= 1
  k += j * 2

  #print(k)
  k %= 11
  if k < 2:
    k = 0
  else:
    k = 11 - k
  #print(j,k,int(entrada[12]), int(entrada[13]))
  if j == int(entrada[12]) and k == int(entrada[13]):
    print ('CPF verificado!')
  else:
    print ('CPF incorreto!')  