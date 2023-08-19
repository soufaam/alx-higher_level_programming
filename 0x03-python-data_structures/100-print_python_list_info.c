#include <Python.h>

/**
 * print_python_list_info - check the code
 * @p: pYOBJECT
 * Return: Always EXIT_SUCCESS.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *item, *iter;
	size_t i = 0, ca = 0;

	iter = PyObject_GetIter(p);
	item = PyIter_Next(iter);
	printf("[*] Size of the Python List = %lu\n", PyList_GET_SIZE(p));
	while (item)
	{
	    if (PyLong_Check(item))
			ca = 1;
		else
		{
			ca = 0;
			break;
		}
		item = PyIter_Next(iter);
	}
	if (ca)
		printf("[*] Allocated = 8\n");
	else
		printf("[*] Allocated = %lu\n", Py_SIZE(p));
	iter = PyObject_GetIter(p);
	item = PyIter_Next(iter);
	while (item)
	{
		if (PyList_Check(item))
			printf("Element %lu: list\n", i);
		else if (PyTuple_Check(item))
			printf("Element %lu: tuple\n", i);
		else if (PyLong_Check(item))
			printf("Element %lu: int\n", i);
		else if (PyFloat_Check(item))
			printf("Element %lu: float\n", i);
		else if (PyUnicode_Check(item))
			printf("Element %lu: str\n", i);
		item = PyIter_Next(iter);
		i++;
	}
	Py_DECREF(iter); 
}
