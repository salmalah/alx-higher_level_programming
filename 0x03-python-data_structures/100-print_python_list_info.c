#include <Python.h>

/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: A PyObject list.
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	PyListObject *l;
	int list_size, alloc, index;

	l =  (PyListObject *)p;
	alloc = l->allocated
	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (index = 0; index < list_size; index++)
	{
		printf("Element %d: ", index);

		obj = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
