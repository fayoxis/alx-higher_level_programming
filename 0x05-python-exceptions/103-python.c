#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    char *string;
    Py_ssize_t size, i, limit;

    setbuf(stdout, NULL);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size + 1;

    printf("  first %zd bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        unsigned char byte = string[i];
        printf(" %02x", byte);
    }

    printf("\n");
    setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_float(PyObject *p)
{
    double val;
    char *nf;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        setbuf(stdout, NULL);
        return;
    }

    val = PyFloat_AsDouble(p);
    nf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

    printf("  value: %s\n", nf);
    setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;
    PyObject *obj;

    setbuf(stdout, NULL);
    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        setbuf(stdout, NULL);
        return;
    }

    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);

        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        if (PyFloat_Check(obj))
            print_python_float(obj);
    }
    setbuf(stdout, NULL);
}
