import skrf as rf
from skrf.data import ring_slot

# ring_slot=rf.Network('data/ring slot.s2p')

print(ring_slot)
ring_slot.s

import os 
import numpy as np
from ctypes import *

class Driver():
    def __init__(self,port=“COM1”):
      os.chdir(r"./xaVNA_win32/release")
      usb_port=bytes(port,encoding="utf-8")
      self.dll=cdll.LoadLibrary("libxavna-0")
      
    def is_tr(self):
      ret=self.dll.xavan_is_tr(self.lib)
      return ret
    
    def set_params(self,freq_kHz=10000,atten=0,port=1,nWait=20)
      ret=self.dll.xavna_set_params(self.lib,freq_kHz,port,nWait)
      
      return ret
    
    def read_values(self):
      temp_data=(c_double*4)()
      ret=self.dll.xavna_read_values(self.lib,byref(temp_data),50)
      
      return ret
    
    def read_values_raw(self):
      temp_data=(c_double*8)()
      ret=self.dll.xavna_read_values_raw(self.lib,byref(temp_data),50)
      
      return ret
    
    def one_port(self,startFreq=200e6,stopFreq=250e9,pointcount=50):
      freq_points=np.linspace(startFreq,stopFreq,pointcount)
      read_data=self.read_values()
      port_data=[]
      for freq in freq_points:
        self.set_params(freq)
        port_data.append(read_data)
    def one_port(self,startFreq=200e6,stopFreq=250e9,pointcount=50):
      freq_points=np.linspace(startFreq,stopFreq,pointcount)
      read_data=self.read_values_raw()
      port_data=[]
      for freq in freq_points:
        self.set_params(freq)
        port_data.append(read_data)
if __name__=="__main__":
    driver=Driver()
    
    
    
    
    
    
    
