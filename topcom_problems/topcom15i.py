n = int(input())

for i in range(n):
  ordem = int(input())
  texto = input()
  nR = int(input())
  dicR = {}
  for j in range(nR):
    regra = input().split('=')
    dicR[regra[0]] = regra[1]
  
  while ordem:
    novoTexto = ""

    for letra in texto:
      if letra in dicR:
        novoTexto += dicR[letra]
      else:
        novoTexto += letra

    texto = novoTexto 


    ordem -= 1
  print(texto)