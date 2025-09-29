import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv('vehicles.csv')

car_data = load_data()

st.header('Análise de dados de anúncios de vendas de carros')

# Inicializa flags na sessão
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False
if 'show_scatter' not in st.session_state:
    st.session_state.show_scatter = False

st.subheader('Conjunto de dados de anúncios de vendas de carros — HISTOGRAMA')
if st.button('Criar gráfico de histograma', key='btn_hist'):
    st.session_state.show_hist = True  # mantém aberto nas próximas execuções

if st.session_state.show_hist:
    st.write('Criando um histograma para o conjunto de dados…')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Conjunto de dados de anúncios de vendas de carros — DISPERSÃO')
if st.button('Criar gráfico de dispersão', key='btn_disp'):
    st.session_state.show_scatter = True  # mantém aberto nas próximas execuções

if st.session_state.show_scatter:
    st.write('Criando dispersão para o conjunto de dados…')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

# (Opcional) botão para limpar tudo
if st.button('Limpar gráficos', key='btn_clear'):
    st.session_state.show_hist = False
    st.session_state.show_scatter = False
