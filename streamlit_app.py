import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.DataFrame(pd.read_csv("data.csv"))
st.write(df)
df['time'] = pd.to_datetime(df['time'])
st.write(df)
clist = df['id_'].unique()
st.write(clist)
id_ = st.sidebar.selectbox("Select ID:",clist)
st.header("T over time")
fig = px.line(df[df['id_'] == id_], 
    x = "time", y = "T", title = int(id_))
st.plotly_chart(fig)



