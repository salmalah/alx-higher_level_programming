#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - A function that prints some basic info about Python lists
 * @p: object types for Python
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
