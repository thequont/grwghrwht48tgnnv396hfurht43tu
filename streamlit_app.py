

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
df = pd.DataFrame(pd.read_csv("data.csv"))
#df['time'] = pd.to_datetime(df['time'])
clist = df['id_'].unique()
id_ = st.sidebar.selectbox("Select ID:",clist)
st.header("T over time")
fig = px.line(df[df['id_'] == id_], 
    x = "time", y = "T", z="RSSI", title = str(id_))
st.plotly_chart(fig)

st.header("RSSI over time")
figR = px.line(df[df['id_'] == id_], 
    x = "time", y = "RSSI", title = str(id_))
st.plotly_chart(figR)

st.header("Raw Data")
st.write(df)


