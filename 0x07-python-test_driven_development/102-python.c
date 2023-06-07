#include <Python.h>

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		PyUnicode_READY(p);
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);
		Py_UNICODE *value = PyUnicode_AS_UNICODE(p);

		printf("[.] string object info\n");
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n", length);
		printf("  value: %ls\n", value);
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}

