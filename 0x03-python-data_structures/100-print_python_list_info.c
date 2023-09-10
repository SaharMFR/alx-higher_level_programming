#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: The python object (python list).
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int i;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
