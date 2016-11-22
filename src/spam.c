//$ begin Python.h
#include <Python.h>
//$ end

//$ begin spam_system
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    if (!PyArg_ParseTuple(args, "s", &command)) return NULL;

    const int sts = system(command);
    return Py_BuildValue("i", sts);
}
//$ end

//$ begin SpamMethods
static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
//$ end

//$ begin initspam
PyMODINIT_FUNC
initspam(void)
{
   (void)Py_InitModule("spam", SpamMethods);
}
//$ end
