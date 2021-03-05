from enlace import *
from time import time
import numpy as np
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os

#imageR = imageInput()
#Tk().withdraw()
#imageR=askopenfilename(initialdir=os.getcwd(), title="Select the image you wish to send", filetypes=[("Image Files", ".png"), ("Image Files", ".jpg"), ("Image Files", ".jpeg")])
imageR='./img/transmission.png'
    
header_size=4

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return units.get(unit)*time, unit

def main():
    try:
        door="COM5"
        com1 = enlace(door)
        com1.enable()
        #print(f'Abriu a porta {door}')
        
        with open(imageR, 'rb') as f:
            txBuffer = f.read()
            
        size=len(txBuffer)
        header=size.to_bytes(header_size, 'big')
        
        start_time = time()
        
        com1.sendData(header)
        com1.sendData(txBuffer)
        time_to_send=time() - start_time
        time, unit=process_time(time_to_send, 'ms')
        #print("Enviou: {}" .format(txBuffer)) 
       
        #txSize = com1.tx.getStatus()
        #print("Atualizou o status")
        
        print("-------------------------\nMessage sent.\n-------------------------")
        print(f"Program took {time} {unit} to send.")
        print(f"Message sent at {size/time_to_send} bytes/s.")
        
        rxBufferClient, nRxClient = com2.getData(4)
        answer= int.from_bytes(rxBufferClient, 'big')
        
        if size==answer:
            print(f"Communication successful. There was no loss of data.")
        else:
            print(f"There was a communication error. There were {size-answer} bytes lost.")
            
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()