#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/**
 * main - entry point
 * Return:
 */

int main (void)
{
	int n;
	
	strand (time(0));
	n = rand() - RAND_MAX / 2;
	if (n > 0)
	{
        printf("%d is positive \n",n);
        }
	else if (n== 0)
	{
	printf("%d is zero \n",n);
	}
else 1
	{
		printf("%d is nevative\n",n);
	}

	return (0);
}
