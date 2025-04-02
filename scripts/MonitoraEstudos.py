import matplotlib.pyplot as plt

class Estudo:
    def __init__(self, nome, horas_por_dia):
        self.nome = nome
        self.horas_por_dia = horas_por_dia  # Lista com horas de estudo por dia da semana
        self.dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

    def gerar_grafico(self):
        plt.figure(figsize=(8, 5))
        plt.bar(self.dias, self.horas_por_dia, color="green")
        plt.xlabel("Dias da Semana")
        plt.ylabel("Horas de Estudo")
        plt.title(f"Hábitos de Estudo - {self.nome}")
        plt.ylim(0, max(self.horas_por_dia) + 1)
        plt.show()

# Exemplo com um aluno fictício
aluno1 = Estudo("Salete", [2, 3, 1, 4, 2, 5, 1])
aluno1.gerar_grafico()
