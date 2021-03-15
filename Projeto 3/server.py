from enlace import *
from time import time
import numpy as np
import os

imageW = "./img/transmission_receive.png"

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        door="COM6"
        com2 = enlace(door)
        com2.enable()
        #print(f'Abriu a porta {door}')
        
        os.system('py client.py')
        
        start_time = time()

        img_size_b, nRx = com2.getData(4)
        print("Recebeu o header.")
        img_size=int.from_bytes(img_size_b, 'big')
        rxBuffer, nRx = com2.getData(img_size)
        print("Recebeu a imagem.")
        
        time_to_receive=time() - start_time
        time_r, unit=process_time(time_to_receive, 'ms')
        
        answer=nRx.to_bytes(4, 'big')
        com2.sendData(answer)
        print("Mandou de volta o tamanho recebido.")
        
        with open(imageW, 'wb') as f:
            f.write(rxBuffer)
           
        print("-------------------------\nMessage received.\n-------------------------")
        print(f"Program took {time_r} {unit} to receive.")
        print(f"Message received at {img_size/time_to_receive} bytes/s.")
        
        com2.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com2.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
