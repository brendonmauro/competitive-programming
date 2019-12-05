def imprimir_mat(mat):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      print(mat[i][j], end=' ')
    print()
def main():
  entrada = input().split(' ')
  l = int(entrada[0])
  c = int(entrada[1])
  mat = []
  d = []
  for i in range(l):
    mat.append(input().split())
    d.append(int(mat[i].pop()))
  
  b = []
  entrada = input().split(' ')
  for i in range(c):
    b.append(int(entrada[i]))
  
  variaveis = []
  dic_var = {}
  tem_var = 1
  cont = 0
  contA = 5
  while tem_var and cont < contA :
    tem_var = 0
    #analisa linha
    for i in range(l):
      aux_var = {}
      num = 0
      for j in range(c):
        if mat[i][j].replace('-','').isnumeric():
          num += int(mat[i][j])
        else:
          if mat[i][j] not in aux_var:
            aux_var[mat[i][j]] = 1
          else:
            aux_var[mat[i][j]] += 1
      
      if len(aux_var.keys()) == 1:
        variavel = list(aux_var.keys())[0]
        qtd = aux_var[variavel]
        valor = int((d[i] - num)/qtd)
        if variavel not in dic_var:
          variaveis.append([variavel,valor])
          dic_var[variavel] = valor
        for j in range(c):
          if not mat[i][j].replace('-','').isnumeric():
            mat[i][j] = str(valor)
      
      if len(aux_var.keys()) > 1:
        tem_var = 1
    #print("analisou linha", mat)
    #analisa coluna
    for j in range(c):
      aux_var = {}
      num = 0
      for i in range(l):
        if mat[i][j].replace('-','').isnumeric():
          num += int(mat[i][j])
        else:
          if mat[i][j] not in aux_var:
            aux_var[mat[i][j]] = 1
          else:
            aux_var[mat[i][j]] += 1
      
      if len(aux_var.keys()) == 1:
        variavel = list(aux_var.keys())[0]
        qtd = aux_var[variavel]
        valor = int((b[j] - num)/qtd)
        if variavel not in dic_var:
          variaveis.append([variavel,valor])
          dic_var[variavel] = valor
        for i in range(l):
          if not mat[i][j].replace('-','').isnumeric():
            mat[i][j] = str(valor)
      
      if len(aux_var.keys()) > 1:
        tem_var = 1
    
    #substitui toda a mat
    for i in range(l):
      for j in range(c):
        if mat[i][j] in dic_var:
          mat[i][j] = str(dic_var[mat[i][j]])

    #print("analisou coluna", mat)
    #cont+=1

  variaveis.sort()
  for a,b in variaveis:
    print(a,b)
  #print(dic_var)
  #imprimir_mat(mat)
  return 0

main()