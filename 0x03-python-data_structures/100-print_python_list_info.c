#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: object types for Python
 * Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t k;

	list_size = Py_SIZE(p);
	l_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n",liste_size);
	printf("[*] Allocated = %ld\n", l_allocated);

	for (k = 0; k < liste_size; k++)
	{
		printf("Element %ld: %s\n", k, Py_TYPE(list->ob_item[k])->tp_name);
	}
}
