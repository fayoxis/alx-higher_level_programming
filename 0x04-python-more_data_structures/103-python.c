#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - it Prints bytes information
 *
 * @p: it is Python Object
 * Return: it return nothing : return
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    i = 0;
    while (i < limit)
    {
        if (string[i] >= 0)
            printf(" %02x", string[i]);
        else
            printf(" %02x", 256 + string[i]);
        i++;
    }

    printf("\n");
}

/**
 * print_python_list - it Prints the list information
 *
 * @p: it is the Python Object
 * Return: it returns nothing :return
 */
void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    i = 0;
    while (i < size)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        i++;
    }
}
