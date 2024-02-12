import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "DORADITA")

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con botón")

# Función para mostrar el mensaje
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "DORADITA")

# Crear el botón
boton = tk.Button(root, text="Lo siento", command=mostrar_mensaje)
boton.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()