import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina= pd.read_csv('gasolina.csv')
# gasolina.head()

sns.set_theme(style="darkgrid")

fig, grafico = plt.subplots(facecolor=(.18, .31, .31))
grafico= sns.lineplot(data= gasolina, x='dia', y='venda', color="green")
grafico.set_facecolor('#eafff5')
grafico.set_title('Preço Médio da gasolina em Julho/2021 - SP', color='0.7')
grafico.set_xlabel('Primeiros 10 dias de Julho', color='c')
grafico.set_xlim(1, 10)
grafico.set_ylabel('Variação Preços', color='peachpuff')
grafico.set_ylim(4.90, 5.30)
grafico.tick_params(labelcolor='tab:orange')
plt.savefig('gasolina.png', format='png')