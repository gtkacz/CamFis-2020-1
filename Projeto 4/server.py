__author__ = "Gabriel Mitelman Tkacz"

from time import time
from GUI import *
from transmission import Server
import logging, traceback, datetime

def process_time(time, unit):
    units={"ms":1e3, "μs": 1e6, "ns":1e9}
    return round(units.get(unit)*time, 3), unit

def main():
    try:
        logging.basicConfig(filename="server.log", level=logging.INFO, format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        logging.warning('New program instance.')
        door = 'COM6'
        server = Server(door)
        logging.info(f'Enabled server on door {door}')
        
    except:
        e=traceback.format_exc()
        logging.error(e)
        server.end_transmission()
        
if __name__ == "__main__":
    main()