import tkinter as tk
from PIL import Image, ImageTk

def calcular_formula(entry_largo, entry_diametro, entry_peso, entry_grosor, entry_angulo, resultado_label):
    try:
        largo = float(entry_largo.get())
        diametro = float(entry_diametro.get())
        peso = float(entry_peso.get())
        grosor = float(entry_grosor.get())
        angulo = float(entry_angulo.get())
        
        resultado = (largo * diametro + peso / grosor) / (angulo ** 2)
        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Por favor, introduce números válidos.")

def crear_interfaz(formula):
    ventana = tk.Tk()
    ventana.title("Calculadora de Fórmula")
    ventana.geometry("500x600+350+20")
    ventana.minsize(480, 500)
    ventana.title('T.M.I')

    # Configurando widgets
    tk.Label(ventana, text="Largo:", foreground="black").pack(anchor="center")
    entry_largo = tk.Entry(ventana)
    entry_largo.pack(anchor="center")
    entry_largo.configure(font=('sans serif', 12), foreground="black")

    tk.Label(ventana, text="Diámetro:", foreground="black").pack(anchor="center")
    entry_diametro = tk.Entry(ventana)
    entry_diametro.pack(anchor="center")
    entry_diametro.configure(font=('sans serif', 12), foreground="black")

    tk.Label(ventana, text="Peso:", foreground="black").pack(anchor="center")
    entry_peso = tk.Entry(ventana)
    entry_peso.pack(anchor="center")
    entry_peso.configure(font=('sans serif', 12), foreground="black")

    tk.Label(ventana, text="Grosor:", foreground="black").pack(anchor="center")
    entry_grosor = tk.Entry(ventana)
    entry_grosor.pack(anchor="center")
    entry_grosor.configure(font=('sans serif', 12), foreground="black")

    tk.Label(ventana, text="Ángulo:", foreground="black").pack(anchor="center")
    entry_angulo = tk.Entry(ventana)
    entry_angulo.pack(anchor="center")
    entry_angulo.configure(font=('sans serif', 12), foreground="black")

    resultado_label = tk.Label(ventana, text="", font=('sans serif', 12), foreground="black")
    resultado_label.pack(anchor="center")

    tk.Button(ventana, text="Calcular", font=('sans serif', 12), command=lambda: calcular_formula(entry_largo, entry_diametro, entry_peso, entry_grosor, entry_angulo, resultado_label)).pack(anchor="center")

    tk.Label(ventana, text=f"Fórmula: {formula}", font=('sans serif', 12), foreground="black").pack(anchor="center")
    
    ruta_imagen = r"C:\Users\AnalistaIT\Downloads\Project medidas\img\Randy.png"
    image = Image.open(ruta_imagen)
    photo = ImageTk.PhotoImage(image)
    imagen_label = tk.Label(ventana, image=photo)
    imagen_label.image = photo
    imagen_label.pack(anchor="center")

    ventana.mainloop()
