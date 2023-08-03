import streamlit as st
import pandas as pd
import os 
from bokeh.plotting import figure
import numpy as np
filename = []
for i in os.listdir():
  if i.endswith('.csv'):
    df1 = pd.read_csv(i)
    filename.append(i)

st.write(filename) 
df =  pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
el_list = df.columns.tolist()[27:80]
#x_axis = st.selectbox('select element', el_list)
colours = ['blue', 'green', 'purple', 'pink', 'yellow', 'grey', 'black']
st.multiselect('select location' , filename, filename[0])

x = st.selectbox('x-axis', df1.columns.tolist()[27:80])
y = st.selectbox('y-axis', df1.columns.tolist()[27:80], index =9)
p = figure(
    title='Plot',
    x_axis_label= x + '(wt%)',
    y_axis_label= y + '(wt%)')
#mean1 = np.mean(final_data[x]/10000)
#mean2 = np.mean(final_data[y]/10000)
                

p.circle(filename[x]/10000, filename[y]/10000, legend_label=filename, color= colours,  line_width=2)
#p.line(mean1, mean2, line_width=2)
st.bokeh_chart(p, use_container_width=True)
st.write(mean1, mean2)
