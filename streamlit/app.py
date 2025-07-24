
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Dashboard de Transactions", layout="wide")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("data/Transactions_data_complet.csv")
    df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])
    df["Year"] = df["TransactionStartTime"].dt.year
    df["Month"] = df["TransactionStartTime"].dt.month
    df["DayOfWeek"] = df["TransactionStartTime"].dt.day_name()
    df["Hour"] = df["TransactionStartTime"].dt.hour
    return df

df = load_data()

# Sidebar pour les filtres
st.sidebar.header("Filtres")
channel_filter = st.sidebar.multiselect("Canaux :", df["ChannelId"].unique(), default=df["ChannelId"].unique())
product_filter = st.sidebar.multiselect("Catégories de produit :", df["ProductCategory"].unique(), default=df["ProductCategory"].unique())

filtered_df = df[(df["ChannelId"].isin(channel_filter)) & (df["ProductCategory"].isin(product_filter))]

# Titre
st.title("Dashboard d'analyse des transactions & fraudes")

# Indicateurs
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", f"{len(filtered_df):,}")
col2.metric("Total Fraudes", f"{filtered_df['FraudResult'].sum():,}")
col3.metric("Taux de fraude", f"{(filtered_df['FraudResult'].mean()*100):.2f}%")

# Graphique 1 - Montant par jour de la semaine
st.subheader(" Répartition des montants par jour de la semaine")
fig1 = px.box(filtered_df, x="DayOfWeek", y="Amount", color="FraudResult",
              category_orders={"DayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]})
st.plotly_chart(fig1, use_container_width=True)

# Graphique 2 - Histogramme des montants
st.subheader("Distribution des montants de transactions")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["Amount"], bins=50, kde=True, ax=ax2)
st.pyplot(fig2)

# Graphique 3 - Nombre de fraudes par canal
st.subheader("Nombre de fraudes par canal")
frauds_by_channel = filtered_df[filtered_df["FraudResult"] == 1]["ChannelId"].value_counts()
fig3 = px.bar(x=frauds_by_channel.index, y=frauds_by_channel.values, labels={"x": "ChannelId", "y": "Nombre de fraudes"})
st.plotly_chart(fig3, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Projet Python pour la Finance • Réalisé par Adam")
