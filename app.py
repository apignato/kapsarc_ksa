import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Émissions de méthane - Vue interactive")

# Charger les données
df = pd.read_csv("comparison_OG.csv")  


assets = df["Asset"].unique()
selected_asset = st.selectbox("Choose an asset :", assets)

filtered_df = df[df["Asset"] == selected_asset]


fig = px.bar(
    filtered_df,
    x="Year",
    y="Emissions (Mt)",
    color="Method",
    barmode="group",
    title=f"O&G emissions for {selected_asset}"
)


st.plotly_chart(fig)
