#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: object types for Python
 * Return: nothing
 */


void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(list);
	Py_ssize_t k;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (k = 0; k < size; k++)
	{
		printf("Element %ld: %s\n", k, Py_TYPE(list->ob_item[k])->tp_name);
	}
}
