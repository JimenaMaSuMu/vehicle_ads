import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    .stForm {
        background-color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

st.header('Vehicles advertisement')
st.write('Selecciona el grafico deseado.')


car_data = pd.read_csv('datasets/cars_us.csv') # leer los datos
#hist_button = st.button('Construir histograma')
hist_check = st.checkbox('Construir histograma de precios')
if hist_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de los precios de coches')    
    # crear un histograma
    fig = px.histogram(car_data, x="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

#scatter_button = st.button('Construir diagrama de dispersion')
scatter_check = st.checkbox('Construir diagrama de dispersion de precios')
if scatter_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos los precios de venta de coches')    
    # crear un histograma
    fig1 = px.scatter(car_data, x="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)


hist_check_brand = st.checkbox('Construir histograma enfocando a las marcas de los coches')
if hist_check_brand:
    st.write('Creación de un histograma para el conjunto de datos de las marcas de coches')
    fig2 = px.histogram(car_data , x='model')
    st.plotly_chart(fig2, use_container_width=True)

scatter_check_brand = st.checkbox('Construir diagrama de dispersion de las marcas')
if hist_check_brand:
    st.write('Construir diagrama de dispersion enfocando a las marcas de los coches')
    fig2 = px.histogram(car_data , x='model')
    st.plotly_chart(fig2, use_container_width=True)