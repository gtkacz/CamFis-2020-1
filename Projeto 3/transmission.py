from enlace import *
from numpy import asarray
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Datagram():
    head: bytes = None
    payload: bytes = None
    eop: bytes = None

class Client():
    def __init__(self, door):
        self.HEAD_SIZE=10
        self.EOP_SIZE=4
        self.MAX_PAYLOAD_SIZE=114
        self.com=enlace(door)
        self.com.enable()
        print(f'Abriu a porta {door}')
        self.OVERHEAD=(self.HEAD_SIZE + self.MAX_PAYLOAD_SIZE + self.EOP_SIZE)/self.MAX_PAYLOAD_SIZE
        print(f'Overhead de {self.OVERHEAD}')
    
    def __build_head__(self, transmission_type, filepath=None):
        self.head_transmissiontype_len=1
        self.head_file_len=self.HEAD_SIZE-self.head_transmissiontype_len
        self.transmission_types = {
            'HANDSHAKE':1,
            'HANDSHAKE_SERVER':2,
            'SEND PACKAGE':3,
            'SUCCESS':4,
            'FAILURE':5,
        }
        
        self.transmission_type = self.transmission_types.get(transmission_type.upper())
        if self.transmission_type==1:
            pass
        
        elif self.transmission_type==2:
            if filepath==None:
                raise ValueError("Can't send NORMAL transmission without specifying file path.")
            else:
                filepath=Path(filepath)
                with open(filepath, 'rb') as file:
                    self.txBuffer=file
                self.size=len(self.txBuffer)
                self.head_file_size=self.size.to_bytes(self.head_file_len, 'big')
                self.n_of_datagrams=self.head_file_size/self.MAX_PAYLOAD_SIZE
    
    def __EOP__(self):
        self.EOP_VALUE=2001
        self.EOP=self.EOP_VALUE.to_bytes(self.EOP_SIZE, 'big')
    
    def __build_payloads__(self, data, n):
        self.payloads=[0*self.]
        pass
    
    def __build_packages__(self, data):
        self.packages=[]
        
        self.payload=self.__build_payload__(data)
            
        self.head=self.__build_head__(data)
        
        self.__EOP__()
        
        self.package=Datagram(self.head, self.payload, self.EOP)
        
        self.packages.append(self.package)
    
    def send_all(self):
        for i in range(len(self.packages)):
            self.com.sendData(self.packages[i])
        pass
    
    def end_transmission(self):
        self.com.disable()
        
class Server():
    def __init__(self, door):
        self.HEAD_SIZE=10
        self.EOP_SIZE=4
        self.MAX_PAYLOAD_SIZE=114
        self.com=enlace(door)
        self.com.enable()
        print(f'Abriu a porta {door}')
        
    def end_transmission(self):
        self.com.disable()