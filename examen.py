from tkinter import ttk
from tkinter import *
import math
import datetime
class Desk:
    def __init__(self, window):
#ventana
        ancho = 450
        alto = 300
        
     
        self.wind = window
        self.wind.geometry(str(ancho)+'x'+str(alto))
 #titulo
        self.wind.columnconfigure(0, weight=1)
        self.wind.title('EXAMEN FINAL')
        
#titulo_entrada
        frame = LabelFrame(self.wind, text = '')

        frame.grid(row = 0, column = 2, columnspan = 20, pady = 20)