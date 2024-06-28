# verify_tkinter.py

import sys

try:
    import tkinter as tk
    print(f"tkinter está instalado. Versión: {tk.TkVersion}")
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    print("Se ha creado una instancia de Tk exitosamente.")
except ImportError:
    print("tkinter no está instalado en este sistema.")
    print(f"Estás usando Python {sys.version}")
    print("Por favor, instala tkinter para tu versión de Python.")