# PRACTICA 7. Interfaz Gráfica de Usuario (GUI)
# Basado en ejercicio de clase

# Importando Tkinter
from tkinter import *

# Importando modulo
import tkinter.messagebox

# ArrayList
videogameList = [['Gear of War', 'Guerro', 'Xbox', '2121'], ['Fifa 20', 'Deportes', 'PlayStation, Xbox', '2020'],
                 ['Mario Kart 8', 'Carreras', 'Nintendo', '2018']]

# Funcion para saber el registro selecionado
def selecionVideojuego():
    print("Posicion {0}".format(select.curselection())) #imprimier en consola la posicion
    return int(select.curselection()[0])

# Funcion para agregar nuevo registro
def agregarVideojuego():
    videogameList.append(
        [juego.get(), genero.get(), plataforma.get(), anio.get()])
    tabla()  # Actualizamos la tabla

# Funcion para eliminar nuevo registro
def eliminarVideojuego():
    del videogameList[selecionVideojuego()]  # Eliminamos videojuego de la lista
    tabla()  # Actualizamos la tabla

# Funcion de confguracion de la ventana
def makeWIndow():
    # Variables globales
    global juego, genero, plataforma, anio, select

    # Definimos la ventana
    win = Tk()

    # Definimos titulo de la ventana
    win.title("Videojuegos")

    # Definimos tamaño de la ventana
    win.geometry('350x450')

    # Configuracion de icono
    icon = PhotoImage(file="icon.png")
    win.iconphoto(False, icon)

    # Dibujando la estrella
    canvas_width = 200
    canvas_height = 200
    python_green = "#476042"

    w = Canvas(win, width=canvas_width,  height=canvas_height)  # canvas
    w.pack()

    points = [100, 140, 110, 110, 140, 100, 110,
              90, 100, 60, 90, 90, 60, 100, 90, 110]
    w.create_polygon(points, outline=python_green, fill='yellow', width=3)

    # Barra de navegacion en la ventana
    menubar = Menu(win)
    win.config(menu=menubar)

    filemenu = Menu(menubar)
    menubar.add_cascade(label='Archivo', menu=filemenu)

    # Create entries in the "File" menu
    # simulated command functions that we want to invoke from our menus
    def doPrint(): tkinter.messagebox.showinfo('Mensaje',"Practica 7 - Luis")
    filemenu.add_command(label='Informacion', command=doPrint)
    filemenu.add_separator()
    filemenu.add_command(label='Salir', command=win.destroy)

    frame1 = Frame(win)
    frame1.pack()

    # Labels
    Label(frame1, text="Nombre").grid(row=0, column=0, sticky=W)
    juego = StringVar()
    nombreVideojuego = Entry(frame1, textvariable=juego)
    nombreVideojuego.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Genero").grid(row=1, column=0, sticky=W)
    genero = StringVar()
    generoVideojuego = Entry(frame1, textvariable=genero)
    generoVideojuego.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Plataforma").grid(row=2, column=0, sticky=W)
    plataforma = StringVar()
    plataformaVideojuego = Entry(frame1, textvariable=plataforma)
    plataformaVideojuego.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Año").grid(row=3, column=0, sticky=W)
    anio = StringVar()
    anioVideojuego = Entry(frame1, textvariable=anio)
    anioVideojuego.grid(row=3, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2, text="Agregar", command=agregarVideojuego)
    b2 = Button(frame2, text="Borrar", command=eliminarVideojuego)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win

# Funcion para cargar los datos de la tabla
def tabla():
    videogameList.sort(key=lambda record: record[1])
    select.delete(0, END)
    for nombreVideojuego, generoVideojuego, plataformaVideojuego, anioVideojuego in videogameList:
        select.insert(END, "Videojuego: {0} | Genero: {1} | Plataforma {2} | Año: {3}".format(
            nombreVideojuego, generoVideojuego, plataformaVideojuego, anioVideojuego))






window = makeWIndow()  # Creamos una ventana
tabla()  # Cargamos la tabla
window.mainloop()  # Ejecutar los eventos
