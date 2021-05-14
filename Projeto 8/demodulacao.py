from scipy.io import wavfile
from tkinter import Tk, ttk
from funcoes_LPF import *
from tkinter.filedialog import askopenfilename
import scipy.signal as sps
import sounddevice as sd
import os

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
    
    Column1=ttk.Button(window, text='Carregue o arquivo', command=loadsoundfile)
    Column1.grid(row=0, column=0, padx=50, pady=25)

    window.mainloop()

def main(carrier_freq):
    sd.default.channels = 1
    sd.default.samplerate = fs
    
    loadsound()
    
    demodulado=carrier_freq*som
    demodulado_filtrado=LPF(demodulado, 4000, fs)
    
    sd.playrec(demodulado_filtrado)
    sd.wait()

if __name__ == '__main__':
    fs=44100
    som=None
    main(generateSin(20000, 1, 1, fs)[1])