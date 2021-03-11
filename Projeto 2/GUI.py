from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os

def imageInput():
    Tk().withdraw()
    return (askopenfilename(initialdir=os.getcwd(), title="Select the image you wish to send", filetypes=[("Image Files", ".png"), ("Image Files", ".jpg"), ("Image Files", ".jpeg")]))

def timeWindow(typeOfTransmission, time):
    Tk().withdraw()
    messagebox.showinfo(title=f"Time it took to {typeOfTransmission} image", message=f"Message took {time} to {typeOfTransmission}.")
    
class App():
    def __init__(self):
        pass