n = int(input())
simbolos = '+-/*'
for i in range(n):
  entrada = input().split(" ")
  pilha = []
  divZero = False
  for elem in entrada:
    if elem == "":
      continue
    if elem not in simbolos:
      pilha.append(int(elem))
    else:
      sec = pilha.pop()
      pri = pilha.pop()
      if (elem == '+'):
        pilha.append(pri+sec)
      elif(elem == '-'):
        pilha.append(pri-sec)
      elif(elem == '*'):
        pilha.append(pri*sec)
      else:
        if sec == 0:
          divZero = True
          break
        pilha.append(int(pri/sec))
  
  if divZero:
    print('DIV0')
  else:
    print(pilha.pop())