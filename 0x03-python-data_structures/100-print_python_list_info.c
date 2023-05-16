#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - A function that prints some basic info about Python lists
 *@p: object types for Python
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, l_allocated, i = 0;
	PyObject *it;

	list_size = PyList_Size(p);
	l_allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %ld\n", l_allocated);
	for (i = 0; i < list_size; i++)
	{
		it = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(it)->tp_name);
	}
}
