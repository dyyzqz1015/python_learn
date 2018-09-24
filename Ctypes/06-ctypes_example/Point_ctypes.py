import ctypes
from ctypes import *
import numpy as np
from enum import IntEnum

#######################################
###        加载动态链接库
#######################################
cdll=windll.LoadLibrary("Point.dll")
math=windll.LoadLibrary("Point.dll")
anEnum=windll.LoadLibrary("Point.dll")

########## 整数调用 #################
print(math.add_int(4,8))
########## 浮点数调用 #################
math.add_float.restype=c_float
math.add_float.argtypes=[c_float,c_float]
print(math.add_float(6.5,7.2))
print(math.add_float(c_float(6.5),c_float(7.2)))

######### 指针调用  ###############

math.add_float_ref.restype=c_float
math.add_float_ref.argtypes=[POINTER(c_float),POINTER(c_float),POINTER(c_float)]


a=c_float(2.2)
b=c_float(4.5)
c=c_float()
math.add_float_ref(byref(a),byref(b),byref(c))
print(c.value)
math.add_float_ref(pointer(a),pointer(b),pointer(c))
print(c.value)
######### 数组指针调用-1  ###############
a=(c_int*3)(-1,2,5)
b=(c_int*3)(-1,3,3)
res=(c_int*3)(0,0,0)
n=c_int(3)

# math.add_int_aray.restype=c_int
# math.add_int_aray.argtypes=[POINTER(c_int),POINTER(c_int),POINTER(res),c_int]

math.add_int_array(a,b,res,n)

for i in range(len(res)):
    print(res[i])

######### 数组指针调用-2  ###############

a=np.array([1,2,-5],dtype=c_int)
b=np.array([-2,3,3],dtype=c_int)
res=np.zeros(3,dtype=c_int)
n=c_int(3)
intp=POINTER(c_int)

i=a.ctypes.data_as(intp)
j=b.ctypes.data_as(intp)
k=res.ctypes.data_as(intp)

math.add_int_array(i,j,k,n)

print(res)

######### 结构体调用-1  ###############


class Rectangle(Structure):
    _fields_=[
        ("width",c_float),
        ("height",c_float)
    ]

math.area.restype=c_float
math.area.argtypes=[Rectangle]
r=Rectangle(6,5)

print(math.area(r))
######### 结构体调用-1  ###############
###  void show_point(Point point)
#######################################

class Point(Structure):
    _fields_=[
        ('x',c_int),
        ('y',c_int)
    ]

cdll.show_point.restype=c_void_p
cdll.show_point.argtypes=[Point]

a=Point(1,4)
cdll.show_point(a)

######### 结构体调用-2  ###############
###  void move_point(Point point)
#######################################
cdll.move_point.restype=c_void_p
cdll.move_point.argtypes=[Point]
b=Point(10,6)
cdll.move_point(b)

######### 结构体调用-3  ###############
###  void move_point_by_ref(Point point)
#######################################

cdll.move_point_by_ref.restype=c_void_p
cdll.move_point_by_ref.argtypes=[POINTER(Point)]
c=Point(5,6)
cdll.move_point_by_ref(byref(c))

######### 结构体调用-3  ###############
###  Point get_point(int x, int y);
#######################################
cdll.get_point(7,2)

######### 结构体调用-3  ###############
###  Point get_point_float(int x, int y);
#######################################
class Point_float(Structure):
    _fields_=[
        ('x',c_float),
        ('y',c_float)
    ]

# cdll.get_point_float.restype=None
cdll.get_point_float.argtypes=[c_float,c_float]
cdll.get_point_float(8.6,2.8)

######### 结构体调用-4  ###############
###  Point get_default_point(int x, int y);
#######################################
cdll.get_default_point()

######### 枚举的调用-1  ###############
###  int getAnEnumValue(MyEnum anEnum); 没有成功
#######################################



class CtypesEnum(IntEnum):

    """A ctypes-compatible IntEnum superclass."""

    @classmethod

    def from_param(cls, obj):

        return int(obj)

class MyEnum(IntEnum):
    ZERO=0
    ONE=1
    TWO=2

get_an_enum_value = anEnum.getAnEnumValue
get_an_enum_value.argtypes = [MyEnum]
get_an_enum_value.restype = c_int


