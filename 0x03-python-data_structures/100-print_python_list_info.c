#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: A PyObject list.
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int list_size, alloc, i;

	alloc = ((PyListObject *)p)->allocated;
	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < list_size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
