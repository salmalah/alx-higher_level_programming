#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: object types for Python
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	Py_ssize_t k;

	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n",list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < size; k++)
	{
		printf("Element %ld: %s\n", k, Py_TYPE(list->ob_item[k])->tp_name);
	}
}
