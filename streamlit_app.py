import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.DataFrame(pd.read_csv("data.csv"))
df['time'] = pd.to_datetime(df['time'])
clist = df['id_'].unique()
id_ = st.sidebar.selectbox("Select ID:",clist)
st.header("T over time")
fig = px.line(df[df['id_'] == int(id_)], 
    x = "time", y = "T", title = id_)
st.plotly_chart(fig)



