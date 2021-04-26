from enlace import *
from time import time
import numpy as np
from GUI import *
from timeit import timeit

imageR = imageInput()
    
header_size=4

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        door="COM5"
        com1 = enlace(door)
        com1.enable()
        print(f'Abriu a porta {door}.')
        
        with open(imageR, 'rb') as f:
            txBuffer = f.read()
            print("Abriu a imagem.")
            
        size=len(txBuffer)
        header=size.to_bytes(header_size, 'big')
        print(f"Montou o header:/n {header}")
        
        start_time = time()
        
        com1.sendData(header)
        print("Mandou o header.")
        com1.sendData(txBuffer)
        print("Mandou a imagem.")
        time_to_send=time() - start_time
        time_s, unit=process_time(time_to_send, 'ms')
        
        print("-------------------------\nMessage sent.\n-------------------------")
        print(f"Program took {time_s} {unit} to send.")
        print(f"Message sent at {size/time_to_send} bytes/s.")
        
        rxBufferClient, nRxClient = com1.getData(4)
        answer=int.from_bytes(rxBufferClient, 'big')
        
        if size==answer:
            print("Communication successful. There was no loss of data.")
        else:
            print(f"There was a communication error. There were {size - answer} bytes lost.")
            
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

if __name__ == "__main__":
    main()
