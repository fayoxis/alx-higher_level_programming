#include <stdio.h>
#include <string.h>

/**
 * print_python_string - Function that prints information
 * about Python strings
 * @objects: Array of PyObject pointers representing Python objects.
 * @size: Size of the array.
 * This function iterates over an array of PyObject pointers
 * and prints information
 * about each Python string object in the array.
 */
void print_python_string(PyObject *objects)
{
PyObject *str, *repr;
(void)repr;
printf("[.] Python string object information\n");
for (int i = 0; i < size; i++) {
/* Check if the object is a string */
if (strcmp(objects[i]->ob_type->tp_name, "str"))
{
printf("  [ERROR] Invalid String Object\n");
continue;
}
/* Check if the string is compact ASCII or compact Unicode */
if (PyUnicode_IS_COMPACT_ASCII(objects[i]))
printf("  type: compact ASCII\n");
else
printf("  type: compact Unicode object\n");
/* Get the representation and encoded string value */
repr = PyObject_Repr(objects[i]);
str = PyUnicode_AsEncodedString(objects[i], "utf-8", "~E~");
/* Print the length and value of the string */
printf("  length: %ld\n", PyUnicode_GET_SIZE(objects[i]));
printf("  value: %s\n", PyBytes_AsString(str));
}
}
