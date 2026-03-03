#include<stdio.h>
void main()
{
	int i=1;
	printf("A\n");
	while(i<4)
	{
		printf("B\n");
		i=i+1;
		printf("C\n");
		printf("%d\n",i);
	}
	printf("D\n");
	printf("%d",i);
}