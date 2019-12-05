#include <stdio.h>

int fatorial (int num)
{
	if (num == 1 || num == 0)
		return 1;
	else
		return num*fatorial(num-1);
}

int main(int argc, char **argv)
{
	int n,k,cont;
	
	scanf("%d", &n);
	
	cont = 0;
	while(n > 0)
	{
		k = 1;
		while(fatorial(k) <= n) k++;
		cont++;
		n -= fatorial(k-1);
	}
	printf("%d\n", cont);
	return 0;
}
