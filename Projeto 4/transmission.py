__author__ = "Gabriel Mitelman Tkacz"

from enlace import *
from numpy import asarray
from pathlib import Path
from dataclasses import dataclass
import logging

@dataclass(order=True, frozen=True)
class Datagram():
    head: bytes
    payload: bytes
    eop: bytes = b'\xff' b'\xaa' b'\xff' b'\xaa'

class Client():
    def __init__(self, door):
        self.HEAD_SIZE=10
        self.EOP_SIZE=4
        self.MAX_PAYLOAD_SIZE=114
        self.com=enlace(door)
        self.com.enable()
        self.OVERHEAD=(self.HEAD_SIZE + self.MAX_PAYLOAD_SIZE + self.EOP_SIZE)/self.MAX_PAYLOAD_SIZE
        
    def load_data(self, path):
        with open(path, 'rb') as file:
            self.imageBytes = file.read()
    
    def __build_head__(self, transmission_type, file):
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
    
    def __build_payloads__(self, data, n):
        self.payloads=[0]*n
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
        
    def end_transmission(self):
        self.com.disable()