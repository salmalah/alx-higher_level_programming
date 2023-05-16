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
	int list_size, l_ollocated, index = 0;

	l =  (PyListObject *)p;
	l_ollocated = (*l).allocated;
	list_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", l_ollocated);
	while (index < list_size)
	{
		printf("Element %d: ", index);
		obj = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		index++;
	}
}
