#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - it is the Prints bytes information
 * required
 * @p: it is the Python Object
 * Return: return no return
 */
void print_python_bytes(PyObject *p) {
    char *str;
    long int s, i, limit;

    setbuf(stdout, NULL);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        setbuf(stdout, NULL);
        return;
    }

    s = ((PyVarObject *)(p))->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", s);
    printf("  trying string: %s\n", str);

    limit = (s >= 10) ? 10 : s + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++) {
        printf(" %02x", (str[i] >= 0) ? str[i] : 256 + str[i]);
    }

    printf("\n");
    setbuf(stdout, NULL);
}

/**
 * print_python_float - it Prints  the float information
 *
 * @p: it is the Python Object
 * Return: return no return
 */
void print_python_float(PyObject *p)
{
    double v;
    char *f;

    setbuf(stdout, NULL);
    printf("[.] float object info\n");

    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        setbuf(stdout, NULL);
        return;
    }

    v = ((PyFloatObject *)(p))->ob_fval;
    f = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

    // Loop to print each character of the string
    int i;
    printf("  value: ");
    for (i = 0; f[i] != '\0'; i++)
    {
        printf("%c", f[i]);
    }
    printf("\n");

    setbuf(stdout, NULL);
}

/**
 * print_python_list - it is the Printed list of information
 *
 * @p: it is the Python Object
 * Return: return no return
 */
void print_python_list(PyObject *p)
{
    long int s, i;
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

    s = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", s);
    printf("[*] Allocated = %ld\n", list->allocated);

    i = 0;
    while (i < s)
    {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

        if (PyBytes_Check(obj))
            print_python_bytes(obj);
        if (PyFloat_Check(obj))
            print_python_float(obj);

        i++;
    }
    setbuf(stdout, NULL);
}
