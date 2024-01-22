#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_bytes -this  Prints bytes the  information
 * required 
 * @p: this is the Python Object
 * Return: return no return
 */
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);
{
	char *str;
	long int s, i, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	while (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL); 
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		limit = 10;
	else
		limit = s + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - this is the Prints float information
 *
 * @p: it is the Python Object
 * Return: returns  no return
 */
void print_python_float(PyObject *p)
{
	double v;
	char *f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	while (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	v = ((PyFloatObject *)(p))->ob_fval;
	f = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", f);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - it actually Prints list information
 *
 * @p: this the Python Object
 * Return: returns no return
 */
void print_python_list(PyObject *p)
{
	int s, i, alloc;
	PyVarObject *v = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	s = v->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < s; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		while (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
