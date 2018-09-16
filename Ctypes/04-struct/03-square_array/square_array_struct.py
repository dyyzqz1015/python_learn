import ctypes
import numpy

testlib = ctypes.cdll.LoadLibrary('square_array_struct.dll')

class Data(ctypes.Structure):
     _fields_ = [("n", ctypes.c_int),
                ("ina", ctypes.POINTER(ctypes.c_double)),
                ("outa", ctypes.POINTER(ctypes.c_double))]

n=5
outa = numpy.zeros(n,numpy.float)
ina = numpy.linspace(1.0,200.0,n)

data = Data(n,
            numpy.ctypeslib.as_ctypes(ina),
            numpy.ctypeslib.as_ctypes(outa))

print("initial array",ina)
testlib.square_array.restype = None
testlib.square_array(ctypes.byref(data))
print("final array",outa)