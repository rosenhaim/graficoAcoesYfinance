import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Definir o intervalo de datas para obter os dados
start_date = '2021-01-01'
end_date = '2023-05-29'

# Obter os dados das ações da Petrobras (código PETR4) usando a biblioteca yfinance
df = yf.download('PETR4.SA', start=start_date, end=end_date)

# Plotar o gráfico das ações
plt.plot(df.index, df['Close'])
plt.title('Preço de fechamento das ações da Petrobras')
plt.xlabel('Data')
plt.ylabel('Preço de fechamento')
plt.show()
