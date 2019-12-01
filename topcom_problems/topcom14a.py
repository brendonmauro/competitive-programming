def processa(pares, polinomio):
  numeros = "0123456789"
  saida = ""
  tuplas = []
  tam = len(polinomio)
  number = ""
  ignora = 0
  for i in range(tam):
    if ignora:
      ignora -= 1
      continue

    if polinomio[i] == 'x':
      base = 1
      expoente = ""
      if i > 0 and i < tam:
        if number == "+":
          base = 1
        elif number == "-":
          base = -1
        else:
          base = int(number)
        number = ""
      j =i+2
      if j > 0 and j < tam and polinomio[i+1] == '^':
        expoente += polinomio[j]
        j+=1
        while j < tam and polinomio[j] in numeros:
          expoente += polinomio[j]
          j+=1
        j-=1
        expoente = int(expoente)
      else:
        expoente = 1
        j = i
      ignora = j - i

      tuplas.append((base,expoente))
    elif polinomio[i] not in numeros and len(number):
      base = int(number)
      tuplas.append((base,0))
      number = polinomio[i]
    else:
      number += polinomio[i]

  if len(number):
    base = int(number)
    tuplas.append((base,0))
    number = ""
  #print(tuplas)
  #print(pares)
  for i in range(len(pares)):
    par = pares[i]
    cont = 0
    for tupla in tuplas:
      cont += tupla[0]*par[0]**tupla[1]

    if cont == par[1]:
      if len(saida) == 0:
        saida = str(i)
      else:
        saida += "," + str(i)

  print(saida)

def main():
  n = int(input())
  pares= []
  for i in range(n):
    entrada = input().split(' ')
    pares.append([int(entrada[0]), int(entrada[1])])
  
  m = int(input())
  polinomios = []
  for i in range(m):
    entrada = str.lower(input().replace(' ', '', 9999999))
    entrada = entrada.replace('=y','')
    polinomios.append(entrada)
    processa(pares,entrada)
  return 0

main()