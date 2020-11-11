import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def division():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA//numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana=tk.Tk()
ventana.config(width=300,height=200)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)



etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=70,y=60)

botonTransportar=Button(ventana,text="Division A y B", command=division)
botonTransportar.place(x=0,y=90)


ventana.mainloop()

