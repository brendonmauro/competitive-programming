#include <stdio.h>
#include <stdlib.h>

int main()
{
  char dic[12][5] = {"si","do", "do#", "re", "re#", "mi", "fa", "fa#", "sol",
    "sol#", "la", "la#"};
  
  int n,*notas, escalas[12][7], escalaMaior[6] = {2,2,1,2,2,2,1};
  register int i,j,k, aux;
  
  register int flag, flag2, desafinado = 1;
  
  for (i = 0; i < 12 ; i++)
  {
    aux = i;
    for(j = 0; j < 7; j++)
    {
      escalas[i][j] = aux;
      aux =(aux + escalaMaior[j]) % 12;
    }
  }
  
  scanf("%d", &n);
  notas = (int*) malloc(sizeof(int)* n);

  for (i = 0; i < n; i++)
    scanf("%d", &notas[i]);

  for (i = 0; i < 12; i++)
  {
    flag = 1;
    for(j = 0; j < n; j++)
    {
      flag2 = 0;
      for (k = 0; k < 7; k++)
      {
        if ((notas[j] % 12) == escalas[i][k])
        {
          flag2 = 1;
          break;
        }
      }
      
      if (!flag2)
      {
        flag = 0;
        break;
      }
    }
    
    if (flag)
    {
      printf("%s\n", dic[i]);
      desafinado = 0;
      break;
    }
  }
  
  if (desafinado)
    printf("desafinado\n");
  
  free(notas);
  return 0;
  
}