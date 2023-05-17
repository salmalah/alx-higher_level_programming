#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_list - A fucntion prints info about python list.
 * @p: A PyObject
 */
void print_python_list(PyObject *p)
{
	int a, s, index = 0;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	a = list->allocated;
	s = var->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	while (index < s)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %d: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		index++;
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
