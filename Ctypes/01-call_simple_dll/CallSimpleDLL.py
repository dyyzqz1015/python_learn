#!/usr/bin/env python

#The ctypes library includes datatypes for passing data to DLLs
#For instance, c_int to pass integer pointers
from ctypes import *

#Load the DLL
dll = cdll.LoadLibrary("SimpleDLL.dll")

x = 5
y = 3

#Create sum as a c style integer
sum = c_int(0)
# string = create_string_buffer('',20)
string=create_string_buffer(20)


#Function Prototype: int addNumbers (int x, int y, int *sum, char *string)

#Call the Function
#Pass pointers using the byref keyword
returnValue = dll.addNumbers(x, y, byref(sum), byref(string))

#Print Results
print("Sum: ", sum, "\n")
print("String: ", repr(string.raw), "\n")
print("returnValue: ", returnValue, "\n")

