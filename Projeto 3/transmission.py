from enlace import *
from time import time
from numpy import asarray
from GUI import *
from pathlib import Path

class Transmission():
    def __init__(self, door):
        self.HEAD_SIZE=10
        self.EOP_SIZE=4
        self.MAX_PAYLOAD_SIZE=128
        self.com=enlace(door)
        self.com.enable()
        print(f'Abriu a porta {door}')
        self.OVERHEAD=(self.HEAD_SIZE + self.MAX_PAYLOAD_SIZE + self.EOP_SIZE)/self.MAX_PAYLOAD_SIZE
    
    def __build_head__(self, transmission_type, filepath=None):
        self.transmission_types = {
            'HANDSHAKE':1,
            'NORMAL':2,
            'LAST':3,
            'SUCCESS':4,
            'FAILURE':5,
        }
        
        self.transmission_type = self.transmission_types.get(transmission_type.upper())
        if self.transmission_type==2:
            if filepath==None:
                raise TypeError("Can't send NORMAL transmission without specifying file path.")
            else:
                filepath=Path(filepath)
                with open(filepath, 'rb') as file:
                    self.txBuffer=file
    
    def __EOP__(self):
        self.EOP_VALUE=2001
        self.EOP=self.EOP_VALUE.to_bytes(self.EOP_SIZE, 'big')
    
    def __build_payloads__(self, data, n):
        self.payloads=[0*self.]
        pass
    
    def __build_packages__(self, data):
        self.packages=[]
        
        if data!=self.HANDSHAKE_VALUE:
            self.payload=self.__build_payload__(data)
            
        self.head=self.__build_head__(data)
        
        
        self.package=self.head+self.payload+self.EOP
    
    def send_all(self):
        for i in range(len(self.packages)):
            self.com.sendData(self.packages[i])
        pass
    
    def __receive_head__(self, datagram):
        self.PAYLOAD_SIZE=None
        pass
    
    def __receive_packages__(self, datagram):
        pass
    
    def __receive_EOP__(self, datagram):
        pass
    
    def receive_all(self, data):
        pass
    
    def send_handshake(self):
        self.HANDSHAKE_VALUE=(0).to_bytes(1, 'big')
        pass
    
    def receive_handshake(self):
        self.HANDSHAKE_RECEIVE_VALUE=1972
    
    def acknowledge(self):
        pass
    
    def end_transmission(self):
        self.com.disable()