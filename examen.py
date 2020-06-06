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
        Button(frame, text = 'FUNCION 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'FUNCION 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
         #resultados
        self.message = Label(text = '', fg = 'Black')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    #binariotest
    def funcion1(self):
        dia=int(self.pp3.get())
        mes=int(self.pes4.get())
        anio=int(self.pap5.get())
        bindia=format(dia, '0b' )
        binmes=format(mes, '0b')
        binanio=format(anio, '0b')

        self.message['text'] = 'naciste en la fecha: {}/{}/{} tu fecha de nacimiento en binario es :{}/{}/{}'.format(dia,mes,anio,bindia,binmes,binanio)
      #vidaprueba2
    def funcion2(self):
            
        dia=int(self.pp3.get())
        mes=int(self.pes4.get())
        anio=int(self.pap5.get())
        fecha_denacimiento = datetime.datetime(anio, mes, dia)
        fecha_de_hoy = datetime.datetime.now()
        diferencia = fecha_de_hoy - fecha_de_nacimiento
        dias_vividos = diferencia.days
        self.message['text'] = 'Naciste en: {}/{}/{}: en total has vivido{} dias'.format(dia,mes,anio,dias_vividos)   
        