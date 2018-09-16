from ctypes import *

class Particle(Structure):
    _fields_=[
        ('x',c_double),
        ('y',c_double)
    ]
getp=cdll.struct_array_pointer.getParticles
getp.restype=POINTER(Particle)  #函数的类型是指针类型，但要带结构体

particles=getp()

for i in range(3):
    print(particles[i].x,particles[i].y)