dic = {}
m = 0
n = 0


def percorrer(no, minutos):
  global dic
  cont = 0
  a = minutos - 1 if no - m > minutos - 1  else  no - m
  b = minutos - 1 if n - no > minutos - 1 else n - no
  #print("a => %d, b => %d" % (a,b))
  if b < a:
    a = b

  if (a,minutos) in dic:
    return dic[(a,minutos)]
  elif minutos == 1:
    return 1
  else:
    if no - 1 > m - 1:
      cont += percorrer(no-1, minutos-1)
    if no + 1 < n + 1:
      cont += percorrer(no+1, minutos-1) 

  dic[(a,minutos)] = cont
  #print("no => %d, m = > %d, cont => %d" % (no,minutos,cont))
  return cont

def main():
  global dic,m,n
  cont = 0
  entrada = input().split(' ')
  t = int(entrada[0])
  m = int(entrada[1])
  n = int(entrada[2])
  
  if t < n - m:
    valor = t
  else:
    valor = n - m
  
  for i in range(m,m+valor):
    percorrer(i,t)
  
  for i in range(m, n + 1):
    a = t - 1  if i - m > t - 1 else i - m
    b = t - 1  if n - i > t -1 else n - i

    if b < a:
      a = b
    cont += dic[(a,t)]
  print(cont % 1000000007)
  return 0

main()