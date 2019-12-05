#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	int j, r, *lista,jog = 1,maiorJ;
	int maior = 0, cont, i, k = 0;
	
	scanf("%d %d", &j, &r);
	lista = (int*)malloc(j*r*sizeof(int));
	
	for(i = 0; i < j*r; i++)
		scanf("%d", &lista[i]);
	
	while(k < j)
	{
		cont = 0;
		for (i = k; i < j*r; i+=j)
		{
			cont += lista[i];
		}
		if(cont >= maior)
		{
			maior = cont;
			maiorJ = jog;
		}
		jog++;
		k++;
	}
	printf("%d\n", maiorJ);
	return 0;
}