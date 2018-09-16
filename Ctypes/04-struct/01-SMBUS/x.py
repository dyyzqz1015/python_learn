from ctypes import *
SMB_MAX_DATA_SIZE = 5  #对应宏定义
ARRAY5 = c_ubyte * SMB_MAX_DATA_SIZE  #定义5个无符号的字符串数据

#定义结构体
class SMB_REQUEST(Structure):
    #定义定段
    _fields_ = [
        ("Address", c_ubyte),   #定义无字符的字符串，c_ubyte对应unsigned char
        ("Command", c_ubyte),
        ("BlockLength", c_ubyte),
        ("Data", ARRAY5)]       #定义字符串数组

smbus_read_byte = CDLL('x').SmBusReadByte #加载动态库并指定引用的函数
smbus_read_byte.argtypes = [c_void_p,POINTER(SMB_REQUEST)]  #传参数类型
smbus_read_byte.restype = c_int     #指定函数的类型

open_smbus = CDLL('x').OpenSmbus   #加载动态库并引用函数
open_smbus.argtypes = []            #指定参数的类型是C语言所对应的 viod,所对应的参数是（void）
open_smbus.restype = c_void_p       #指定函数的类型，所对应的是viod的函数类型

handle = open_smbus()               #不明白为什么还要实例化
print('handle = %08Xh' % handle)
# print('handle=%08Xh' % CDLL('x').OpenSmbus())  #这里就来解释为什么要实例化，其实并非实例化，而是要调用的函数
smb_request = SMB_REQUEST(1,2,7)          #这里可以少传参数或不传参数进来
# smb_request.BlockLength=5                 #通过这个例子，可以少传参数或不传参数，使用时再定义

#宏定义的时候是typedef void* SMBUS_HANDLE；而为什么不是传指针进来
#而这里为什么传OpenSmbus进来按组合的定义来说应该是 void* handle,这三者是什么样的关系
print('returned =',smbus_read_byte(handle,byref(smb_request)))
print('Address =',smb_request.Address)
print('Command =',smb_request.Command)
print('BlockLength =',smb_request.BlockLength)
for i,b in enumerate(smb_request.Data):
    print('Data[%d] = %02Xh' % (i,b))