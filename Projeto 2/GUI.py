from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import os

def imageInput():
    Tk().withdraw()
    return askopenfilename(initialdir=os.getcwd(), title="Select the image you wish to send", filetypes=[("Image Files", ".png"), ("Image Files", ".jpg"), ("Image Files", ".jpeg")])

'''def timeWindow(typeOfTransmission, time):
    title=f"Time it took to {typeOfTransmission} the image:"
    time=str(int(time*1000))+"ms"
    
    Tk().withdraw()
    window = Tk()
    window.title(title)
    window.geometry('350x200')
    #lbl = Label(window, text=time, font=("Arial Bold", 50))
    messagebox.showinfo(title, time)
    #lbl.grid(column=0, row=0)
    window.mainloop()
    
#timeWindow('send', 0.05)'''