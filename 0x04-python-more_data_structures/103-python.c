#include <Python.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p)
{
        Py_ssize_t size, first;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return ;
        }
        size = PyBytes_Size(p);
        printf("  size: %lu\n", size);
        printf("  trying string: %s\n", PyBytes_AsString(p));

        if (size > 9)
                first = 10;
        else
                first = size + 1;
        printf("  first %lu bytes: ", first);
        for (Py_ssize_t i = 0; i < first; i++)
        {
                unsigned char byte = PyBytes_AsString(p)[i];
                if (i == first - 1)
                         printf("%02x", byte);
                else
                        printf("%02x ", byte);
        }
        printf("\n");
}   
    
void print_python_list(PyObject *p) 
{   
        PyObject *item, *iter;
        size_t i = 0;
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %lu\n", PyList_GET_SIZE(p));
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        iter = PyObject_GetIter(p);
        if (iter)
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
                else if (PyBytes_Check(item))
                {
                        printf("Element %lu: bytes\n", i);
                        print_python_bytes(item);
                }
                item = PyIter_Next(iter);
                i++;
        }
}
