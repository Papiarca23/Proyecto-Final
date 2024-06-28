# gestion_empleados/ui/main_window.py

import tkinter as tk
from tkinter import ttk, messagebox
from services.trabajador_service import TrabajadorService
from dto.trabajador_dto import TrabajadorDTO
from dto.datos_laborales_dto import DatosLaboralesDTO

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Empleados")
        self.trabajador_service = TrabajadorService()

        self.create_widgets()

    def create_widgets(self):
    # Formulario de nuevo trabajador
        ttk.Label(self.master, text="Nuevo Trabajador").grid(row=0, column=0, columnspan=2)
    
        ttk.Label(self.master, text="ID:").grid(row=1, column=0)
        self.id_entry = ttk.Entry(self.master)
        self.id_entry.grid(row=1, column=1)

        ttk.Label(self.master, text="Nombre:").grid(row=2, column=0)
        self.nombre_entry = ttk.Entry(self.master)
        self.nombre_entry.grid(row=2, column=1)

        ttk.Label(self.master, text="RUT:").grid(row=3, column=0)
        self.rut_entry = ttk.Entry(self.master)
        self.rut_entry.grid(row=3, column=1)

        ttk.Label(self.master, text="Género:").grid(row=4, column=0)
        self.genero_combobox = ttk.Combobox(self.master, values=["Masculino", "Femenino", "Otro"])
        self.genero_combobox.grid(row=4, column=1)

        ttk.Label(self.master, text="Dirección:").grid(row=5, column=0)
        self.direccion_entry = ttk.Entry(self.master)
        self.direccion_entry.grid(row=5, column=1)

        ttk.Label(self.master, text="Teléfono:").grid(row=6, column=0)
        self.telefono_entry = ttk.Entry(self.master)
        self.telefono_entry.grid(row=6, column=1)

        ttk.Label(self.master, text="Cargo:").grid(row=7, column=0)
        self.cargo_entry = ttk.Entry(self.master)
        self.cargo_entry.grid(row=7, column=1)

        ttk.Label(self.master, text="Departamento:").grid(row=8, column=0)
        self.departamento_entry = ttk.Entry(self.master)
        self.departamento_entry.grid(row=8, column=1)

        ttk.Button(self.master, text="Guardar", command=self.guardar_trabajador).grid(row=9, column=0, columnspan=2)

    # Lista de trabajadores
        self.tree = ttk.Treeview(self.master, columns=("ID", "Nombre", "RUT", "Género", "Cargo", "Departamento"))
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("RUT", text="RUT")
        self.tree.heading("Género", text="Género")
        self.tree.heading("Cargo", text="Cargo")
        self.tree.heading("Departamento", text="Departamento")
        self.tree.grid(row=10, column=0, columnspan=2)

        ttk.Button(self.master, text="Actualizar Lista", command=self.actualizar_lista).grid(row=11, column=0, columnspan=2)

    def guardar_trabajador(self):
        trabajador_dto = TrabajadorDTO(
            id_trabajador=self.id_entry.get() if self.id_entry.get() else None,
            nombre=self.nombre_entry.get(),
            rut=self.rut_entry.get(),
            genero=self.genero_combobox.get(),
            direccion=self.direccion_entry.get(),
            telefono=self.telefono_entry.get()
        )
        datos_laborales_dto = DatosLaboralesDTO(
            cargo=self.cargo_entry.get(),
            departamento=self.departamento_entry.get()
        )
        try:
            self.trabajador_service.crear_trabajador(trabajador_dto, datos_laborales_dto)
            messagebox.showinfo("Éxito", "Trabajador guardado correctamente")
            self.limpiar_formulario()
            self.actualizar_lista()
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def limpiar_formulario(self):
        self.nombre_entry.delete(0, tk.END)
        self.rut_entry.delete(0, tk.END)
        self.genero_combobox.set("")
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.cargo_entry.delete(0, tk.END)
        self.departamento_entry.delete(0, tk.END)

    def actualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        trabajadores = self.trabajador_service.obtener_trabajadores_filtrados()
        for trabajador in trabajadores:
            self.tree.insert("", tk.END, values=(
                trabajador.id_trabajador,
                trabajador.nombre,
                trabajador.rut,
                trabajador.genero,
                trabajador.cargo,
                trabajador.departamento
            ))
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()