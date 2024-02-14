import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Aplicativo Projeto Sprint 5')

car_data = pd.read_csv(
    # lendo os dados
    'C:\\Users\Alexandre\\Desktop\\New\\vehicles_env\\Projeto-Sprint-5\\vehicles.csv')

hist_button = st.button('Criar histograma')  # criar um botão
scatter_button = st.button('Criar gráfico de dispersão')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer", labels={
                       'odometer': 'Distância Percorrida'})

    # Colocando título no histograma
    fig.update_layout(title="Histograma de Distância Percorrida")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criando um gráfico de distribuição

if scatter_button:  # Se o botão do gráfico de dispersão for clicado
    # Escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # Criar o gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price", labels={
                     'odometer': 'Distância Percorrida', 'price': 'Preço'})
    fig.update_layout(title="Distribuição Preço x Distância Percorrida")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
