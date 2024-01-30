#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>
/**
 * print_python_string - Function that prints information
 * about Python strings
 * @p: Array of PyObject pointers representing Python objects.
 */
void print_python_string(PyObject *p)
{
    wprintf(L"[.] string object info\n");
    if (strcmp(p->ob_type->tp_name, "str"))
    {
        wprintf(L"  [ERROR] Invalid String Object\n");
        return;
    }
    
    Py_UNICODE* unicode = PyUnicode_AS_UNICODE(p);
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_ssize_t i;
    
    for (i = 0; i < length; i++)
    {
        wprintf(L"  character %lu: %lc\n", i, unicode[i]);
    }
}
