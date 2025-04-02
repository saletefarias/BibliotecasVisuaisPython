import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class PartidoPolitico:
    def __init__(self, nome, anos, popularidade):
        self.nome = nome
        self.anos = anos
        self.popularidade = popularidade

    def gerar_grafico(self):
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=self.anos, y=self.popularidade, marker="o", color="red")
        plt.title(f"Popularidade do {self.nome} ao Longo do Tempo")
        plt.xlabel("Ano")
        plt.ylabel("Popularidade (%)")
        plt.show()

# Exemplo
anos = np.arange(2000, 2025)
popularidade = np.random.randint(20, 60, size=len(anos))
partido = PartidoPolitico("Partido X", anos, popularidade)
partido.gerar_grafico()
