#include <Python>
#include <object.h>
#include <listobject.h>

/**
 * print_python_bytes - Prints some basic info about Python bytes.
 * @p: The pointer to the object.
 */
void print_python_bytes(PyObjects *p)
{
	long int size, i;
	char *try_str;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		size = ((PyVarObject *) p)->ob_size;
		try_str = ((PyBytesObject *) p)->ob_sval;

		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", try_str);

		if (size < 10)
			size++;
		else
			size = 10;

		printf("  first %ld bytes:", size);

		for (i = 0; i < size; i++)
		{
			if (try_str[i] < 0)
				printf(" %02x", try_str[i] + 256);
			else
				printf(" %02x", try_str[i]);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}


/**
 * print_python_list - Prints some basic info about Python lists.
 * @p: The pointer to the object (the list).
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *my_list = (PyListObject *)p;
	PyObject *item;

	size = ((PyVarObject *) p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %li\n", my_list->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *) p)->ob_item[i];
		printf("Element %i: %s\n", i, (item->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
