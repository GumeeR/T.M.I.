import tkinter as tk
from Gui import crear_interfaz

# Fórmula que será pasada a la interfaz
formula = "(Largo * Diámetro + Peso / Grosor) / Ángulo^2"

if __name__ == "__main__":
    ventana = crear_interfaz(formula)
    ventana.mainloop()
