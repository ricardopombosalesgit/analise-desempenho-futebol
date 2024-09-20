import streamlit as st
import pandas as pd
import numpy as np

# Título e autor
'# Análise de Desempenho no Futebol'
'Feito por Ricardo Pombo Sales'

# Dados fictícios de desempenho
dados = {
    'Minuto': np.arange(1, 91),
    'Distância Percorrida (m)': np.random.uniform(50, 150, 90),
    'Velocidade Média (km/h)': np.random.uniform(5, 20, 90),
    'Batimentos Cardíacos (bpm)': np.random.uniform(70, 190, 90)
}
df = pd.DataFrame(dados)

# Exibindo o DataFrame
'## Estatísticas do Jogo'
df

# Gráfico de Distância Percorrida
'## Distância Percorrida por Minuto'
st.bar_chart(df[['Minuto', 'Distância Percorrida (m)']].set_index('Minuto'))

# Gráfico de Velocidade Média
'## Velocidade Média por Minuto'
st.line_chart(df[['Minuto', 'Velocidade Média (km/h)']].set_index('Minuto'))

# Gráfico de Batimentos Cardíacos
'## Batimentos Cardíacos por Minuto'
st.area_chart(df[['Minuto', 'Batimentos Cardíacos (bpm)']].set_index('Minuto'))