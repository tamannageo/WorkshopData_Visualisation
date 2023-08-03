import streamlit as st
import pandas as pd
import os 
from bokeh.plotting import figure
import numpy as np
filename = []
for i in os.listdir():
  if i.endswith('.csv'):
    filename.append(i)

 
df =  pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
#el_list = df.columns.tolist()[27:80]
#x_axis = st.selectbox('select element', el_list)
#st.multiselect('select location' , filename, filename[0])

x = st.selectbox('x-axis', df.columns.tolist()[27:80])
y = st.selectbox('y-axis', df.columns.tolist()[27:80], index =9)
p = figure(
    title='Scatter Plot',
    x_axis_label= x + '(wt%)',
    y_axis_label= y + '(wt%)')

p.circle(df[x]/10000, df[y]/10000, legend_label='Trend', line_width=2)
p.line(np.mean(df[x]/10000), np.mean(df[y]/10000))
st.bokeh_chart(p, use_container_width=True)
