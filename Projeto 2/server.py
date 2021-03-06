from enlace import *
from time import time
import numpy as np

imageW = "./img/transmission_receive.png"

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return units.get(unit)*time, unit

def main():
    try:
        door="COM6"
        com2 = enlace(door)
        #print(f'Abriu a porta {door}')

        com2.enable()
        
        start_time = time()

        img_size_b, nRx = com2.getData(4)
        img_size=int.from_bytes(img_size_b, 'big')
        rxBuffer, nRx = com2.getData(img_size)
        
        time_to_receive=time() - start_time
        time_r, unit=process_time(time_to_receive, 'ms')
        
        answer=nRx.to_bytes(4, 'big')
        com2.sendData(answer)
        
        with open(imageW, 'wb') as f:
            f.write(rxBuffer)
           
        print("-------------------------\nMessage received.\n-------------------------")
        print(f"Program took {time_r} {unit} to receive.")
        print(f"Message received at {size/time_to_receive} bytes/s.")
        
        com2.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com2.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
