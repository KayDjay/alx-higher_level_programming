#include <stdio.h>
#include "python_list_info.h"


/**
 * print_python_list_info - print a pyhton list
 *
 * @p: list object to be printed
 *
 * Return: list
 */

void print_python_list_info(PyObject *p)
{
	const char *type_name;
	PyObject *element;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t a = 0; a < size; a++)
	{
		element = PyList_GetItem(p, a);
		type_name = Py_TYPE(element)->tp_name;
		printf("Element %ld: %s\n", a, type_name);
	}
}
