from enlace import *
from time import time
#from datetime import datetime
import numpy as np
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os

#imageR = imageInput()
Tk().withdraw()
imageR=askopenfilename(initialdir=os.getcwd(), title="Select the image you wish to send", filetypes=[("Image Files", ".png"), ("Image Files", ".jpg"), ("Image Files", ".jpeg")])
#imageR='./img/transmission.png'
    
header_size=4

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time,3), unit

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
        print(f"Montou o header: {header}")
        
        start_time = time()
        
        com1.sendData(header)
        print("Mandou o header.")
        com1.sendData(txBuffer)
        time_to_send=time() - start_time
        time_s, unit=process_time(time_to_send, 'ms')
        
        print("-------------------------\nMensagem enviada.\n-------------------------")
        print(f"Programa levou {time_s} {unit} para enviar.")
        print(f"Mensagem enviada a {round((size/time_to_send), 3)} bytes/s.")
        
        rxBufferClient, nRxClient = com1.getData(4)
        answer=int.from_bytes(rxBufferClient, 'big')
        
        if size==answer:
            print("Comunicação bem-sucedida. Não houve perda de dados.")
        else:
            print(f"Ocorreu um erro de comunicação. {size - answer} bytes foram perdidos.")
            
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

if __name__ == "__main__":
    main()
