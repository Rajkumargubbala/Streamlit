import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt


data_path="data/"

df=pd.read_csv(data_path+"iris.csv")

st.title("IRIS DASHBOARD")

st.dataframe(df)

col_name=st.selectbox("select your column",
                     ("SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"))

fig,ax=plt.subplots(2)

ax[0].hist(df[col_name])
ax[1].boxplot(df[col_name])
st.pyplot(fig)

