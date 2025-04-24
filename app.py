import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Comparison Old VS new results")

# Charger les données
df = pd.read_csv("comparison_OG.csv")  
df['Emissions (Mt)'] = df['Emissions (Mt)'].astype(str).str.replace(',', '.').astype(float)
df['Asset'] = df['Asset'].str.strip()

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
