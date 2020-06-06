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