#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: A PyObject list.
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	Py_ssize_t size, alloc, i;

	alloc = ((PyListObject *)p)->allocated;
	size = PyList_Size(p); 
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
