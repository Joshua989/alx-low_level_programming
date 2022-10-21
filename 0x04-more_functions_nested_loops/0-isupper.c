#include "main.h"
/**
 * -isupper  - a function that check for a uppercase character
 *  @ an imput integer
 *  return 1 : if c is uppercase, 0 if otherwise
 *  */
int _isupper(int c)
{
	char i;
	int upper = 0;

	for (i = 'A' ; i <= 'Z' ; i++)
	{
		if(i == c)
			upper = 1;
	}
	return (upper);
}


