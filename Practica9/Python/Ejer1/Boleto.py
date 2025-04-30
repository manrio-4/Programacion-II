import tkinter as tk
from tkinter import ttk, messagebox

class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def calcular_precio(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    def calcular_precio(self):
        self.precio = 50.0 if self.dias_anticipacion >= 10 else 60.0
        return self.precio

class Galeria(Platea):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero, dias_anticipacion)

    def calcular_precio(self):
        self.precio = 25.0 if self.dias_anticipacion >= 10 else 30.0
        return self.precio


class Galeria(Platea):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero, dias_anticipacion)

    def calcular_precio(self):
        self.precio = 25.0 if self.dias_anticipacion >= 10 else 30.0
        return self.precio

class TeatroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal - Boletos")

        #num
        ttk.Label(root, text="Número de Boleto:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_numero = ttk.Entry(root)
        self.entry_numero.grid(row=0, column=1)

        #tipo
        ttk.Label(root, text="Tipo de Boleto:").grid(row=1, column=0, padx=5, pady=5)
        self.tipo_combo = ttk.Combobox(root, values=["Palco", "Platea", "Galeria"], state="readonly")
        self.tipo_combo.grid(row=1, column=1)

        #anticip
        ttk.Label(root, text="Días de Anticipación:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_dias = ttk.Entry(root)
        self.entry_dias.grid(row=2, column=1)

        #botone
        ttk.Button(root, text="Mostrar Boleto", command=self.mostrar_boleto).grid(row=3, column=0, pady=10)
        ttk.Button(root, text="Salir", command=root.quit).grid(row=3, column=1, pady=10)

    def mostrar_boleto(self):
        tipo = self.tipo_combo.get()

        try:
            numero = int(self.entry_numero.get())
        except ValueError:
            messagebox.showerror("Error", "Número de boleto inválido.")
            return

        boleto = None

        if tipo == "Palco":
            boleto = Palco(numero)

        elif tipo == "Platea":
            try:
                dias = int(self.entry_dias.get())
                boleto = Platea(numero, dias)
                boleto.calcular_precio()
            except ValueError:
                messagebox.showerror("Error", "Días de anticipación inválido.")
                return

        elif tipo == "Galeria":
            try:
                dias = int(self.entry_dias.get())
                boleto = Galeria(numero, dias)
                boleto.calcular_precio()
            except ValueError:
                messagebox.showerror("Error", "Días de anticipación inválido.")
                return

        else:
            messagebox.showwarning("Advertencia", "Seleccione un tipo de boleto.")
            return

        messagebox.showinfo("Boleto Generado", str(boleto))


# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroGUI(root)
    root.mainloop()