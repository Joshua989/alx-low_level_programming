#include <stdio>

/**
 * _putchar - writes the chatacter c to stdout
 * @c: The character to print
 *
 * Return on success 1.
 * on error, -1 is returned, and error to set appropraitely.
 **/
int _putchar(char c)
{
	return (write(1, &c, 1));
}

