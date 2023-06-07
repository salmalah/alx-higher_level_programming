#include <Python.h>

void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        PyUnicode_READY(p);
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        Py_UNICODE *value = PyUnicode_AS_UNICODE(p);

        printf("[.] string object info\n");
        printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
        printf("  length: %zd\n", length);
        printf("  value: %ls\n", value);
    }
    else
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}

