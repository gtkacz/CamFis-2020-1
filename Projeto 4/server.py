from time import time
from GUI import *
from transmission import Server
import logging

imageR = imageInput()

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        logging.basicConfig(filename="server.log", level=logging.INFO)
        server = Server('COM6')
        
    except Exception as error:
        print(error)
        com1.disable()
        

if __name__ == "__main__":
    main()
