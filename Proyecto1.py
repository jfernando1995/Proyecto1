import streamlit as st 
import pandas as pd
import altair as alt
import numpy as np
st.title("Mi primer aplicativo")
st.sidebar.title("Parametros")
opciones_inicio=st.sidebar.radio("seleccione una opción",["Inicio","Datos","Calculos"])
if opciones_inicio == "Inicio":
	st.write("Bienvenido a Inicio")
	#Barra deslizadora
	barra_deslizadora=st.slider("Seleccione un valor",1,100,30)
	cálculo=barra_deslizadora*12
	st.write("El resultado es: ", cálculo)
	ingreso_número=st.number_input("Ingrese un valor",min_value=0,max_value=1000,value=100)
	cálculo2=barra_deslizadora*ingreso_número
	st.write("El resultado es: ", cálculo2)
if opciones_inicio == "Datos":
	selección=st.selectbox("Seleccione una opción",["opción 1","opción 2","opción 3"])
	st.write("Usted ha selecionado: ",selección)
	multiselect=st.multiselect("Seleccione una opción",["opción a","opción b", "opción c", "opción b"])
	st.write("El resultado es", multiselect)
	agree = st.checkbox('I agree')
	if agree:
		st.write('Great!')

if opciones_inicio== "Calculos":
	archivo_subida=st.file_uploader("Suba un archivo en formato Excel",type=[".xlsx","XLSX","xls","XLS"],key=None)
	if archivo_subida is None: 
		st.info("Aún no ha cargado un archivo Excel")
	if archivo_subida is not None:
		df=pd.read_excel(archivo_subida)
		df["Nueva"]=df["NÚMEROS"]*2
		st.write(df)
		df2=pd.read_excel("Data_Excel\DATA.xlsx.")
		gráfico=alt.Chart(df2).mark_line().encode(
			x=df2["LETRAS"],y=df2["NÚMEROS"]).interactive()
		st.altair_chart(gráfico)


		#CUANDO LOS ENCABEZADOS SON UNIDOS SE USA (.) Y [] PARA ESPECIFICAR UNA COMUNAS QUE TIENE CARACTERES 






