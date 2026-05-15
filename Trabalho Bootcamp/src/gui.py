import tkinter as tk
from tkinter import messagebox
from logic import calcular_imc, get_weather, recomendacao_agua


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Saude v1.0")
        self.root.geometry("300x300")

        tk.Label(root, text="Peso (kg):").pack(pady=5)
        self.ent_peso = tk.Entry(root)
        self.ent_peso.pack()

        tk.Label(root, text="Altura (m - ex: 1.75):").pack(pady=5)
        self.ent_altura = tk.Entry(root)
        self.ent_altura.pack()

        tk.Button(root, text="Calcular", command=self.processar).pack(pady=10)

        # Novo botao
        tk.Button(root, text="Ver clima e hidratacao", command=self.ver_clima).pack(pady=5)

    def processar(self):
        try:
            p = float(self.ent_peso.get().replace(',', '.'))
            a = float(self.ent_altura.get().replace(',', '.'))
            valor, cat = calcular_imc(p, a)

            messagebox.showinfo(
                "Resultado",
                f"Seu IMC: {valor}\nClassificacao: {cat}"
            )
        except:
            messagebox.showerror("Erro", "Insira valores validos!")

    def ver_clima(self):
        temp, desc = get_weather()

        if temp is None:
            messagebox.showerror("Erro", "Nao foi possivel obter o clima.")
            return

        recomendacao = recomendacao_agua(temp)

        messagebox.showinfo(
            "Clima e Hidratacao",
            f"Temperatura: {temp} C\n"
            f"Condicao: {desc}\n\n"
            f"{recomendacao}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
