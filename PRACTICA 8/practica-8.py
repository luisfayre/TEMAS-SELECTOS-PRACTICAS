# PRACTICA 8 - EJEMPLO DE CLASE CON GUI

import tkinter
import random

class Circulo():

    # Constructor   - Melina
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    # Método getradio( )  - Luis
    def getRadio(self):
        return self.radio

    # Método getcolor( )
    def getColor(self):
        return self.color

class MyGUI:
    def __init__(self):

        # VARIABLES GLOBALES
        global radioFigura, var_color

        # Create the main window widget
        self.main_window = tkinter.Tk()

        # CAPTURAR RADIO
        tkinter.Label(self.main_window, text='Radio: ').pack()
        radioFigura = tkinter.IntVar()
        tkinter.Entry(self.main_window, textvariable=radioFigura).pack()

        # BOTON DIBUJAR
        tkinter.Button(self.main_window, text='Dibujar',
                       command=self.dibujar).pack()
        tkinter.Button(self.main_window, text='Eliminar',
                       command=self.borrar).pack()

        # Crear canvas   - Alonso
        self.canvas = tkinter.Canvas(self.main_window, width=250, height=250)

        # Crear canvas   - Alonso
        self.canvas.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Función dibujar
    def dibujar(self):
        self.figura1 = Circulo(radioFigura.get(), 'null')
        radio = int(self.figura1.getRadio()) * 2  # Obtener radio

        # Colores
        cantidadColores = 8
        # Colores random
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

                 # For dependiendo la cantidad de colores
                 for i in range(cantidadColores)]
        for i in range(cantidadColores):
            randomPosx1 = random.randint(0, 250)  # x inicial
            randomPosy1 = random.randint(0, 250)  # y inicial
            randomPosx2 = randomPosx1 + radio  # x inicial
            randomPosy2 = randomPosy1 + radio    # inicial
            self.canvas.create_oval(
                randomPosx1, randomPosy1, randomPosx2, randomPosy2, fill=color[i])

    # Función borrar
    def borrar(self):
        self.canvas.delete("all")


# Create an instance of the MyGUI class
my_gui = MyGUI()
