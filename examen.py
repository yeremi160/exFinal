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
  #nombre
        Label(frame, text = 'NOMBRE: ').grid(row = 1, column = 0)
       
        self.p1 = Entry(frame)
        self.p1.focus()
        self.p1.grid(row = 1, columnspan = 6)
        #apellido
        Label(frame, text = 'APELLIDO: ').grid(row = 2, column = 0)
        self.op2 = Entry(frame)
        self.op2.grid(row = 2, columnspan = 6)
         #dia
        Label(frame, text = 'DIA: ').grid(row = 3, column = 0)
        self.pp3 = Entry(frame)
        self.pp3.grid(row = 3, columnspan = 6)
        #mes
        Label(frame, text = 'MES: ').grid(row = 4, column = 0)
        self.pes4 = Entry(frame)
        self.pes4.grid(row = 4, columnspan = 6)
        #año
        Label(frame, text = 'AÑO: ').grid(row = 5, column = 0)
        self.pap5 = Entry(frame)
        self.pap5.grid(row = 5, columnspan = 6)
         #botones
        Button(frame, text = 'FUNCION 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'FUNCION 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'FUNCION 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)