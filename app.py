import streamlit as st
import pandas as pd

st.title("Cyber Threat Detection")

file = st.file_uploader("cyberfeddefender_dataset (1).csv.xls")

if file:
    df = pd.read_csv(file)
    st.write("Data Preview:")
    st.write(df.head())