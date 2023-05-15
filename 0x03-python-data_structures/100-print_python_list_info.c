#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - A function that prints some basic info about Python lists
 *@p: object types for Python
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;

	list_size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", list_size); 
}

