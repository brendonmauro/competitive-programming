#include <stdio.h>
#include <stdlib.h>

long int max(long int a,long int b){
  if (a > b)
    return a;
  return b;
}


long int processa(int ini,int fim, long int* lst, int pontua, long int** dic){
  if (ini == fim){
    if (pontua){
      
      return (long int) lst[ini];
    }else 
      return (long int)0;
  }else{
    if (dic[ini+1][fim] == -1){
      dic[ini+1][fim] = processa(ini+1, fim, lst,  !pontua, dic);
    }
    if (dic[ini][fim-1] == -1){
      dic[ini][fim-1] = processa(ini, fim-1, lst, !pontua, dic);
    }
    if (pontua){
      
      if ((long int) (dic[ini+1][fim] + lst[ini]) > (long int) (dic[ini][fim-1] + lst[fim]))
        dic[ini][fim] = (long int) (dic[ini+1][fim] + lst[ini]);
      else
        dic[ini][fim] = (long int) (dic[ini][fim-1] + lst[fim]);
    }else {

      dic[ini][fim] = (long int) max(dic[ini+1][fim], dic[ini][fim-1]);
    }
  }
  return dic[ini][fim];
}

int main(void) {
  int n, i,j;
  long int *lst, **dic, aux;
  scanf("%d", &n);
  while(n)
  {
    lst = (long int*) malloc(n*sizeof(long int));
    dic = (long int**) malloc(n*sizeof(long int*));
    for (i = 0; i < n; i++)
    {
      dic[i] = (long int*) malloc(n*sizeof(long int));
      for (j = 0; j < n; j++)
        dic[i][j] = (long int) -1;
    }
    for (i = 0; i < n; i++)
    {
      scanf("%ld", &aux);
      lst[i] = aux;
    }

    
    

    printf("%ld\n", processa(0,n-1,lst,1,dic));
    free(dic);
    free(lst);
    scanf("%d", &n);
  }
  return 0;
}