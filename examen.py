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
        fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
        fecha_de_hoy = datetime.datetime.now()
        diferencia = fecha_de_hoy - fecha_de_nacimiento
        dias_vividos = diferencia.days
        self.message['text'] = 'Naciste en: {}/{}/{}: en total has vivido{} dias'.format(dia,mes,anio,dias_vividos)   
         #par_impar 
    def funcion3(self):
        nom=str(self.p1.get())
        apel=str(self.op2.get())
        nr_nombre=int(len(nom))
        nr_apellido=int(len(apel))
        if nr_nombre%2==0 and nr_apellido %2==0 :
                self.message['text'] = '{} {} tu nombre es par y tu apellido es par'.format(nom,apel)
        elif nr_nombre%2==0 and nr_apellido %2==1:
            self.message['text'] = '{} {} tu nombre es par y tu apellido es impar'.format(nom,apel)
        elif nr_nombre%2==1 and nr_apellido %2==0:
            self.message['text'] = '{} {} tu nombre es impar y tu apellido es par'.format(nom,apel)
        else:
            self.message['text'] = '{} {} tu nombre es impar y tu apellido es impar'.format(nom,apel)   

        #voca_cons
    def funcion4(self):
        nr=str(self.p1.get())
        apd=str(self.op2.get())
        cuenta = 0
        for carac in nr:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apd:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cud=len(nr)
        cudd=len(apd)
        consonante=cud+cudd-cuenta

        self.message['text'] = 'todo tu nombre tiene {} vocales y {} consonantes'.format(cuenta,consonante)
        #reves
    def funcion5(self):
        ns=str(self.p1.get())
        ad=str(self.op2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in ns:
            cadena_invertida = letra + cadena_invertida
        for letra1 in ad:
            cadena_invertida1 = letra1 + cadena_invertida1
        self.message['text'] = '{} {} tu nombre al reves {} {}'.format(ns,ad,cadena_invertida,cadena_invertida1)
  