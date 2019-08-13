import skrf as rf
from skrf.data import ring_slot

# ring_slot=rf.Network('data/ring slot.s2p')

print(ring_slot)
ring_slot.s

import os 
import numpy as np
from ctypes import *
import matplotlib.pyplot as plt

class Driver():
    def __init__(self,port="COM6"):
        os.chdir(r"./xaVNA_win32/release")
        usb_port=bytes(port,encoding="utf-8")
        self.dll=cdll.LoadLibrary("libxavna-0")
        self.lib=self.dll.xavna_open(usb_port)
        self.dll.xavna_set_params(self.lib,10000,0,1,20)
      
    def is_tr(self):
        ret=self.dll.xavna_is_tr(self.lib)
        return ret
    
    def set_params(self,freq_kHz=10000,atten=0,port=1,nWait=20):
        ret=self.dll.xavna_set_params(self.lib,freq_kHz,atten,port,nWait)
      
        return ret
    
    def read_values(self):
        temp_data=(c_double*4)()
        data=[]
        ret=self.dll.xavna_read_values(self.lib,byref(temp_data),50)
        for i in temp_data:
            data.append(i)
        return data
    
    def read_values_raw(self):
        temp_data=(c_double*8)()
        data=[]
        ret=self.dll.xavna_read_values(self.lib,byref(temp_data),50)
        for i in temp_data:
            data.append(i)
        return data
    
    def one_port(self,startFreq=10000,stopFreq=100000,pointcount=50):
        freq_list=np.linspace(startFreq,stopFreq,pointcount,dtype=int)
        freq_points=freq_list.tolist()
        port_data=[]
        s11_real=[]
        s11_imag=[]
        s21_real=[]
        s21_imag=[]
        for freq in freq_points:
            self.dll.xavna_set_params(self.lib,freq,0,1,20)
            data=self.read_values()
            port_data.append(data)
            s11_real.append(data[0])
            s11_imag.append(data[1])
            s21_real.append(data[2])
            s21_imag.append(data[3])
        
        print(port_data)
        print("s11_real",len(s11_real),s11_real)
        plt.plot(freq_points,s11_real)
        plt.plot(freq_points,s11_imag)
        plt.plot(freq_points,s21_real)
        plt.plot(freq_points,s21_imag)
        plt.legend(["s11_real","s11_imag","s21_real","s21_imag"])
        plt.show()
    def two_port(self,startFreq=200e6,stopFreq=250e9,pointcount=50):
        freq_points=np.linspace(startFreq,stopFreq,pointcount)
        read_data=self.read_values_raw()
        port_data=[]
        for freq in freq_points:
            self.set_params(freq)
            port_data.append(read_data)
    def data_demo(self):
        startFreq=10000
        stopFreq=100000
        pointcount=10
        freq_points=np.linspace(startFreq,stopFreq,pointcount,dtype=int)
        freq=freq_points.tolist()
        for i in freq:
            self.dll.xavna_set_params(self.lib,i,0,1,20)

            data=self.read_values_raw()
            for j in data:
                print(j)

        

if __name__=="__main__":
    driver=Driver()
    tr=driver.one_port()
    print(tr)
    
    
    
    
    
    
    
