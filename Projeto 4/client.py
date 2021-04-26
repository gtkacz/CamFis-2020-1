__author__ = "Gabriel Mitelman Tkacz"

from time import time
from GUI import *
from transmission import Client
import logging, traceback, datetime

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        logging.basicConfig(filename="client.log", level=logging.INFO, format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        logging.warning('New program instance.')
        door = 'COM5'
        client = Client(door)
        logging.info(f'Enabled client on door {door}.')
        logging.info(f'Overhead of {client.OVERHEAD}.')
        imageR = imageInput()
        client.load_data(imageR)
        logging.info(f'Loaded image from path: {imageR}')
    except:
        e=traceback.format_exc()
        logging.error(e)
        client.end_transmission()
        
if __name__ == "__main__":
    main()