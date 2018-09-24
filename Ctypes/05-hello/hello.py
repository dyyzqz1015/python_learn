from ctypes import *
import numpy as np
hello=windll.LoadLibrary("hello.dll")
hello.greet.restype=c_char_p
print(hello.greet())

#Passing and returning an integer
print(hello.add_one(4))

a=[5.5,7.6,7.1]
hello.print_array.argtypes=[c_double*3,c_int]
print(hello.print_array(a,3))

print_array.argtypes = [ctl.ndpointer(np.float64,
                                         flags='aligned, c_contiguous'),
                           ctypes.c_int]
A = np.array([1.4,2.6,3.0], dtype=np.float64)
py_print_array(A, 3)