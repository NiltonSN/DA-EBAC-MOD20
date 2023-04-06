import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gasolina = pd.read_csv('gasolina.csv')
sns.lineplot(data=gasolina, x='dia', y='venda', palette='pastel')
plt.savefig('gasolina.png', format='png')