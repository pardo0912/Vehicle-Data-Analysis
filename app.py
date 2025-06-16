import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV 
car_data = pd.read_csv(r'C:\Users\vanep\OneDrive\Escritorio\Bootcamp\SPRINT-7\vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos usados en EE.UU.')

# Casilla de verificación para histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Histograma de los valores del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión entre precio y odómetro')

if build_scatter:
    st.write('Gráfico de dispersión: Precio vs Odómetro')
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Relación entre Odómetro y Precio')
    st.plotly_chart(fig2, use_container_width=True)
