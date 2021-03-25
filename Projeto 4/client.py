__author__ = "Gabriel Mitelman Tkacz"

from time import time
from GUI import *
from transmission import Client
import logging

imageR = imageInput()

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        logging.basicConfig(filename="client.log", level=logging.INFO)
        door = 'COM5'
        client = Client(door)
        logging.info(f'Enabled client on door {door}')
        
    except Exception as e:
        logging.error(e)
        client.end_transmission()
        
if __name__ == "__main__":
    main()