#include <stdio.h>
#include <math.h>

typedef long long int llu;


llu fatorial(llu num)
{
	int i, aux = 1;
	
	for (i = num; i > 0; i--)
		aux *=i; 
	
	return aux;
}


int main(void) {
	llu n,i,primo, raiz,cont = 0, res = 0;
	int flag;
	
	scanf("%lld", &n);
	raiz = (int) sqrt(n) + 1;
	
	primo = 2;
	
	flag = 0;
	while (n % 2 == 0)
	{
		if (!flag)
		{
		    flag = 1;
			cont++;
		}
		n /= 2;
	}
	
	primo = 3;
	if (n % primo == 0) cont++;
	
	while (n > 1)
	{
	    flag = 0;
		while (n % primo && primo < raiz)
		{
		    flag = 1;
			primo +=2;
		}
		if (flag)
			cont++;

		n /= primo;
	}
	
	for (i = 2; i < cont + 1; i++)
		res += fatorial(cont)/(fatorial(i) * fatorial(cont-i));
	
	printf("%d\n", res);
	return 0;
}