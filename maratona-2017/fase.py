n = int(input())
m = int(input())
vet = []
for i in range(n):
  vet.append(int(input()))

vet.sort()
vet.reverse()
cont = m

  
for i in range(m,n):
  if vet[i] == vet[i-1]:
    cont+= 1
  else:
    break
  
print (cont)