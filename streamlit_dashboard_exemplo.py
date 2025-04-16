
import streamlit as st
import pandas as pd
import plotly.express as px

# Dados fictícios
data = {
    'Ano': [2023, 2023, 2023, 2024, 2024, 2024] * 3,
    'Região': ['Sul', 'Sudeste', 'Nordeste'] * 6,
    'Produto': ['A', 'B', 'C'] * 6,
    'Categoria': ['Eletrônicos', 'Roupas', 'Alimentos'] * 6,
    'Vendas': [10000, 15000, 12000, 13000, 17000, 9000,
               11000, 16000, 10000, 14000, 18000, 9500,
               10500, 15800, 10300, 13500, 17300, 9100]
}
df = pd.DataFrame(data)

st.title("📊 Dashboard de Vendas - Exemplo")

# Filtros
st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", options=df["Ano"].unique(), default=df["Ano"].unique())
regioes = st.sidebar.multiselect("Região", options=df["Região"].unique(), default=df["Região"].unique())
categorias = st.sidebar.multiselect("Categoria", options=df["Categoria"].unique(), default=df["Categoria"].unique())

# Filtrar os dados
df_filtrado = df[
    (df["Ano"].isin(anos)) &
    (df["Região"].isin(regioes)) &
    (df["Categoria"].isin(categorias))
]

st.subheader("Vendas por Produto")
fig_produto = px.bar(df_filtrado, x="Produto", y="Vendas", color="Região", barmode="group")
st.plotly_chart(fig_produto, use_container_width=True)

st.subheader("Evolução das Vendas por Ano")
fig_evolucao = px.line(df_filtrado.groupby(["Ano"], as_index=False).sum(), x="Ano", y="Vendas")
st.plotly_chart(fig_evolucao, use_container_width=True)

st.subheader("Tabela de Dados Filtrados")
st.dataframe(df_filtrado)
