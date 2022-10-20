#include <stdlib.h>
#include <stdio.h>
#include "Python.h"
/**
 * print_python_string - prints info about a python str
 * @p: pointer to the str object, checks if is str
 */
void print_python_string(PyObject *p)
{
	char *unicode = "compact unicode object";
	char *ascii = "compact ascii";
	char *str = NULL, *encoding = NULL;
	ssize_t len = 0;
	int i;
	PyObject *str_ob = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = (ssize_t)PyUnicode_GET_LENGTH(p);

	str_ob = PyUnicode_AsUTF8String(p);
	str = PyBytes_AsString(str_ob);

	for (i = 0; i < len; i++)
	{
		if (str[i] < 0)
		{
			encoding = unicode;
			break;
		}
	}
	if (encoding == NULL)
		encoding = ascii;
	printf("  type: %s\n", encoding);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", str);
}
