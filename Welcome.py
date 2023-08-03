import streamlit as st
import pandas as pd
import os 

filename = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename.append(i)

 

 

df =  pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)
st.write(filename[0])
st.multiselect('select location' , filename, filename[0])
