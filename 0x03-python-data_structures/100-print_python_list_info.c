#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: A PyObject list.
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int alloc, i;
	PyObject *obj;

	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
