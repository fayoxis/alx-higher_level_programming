#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>
/**
 * print_python_string - Function that prints information
 * about Python strings
 * @point: Array of PyObject pointers representing Python objects.
 */
void print_python_string(PyObject *point)
{
	wprintf(L"[.] string object info\n");
	while(strcmp(point->ob_type->tp_name, "str"))
	{
		wprintf(L"  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(point))
		wprintf(L"  type: compact ascii\n");
	else
		wprintf(L"  type: compact unicode object\n");
	wprintf(L"  length: %lu\n", PyUnicode_GET_LENGTH(point));
	wprintf(L"  value: %ls\n", PyUnicode_AS_UNICODE(point));
}
