import ctypes
from ctypes import *


class Data(ctypes.Structure):
    _fields_ = [("freq", ctypes.c_int),
                ("power", ctypes.c_int),
                ("x",c_int*2)]
##第一种方式
data = Data()
data.freq=1
data.power=2
data.x[0]=1
data.x[1]=2

##第二种方式
data = Data(1,2,(1,2))

#第三种方式
data = Data()
data.freq=1
data.power=2
data.x=(6,2)

##第四种方式
data_array=(1,2)
data = Data()
data.freq=1
data.power=2
data.x=data_array

lib = ctypes.cdll['./libstruct_array.so']
fib = lib['sum']

print(fib(data))