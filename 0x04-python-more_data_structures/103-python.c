#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a bytes object
 *
 * @p: Python bytes object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    
    /* Check if the object is a valid bytes object */
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    /* Determine the limit for printing the bytes */
    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    /* Print each byte in hexadecimal format */
    for (i = 0; i < limit; i++)
    {
        if (string[i] >= 0)
            printf(" %02x", string[i]);
        else
            printf(" %02x", 256 + string[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object
 *
 * @p: Python list object
 * Return: void
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

    /* Iterate over the list elements and print their information */
    for (i = 0; i < size; i++)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
