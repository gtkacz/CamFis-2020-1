from enlace import *
from time import time
from numpy import asarray
from GUI import *

class Transmission():
    def __init__(self, door):
        self.HEAD_SIZE=10
        self.EOP_SIZE=4
        self.MAX_PAYLOAD_SIZE=128
        self.com=enlace(door)
        self.com.enable()
        print(f'Abriu a porta {door}')
        self.OVERHEAD=(self.HEAD_SIZE + self.MAX_PAYLOAD_SIZE + self.EOP_SIZE)/self.MAX_PAYLOAD_SIZE
    
    def __build_head__(self, transmission_type):
        pass
    
    def __EOP__(self):
        self.EOP_VALUE=2001
        self.EOP=self.EOP_VALUE.to_bytes(self.EOP_SIZE)
    
    def __build_payload__(self, data, n):
        pass
    
    def __build_package__(self, data):
        if data!=self.HANDSHAKE_VALUE:
            self.payload=self.__build_payload__(data)
        self.head=self.__build_head__(data)
        
        
        self.package=self.head+self.payload+self.EOP
    
    def send_all(self):
        pass
    
    def __receive_head__(self, datagram):
        pass
    
    def __receive_packages__(self, datagram):
        pass
    
    def __receive_EOP__(self, datagram):
        pass
    
    def receive_all(self, datagram):
        pass
    
    def send_handshake(self):
        self.HANDSHAKE_VALUE=0.to_bytes(4, 'big')
        pass
    
    def receive_handshake(self):
        self.HANDSHAKE_RECEIVE_VALUE=1972
    
    def acknowledge(self):
        pass
    
    def end_transmission(self):
        self.com.disable()