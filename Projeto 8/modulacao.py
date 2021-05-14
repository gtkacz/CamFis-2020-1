from tkinter import Tk, ttk
from funcoes_LPF import *
from tkinter.filedialog import askopenfilename
from scipy.io import wavfile
import os
import scipy.signal as sps
import sounddevice as sd
import matplotlib.pyplot as plt

def loadsound():
    window=Tk()
    window.title('Escolha o arquivo')
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')

    def loadsoundfile():
        global som, fs
        file=askopenfilename(initialdir=os.getcwd(), title='Selecione o arquivo de áudio a ser identificado', filetypes=[('Sound Files', '.wav')])
        window.destroy()
        samplerate, som = wavfile.read(file)
        if samplerate != fs:
            number_of_samples = round(len(som) * float(fs) / samplerate)
            som = sps.resample(som, number_of_samples)
            duration = number_of_samples/fs
            fs = int(number_of_samples/duration)
        else:
            duration = len(som)/samplerate
            number_of_samples = samplerate*duration
        som=normalize_sound(som)
    
    Column1=ttk.Button(window, text='Carregue o arquivo', command=loadsoundfile)
    Column1.grid(row=0, column=0, padx=50, pady=25)

    window.mainloop()
    
def main():
    sd.default.channels = 1
    sd.default.samplerate = fs
    
    loadsound()
    
    sd.playrec(som)
    sd.wait()
    
    som_filtrado=LPF(som, 4000, fs)
    
    sd.playrec(som_filtrado)
    sd.wait()
    
    som_modulado=modulate_sound(som_filtrado)
    
    sd.play(som_modulado)
    sd.wait()

if __name__ == '__main__':
    fs=44100
    som=None
    main()