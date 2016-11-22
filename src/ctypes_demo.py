#$ begin import_libc
import ctypes
libc = ctypes.CDLL("libc.dylib")
#$ end

if False:
#$ begin import_libc2
    import ctypes.util
    libc = ctypes.util.find_library("c")
    libc = ctypes.CDLL(libc)
#$ end

#$ begin system
libc.system("echo hello world")
#$ end

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#$ begin strchr
strchr = libc.strchr
print strchr("abcdef", ord("d"))
#$ end
# 8059983

#$ begin strchr_restype
strchr.restype = ctypes.c_char_p
print strchr("abcdef", ord("d"))
#$ end
# 'def'

#$ begin strchr_argtypes
strchr.argtypes = [ctypes.c_char_p, ctypes.c_char]
print strchr("abcdef", "d")
#$ end
# 'def'

#$ begin strchr_bad_argtypes
try:
    strchr("abcdef", "def")
except Exception, e:
    print e
#$ end
#Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#ArgumentError: argument 2: exceptions.TypeError: one character string expected

if False:                               # will crash python
#$ begin strlen_bad_arg
    print libc.strlen(1)
#$ end

#$ begin strlen_bad_arg2
libc.strlen.argtypes = [ctypes.c_char_p]
try:
    print libc.strlen(1)
except Exception, e:
    print e
#$ end
# argument 1: <type 'exceptions.TypeError'>: wrong type  (ctypes.ArgumentError)

#$ begin strlen_bad_narg
print libc.strlen("abc", "def")
#$ end
# 3

