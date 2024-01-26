from tkinter import *
import pygame as pg
import pygame



pg.init()


musicList =['sonido/coniferous-forest-142569.mp3']
pygame.mixer.music.load(musicList[0])
pygame.mixer.music.play()
track = 0

#funcion para abrir un archivo
def abrir_archivo():
    archivo=open("Play_burbuja.py","r")
    archivo.close()
    ventana.destroy()
  
#funcion para salir
def salir():
    ventana.destroy()
  
#creacion de la ventana
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Burbuja Explosiva")
ventana.configure(background="light blue")

#Agregar la imagen de fondo
imagen_fondo = PhotoImage(file="images/fondo.png")
fondo = Label(ventana, image=imagen_fondo).place(x=0, y=0, relwidth=1, relheight=1)
  
#creacion de etiqueta
label = Label(ventana, text="Burbuja Explosiva", font=("Verdana", 20), bg="light blue")
label.place(x=285, y=50)
  
#boton para abrir archivo
boton_abrir_archivo = Button(ventana, text="Jugar", command=abrir_archivo, width=15, height=3, font=('Verdana', 13))
boton_abrir_archivo.place(x=320, y=200)
  
#boton para salir
boton_salir = Button(ventana, text="Salir", command=salir, width=15, height=3, font=('Verdana', 13))
boton_salir.place(x=320, y=400)
  
#ejecutar la ventana
ventana.mainloop()