import tkinter as tk
from tkinter import messagebox
from logic import calcular_imc

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Saúde v1.0")
        self.root.geometry("300x250")

        tk.Label(root, text="Peso (kg):").pack(pady=5)
        self.ent_peso = tk.Entry(root)
        self.ent_peso.pack()

        tk.Label(root, text="Altura (m - ex: 1.75):").pack(pady=5)
        self.ent_altura = tk.Entry(root)
        self.ent_altura.pack()

        tk.Button(root, text="Calcular", command=self.processar).pack(pady=20)

    def processar(self):
        try:
            p = float(self.ent_peso.get().replace(',', '.'))
            a = float(self.ent_altura.get().replace(',', '.'))
            valor, cat = calcular_imc(p, a)
            messagebox.showinfo("Resultado", f"Seu IMC: {valor}\nClassificação: {cat}")
        except Exception as e:
            messagebox.showerror("Erro", "Insira valores válidos!")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
