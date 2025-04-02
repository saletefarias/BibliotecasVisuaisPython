import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class ConflitoHistorico:
    def __init__(self, nome, seculos, ocorrencias):
        self.nome = nome
        self.seculos = seculos
        self.ocorrencias = ocorrencias

    def gerar_grafico(self):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.seculos, y=self.ocorrencias, color="darkblue", s=100)
        plt.title(f"Evolução dos Conflitos - {self.nome}")
        plt.xlabel("Século")
        plt.ylabel("Número de Conflitos")
        plt.grid(True)
        plt.show()

# Exemplo
seculos = np.arange(11, 21)
conflitos = np.random.randint(5, 50, size=len(seculos))
conflito = ConflitoHistorico("Conflitos Europeus", seculos, conflitos)
conflito.gerar_grafico()
