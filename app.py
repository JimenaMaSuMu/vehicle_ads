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
hist_check_price = st.checkbox('Construir histograma de precios')
if hist_check_price: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma para el conjunto de datos de los precios de coches\n')    
    st.write('Tenemos una mayor cantidad de carros con precios de 2k a 9k, donde el pico esta en 5k. ')  
    # crear un histograma
    fig_p = px.histogram(car_data, x="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_p, use_container_width=True)

hist_check_year = st.checkbox('Construir histograma enfocando a los años de los coches')
if hist_check_year:
    st.write('Histograma para el conjunto de datos de los años de los coches')
    st.write('Apartir del 200 empezó a incrementar la cantidad de vehiculos.\n En el 2013 tenemos un pico, donde empieza a descender la cantidad de carros por año')
    fig_y = px.histogram(car_data , x='model_year')
    st.plotly_chart(fig_y, use_container_width=True)

hist_check_condition = st.checkbox('Construir histograma enfocando a la condicion de los coches')
if hist_check_condition:
    st.write('Histograma para el conjunto de datos de la condicion de cada coche\n')
    st.write('Hay mas carros en excelentes y buenas condiciones.\n Son minimos los carros salvados y nuevos.')
    fig_c = px.histogram(car_data , x='condition')
    st.plotly_chart(fig_c, use_container_width=True)

#scatter_button = st.button('Construir diagrama de dispersion')
scatter_check = st.checkbox('Construir diagrama de dispersion de precios vs. año modelo')
if scatter_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Diagrama de dispersion para el conjunto de datos los precios con respecto al año modelo de los coches\n') 
    st.write('Todos los carros del 2000 al 2020 valen en su mayoría menos de 100k.')    
    # crear un histograma
    fig1 = px.scatter(car_data, y="price",x='model_year')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

scatter_check_p_c = st.checkbox('Construir diagrama de dispersion comparando precio y condicion de los coches')
if scatter_check_p_c:
    st.write('Diagrama de dispersion comparando el año de los coches y su condicion. \n')
    st.write('Los precio se acumulan principalmente 100k para abajo sin importar su condicion') 
    fig_p_c = px.scatter(car_data , y='price',x='condition')
    st.plotly_chart(fig_p_c, use_container_width=True)