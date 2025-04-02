#Crie um Gráfico de barras mostrando a frequência das palavras mais comuns em um texto
class Texto:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def calcular_frequencia(self):
        palavras = self.conteudo.lower().split()
        frequencia = {}
        for palavra in palavras:
            frequencia[palavra] = frequencia.get(palavra, 0) + 1
        return frequencia

    def gerar_grafico(self):
        freq = self.calcular_frequencia()
        df = pd.DataFrame(freq.items(), columns=["Palavra", "Frequência"]).sort_values(by="Frequência", ascending=False)[:10]

        plt.figure(figsize=(8, 5))
        sns.barplot(x="Frequência", y="Palavra", data=df, hue="Palavra", palette="Blues_r", legend=False)
        plt.title(f"Frequência das Palavras - {self.titulo}")
        plt.show()

# Exemplo
texto_exemplo = Texto("Discurso Político", "democracia poder justiça sociedade governo liberdade estado direito direito")
texto_exemplo.gerar_grafico()
