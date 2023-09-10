#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	PyListObject *my_list = (PyListObject *)p;
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", my_list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(my_list->ob_item[i])->tp_name);
	}
}
