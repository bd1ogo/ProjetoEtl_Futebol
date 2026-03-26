import streamlit as st
import pandas as pd
import json

st.title("Dashboard - Ranking de Futebol")

with open("data/ranking.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

df = pd.DataFrame(dados)
df = df.sort_values(
    by=["saldo_gols", "gols_feitos"],
    ascending=[False, False]
).reset_index(drop=True)
df["posição"] = df.index + 1
df = df[["posição", "time", "saldo_gols", "gols_feitos", "gols_sofridos"]]
st.dataframe(df)

melhor_time = df.iloc[0]
melhor_ataque = df.loc[df["gols_feitos"].idxmax()]
melhor_defesa = df.loc[df["gols_sofridos"].idxmin()]

st.title("Ranking dos Melhores")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        label="🏆 Melhor Time",
        value=melhor_time["time"],
        delta=f"{melhor_time['saldo_gols']} goal difference"
    )
with col2:
    st.metric(
        label="⚽ Melhor Ataque",
        value=melhor_ataque["time"],
        delta=f"{melhor_ataque['gols_feitos']} goals"
    )
with col3:
    st.metric(
        label="🧱 Melhor Defesa",
        value=melhor_defesa["time"],
        delta=f"-{melhor_defesa['gols_sofridos']} conceded"
    )

st.subheader("Gols marcados por Time")
st.bar_chart(df.set_index("time")["gols_feitos"])

st.subheader("Ataque x Defesa")
st.scatter_chart(
    df,
    x="gols_sofridos",
    y="gols_feitos"
)
