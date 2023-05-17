#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);

        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
        else
        {
            printf("%s\n", Py_TYPE(item)->tp_name);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *buffer;

    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);

    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", size <= 10 ? size : 10);

    buffer = (unsigned char *)PyBytes_AsString(p);
    for (i = 0; i < (size <= 10 ? size : 10); i++)
    {
        printf("%02x%c", buffer[i], i == 9 || i == size - 1 ? '\n' : ' ');
    }
}
