#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes.
 * @p: The pointer to the object.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *try_str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{

		size = ((PyVarObject *)(p))->ob_size;
		try_str = ((PyBytesObject *)p)->ob_sval;

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", try_str);

		if (size < 10)
			limit = size + 1;
		else
			limit = 10;

		printf("  first %ld bytes:", limit);

		for (i = 0; i < limit; i++)
			if (try_str[i] < 0)
				printf(" %02x", try_str[i] + 256);
			else
				printf(" %02x", try_str[i]);

		printf("\n");
	}
}

/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: The pointer to the object (the list).
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *my_list;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	my_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
