
def contar(universidade, x, y, h, v):
  iniX = x - v
  if iniX < 0:
    iniX = 0
  fimX = x + v
  if fimX > len(universidade) - 1:
    fimX = len(universidade) - 1

  iniY = y - h
  if iniY < 0:
    iniY = 0
  fimY = y + h
  if fimY > len(universidade[0]) - 1:
    fimY = len(universidade[0]) - 1

  contZumbi = 0
  contHuman = 0
  for i in range(iniX, fimX + 1):
    for j in range(iniY, fimY + 1):
      if universidade[i][j] == '1':
        contZumbi += 1
      elif universidade[i][j] == '2':
        contHuman += 1
  
  return (contZumbi, contHuman)
  
def main():
  u = int(input())
  for i in range(u):
    entrada = input().split(' ')
    h = int(entrada[0])
    v = int(entrada[1])
    entrada = input().split(' ')
    m = int(entrada[0])
    n = int(entrada[1])
    universidade = []
    for j in range(n):
      universidade.append(input())
    
    maior = (0,0)
    pos = (0,0)
    for k in range(n):
      for l in range(m):
        cont =contar(universidade,k,l,h,v)
        if cont[0] > maior[0]:
          maior = cont
          pos= (k,l)
        elif cont[0] == maior[0] and cont[1] < maior[1]:
          maior = cont
          pos= (k,l)

    print ("X:%d Y:%d" % (pos[1], pos[0]))

main()