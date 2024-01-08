#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - it prints information about a python list object
 * @p: this pointer to generic PyObject which is of PyListObject type
 *
 * Return: always void.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *py_list = NULL;
ssize_t list_length = 0;
const char *element_type = NULL;

list_length = PyList_Size(p);
py_list = (PyListObject *)p;
printf("[*] Size of the Python List = %ld\n", list_length);
printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));

for (ssize_t i = 0; i < list_length; i++) {
    element_type = Py_TYPE(py_list->ob_item[i])->tp_name;
    printf("Element %ld: %s\n", i, element_type);
}
}
