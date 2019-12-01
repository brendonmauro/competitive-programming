import sys

def percorrer(w,h,x,y, num, mapa,tam):
  mapa[x][y] = '0'
  w = len(mapa)
  h = len(mapa[x])
  if x < 0 or x >= w or y <0 or y >= h:
    return tam
  
  if x - 1 >= 0 and mapa[x-1][y] == num:
    tam = percorrer(w,h,x-1,y,num,mapa,tam+1)
  
  if x + 1 < w and mapa[x+1][y] == num:
    tam = percorrer(w,h,x+1,y,num,mapa,tam+1)
  
  if y - 1 >= 0 and mapa[x][y-1] == num:
    tam = percorrer(w,h,x,y-1,num,mapa,tam+1)
  
  if y + 1 < len(mapa[x]) and mapa[x][y+1] == num:
    tam = percorrer(w,h,x,y+1,num,mapa,tam+1)

  return tam

def main():
  sys.setrecursionlimit(100000)
  n = int(input())
  nomes = []
  dic = {}
  for i in range(n):
    nome = input()
    nomes.append(nome)
    dic[i+1] = [nome,0,0]

  entrada = input().split(' ')
  for elem in entrada:
    if elem != '':
      linhas = int(elem)
      break
  mapa = []
  for i in range(linhas):
    entrada = input().split(' ')
    nova_ent = []
    for elem in entrada:
      if elem != '':
        nova_ent.append(elem)
    mapa.append(nova_ent)
  
  for num in range(1,n+1):
    for i in range(len(mapa)):
      for j in range(len(mapa[i])):
        if mapa[i][j] == str(num):
          dic[num][1]+=1
          tam = percorrer(len(mapa),len(mapa[i]),i,j,str(num),mapa,1)
          if tam > dic[num][2]:
            dic[num][2] = tam

  l_tups = list(dic.values())
  l_tups.sort()
  
  for elem in l_tups:
    print(elem[0],elem[1],elem[2])

main()