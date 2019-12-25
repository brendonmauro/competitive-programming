def mdc(a, b):
  if (b == 0):
   return a
  else:
    return mdc(b, a % b)

def mmc(num1,num2):
  return (num1*num2)/mdc(num1,num2)

def mmcl(lista):

  mmc_res = lista[0]
  for i in range(1,len(lista)):
    mmc_res = mmc(mmc_res, lista[i])

  return mmc_res

def main():
  entrada = input().split(' ')
  n = int(entrada[0])
  l = int(entrada[1])

  cs = input().split(' ')
  for i in range(n):
    cs[i] = int(cs[i])

  mmc_coringa = mmcl(list(cs))
  mmc_max = l - l % mmc_coringa
  multiplo = mmc_max /mmc_coringa

  #print(mmc_coringa)
  #print(mmc_max)
  #print(multiplo)
  #print()

  if not multiplo:
    print (1)
    return
  num = multiplo
  novo_cs = list(cs)
  novo_cs.append(num)

  while(mmcl(list(novo_cs)) != mmc_max and num < mmc_max + 1):
    num+= multiplo
    novo_cs[len(novo_cs) -1] = num

  
  print(int(num))
  return 0

main()