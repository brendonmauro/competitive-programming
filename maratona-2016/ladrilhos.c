#include <stdio.h>
#include <stdlib.h>

int menor, h, l;
int ** matriz;

void busca(int i, int j,int * cont)
{
	int valor;
	*cont +=1;
	if (matriz[i][j] == -1) return;
	valor = matriz[i][j];
	matriz[i][j] = -1;
	if(i+1 < h ){
		if(matriz[i+1][j] == valor)
			busca(i+1,j, cont);
	}
	if (j + 1 < l)
	{
		if(matriz[i][j+1] == valor)
			busca(i,j+1,cont);
	}
	if(i-1 >= 0)
	{
		if(matriz[i-1][j] == valor)
			busca(i-1,j,cont);
	}	
	if(j-1 >= 0)
	{
		if(matriz[i][j-1] == valor)
			busca(i,j-1, cont);
	}
}

int main(int argc, char **argv)
{
	int *cont, x, i, j;
	cont = &x;
	
	scanf("%d %d", &h, &l);
	
	menor = h*l;
	x = menor;
	matriz = (int**) malloc(sizeof(int*)*h);
	
	for(i = 0; i < h; i++)
		matriz[i] = (int*) malloc(sizeof(int)*l);
	
	for(i = 0; i < h; i++)
	{
		for (j = 0; j < l; j++)
			scanf("%d",&matriz[i][j]);
	}
	for(i = 0; i < h; i++)
	{
		for (j = 0; j < l; j++){
			if(matriz[i][j] != -1)
			{
				x = 0;
				busca(i, j,cont);
			}
			if(x < menor && matriz[i][j] )
			{
				menor = x;
			}
		}
	}
	printf("%d\n", menor);
	free(matriz);
	return 0;	
}
