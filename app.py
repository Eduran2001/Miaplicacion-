import streamlit as st 
import pandas as pd 

st.title("Mi Primera Aplicación")
st.sidebar.title("Parámetros")
st.sidebar.image("OIP.jpg")

modulo=st.sidebar.selectbox("Seleccione el módulo",["Módulo 1", "Módulo 2", "Módulo 3"])

if modulo== "Módulo 1":
    st.write("Estas en el módulo 1")
    ge=st.number_input("Ingrese el valor de gravedad especifica",min_value=0.1,max_value=1.0,value=0.8)
    api=(141.5/ge)-131.5
    st.write("El valor api es =",api)


elif modulo== "Módulo 2":
    st.write("Estas en el módulo 2")

    df=pd.read_excel("Resultados.xlsx")
    st.write(df)


else:
    st.write("Estas en el módulo 3")

    upload_file= st.file_uploader("Cargar archivo CSV o .xlsx",type=["csv","xlsx"])

    if upload_file is not None: 

        if upload_file.name.endswith(".csv"):
            df=pd.read_excel(upload_file)
        elif upload_file.name.endswith(".xlsx"):
            df=pd.read_excel(upload_file)
        st.write(df)

            
    else:
        st.write("Subir Archivo cvs o .xlsx")    