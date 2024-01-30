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
void print_python_string(PyObject *p) {
    Py_ssize_t i 
    wprintf(L"[.] string object info\n");
    if (strcmp(p->ob_type->tp_name, "str")) {
        wprintf(L"  [ERROR] Invalid String Object\n");
        return;
    }
    if (PyUnicode_IS_COMPACT_ASCII(p))
        wprintf(L"  type: compact ascii\n");
    else
        wprintf(L"  type: compact unicode object\n");
    wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(p));
    
    Py_UNICODE* string_data = PyUnicode_AS_UNICODE(p);
    for (i = 0; i < PyUnicode_GET_LENGTH(p); i++) {
        wprintf(L"  value[%zd]: %lc\n", i, string_data[i]);
    }
}
