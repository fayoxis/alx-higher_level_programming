#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *byteObj = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    const char *data = PyBytes_AsString(p);
    int i;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", data);
    if (size < 10)
        printf("  first %zd bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    i = 0;
    while (i < size && i < 10)
    {
        printf(" %02hhx", data[i]);
        i++;
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *listObj = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    int i = 0;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", listObj->allocated);

    while (i < size)
    {
        PyObject *item = listObj->ob_item[i];
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %i: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
        
        i++;
    }
}
