import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
st.write('Hello world')
df =  pd.read_csv('Bastar Craton.csv')
st.dataframe(df)
