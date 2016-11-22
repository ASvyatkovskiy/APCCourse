# -*- python -*-
#$ begin speak
def speak(string):
    print("Hello %s" % string)
#$ end

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#$ begin f
def f(x):
    return x**2 - x
#$ end

#$ begin integrate_f
def integrate_f(a, b, N):
    s = 0
    dx = (b - a)/N
    for i in range(N):
        s += f(a + i*dx)
    return s*dx
#$ end

#$ begin f1
def f1(double x):
    return x**2 - x
#$ end

#$ begin integrate_f1
def integrate_f1(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a)/N
    for i in range(N):
        s += f1(a + i*dx)
    return s*dx
#$ end

#$ begin f2
cdef double f2(double x) except? -2:
    return x**2 - x
#$ end

#$ begin integrate_f2
def integrate_f2(double a, double b, int N):
    cdef int i
    cdef double s, dx
    s = 0
    dx = (b - a)/N
    for i in range(N):
        s += f2(a + i*dx)
    return s*dx
#$ end
