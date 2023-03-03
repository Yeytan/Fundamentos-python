#Convertidor de pies a metros usando Tkinter
#Sebastian Esdras Martinez Urzua
#23/02/23

from tkinter import *
from tkinter import ttk

class Conversor:

    #Constructor de la
    def __init__(self,raiz):
    
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame,textvariable=self.pies)
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame,text="Calcular", command=self.calcular).grid(column=2, row=2)

        raiz.bind("Return ", self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        
        piesFlotante = float(self.pies.get()) #Conversion de cadena flotante.
        metros = piesFlotante * 0.3048
        print("Metros: ", metros)
        self.metros.set(metros)
        




    
        


if __name__=="__main__":
    print("Este es el archivo principal. ")
    print("Nada mas se mostrara eso si es el principal. ")

    