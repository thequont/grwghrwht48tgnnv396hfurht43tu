import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.DataFrame(pd.read_csv("data.csv"))
#df['time'] = pd.to_datetime(df['time'])
clist = df['id'].unique()
st.write(clist)
country = st.sidebar.selectbox("Select ID:",clist)
st.header("T over time")
fig = px.line(df[df['id'] == id], 
    x = "time", y = "T", title = id)
st.plotly_chart(fig)

st.header("data dump")
st.write(df)

