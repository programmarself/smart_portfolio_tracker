import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def show_summary(df):
    st.subheader("📊 Portfolio Summary")
    latest_prices = df.groupby("Asset")["Price"].last()
    returns = df.groupby("Asset")["Price"].apply(lambda x: x.pct_change().mean()).fillna(0)
    summary = pd.DataFrame({
        "Latest Price": latest_prices,
        "Average Daily Return": returns
    })
    st.dataframe(summary.style.format({"Latest Price": "{:.2f}", "Average Daily Return": "{:.2%}"}))

def show_visuals(df):
    st.subheader("📈 Price Trends")
    assets = df["Asset"].unique()
    for asset in assets:
        asset_data = df[df["Asset"] == asset]
        st.line_chart(asset_data.set_index("Date")["Price"], height=200)

def recommend_rebalance(df):
    st.subheader("🔄 Rebalancing Recommendation")
    mean_returns = df.groupby("Asset")["Price"].apply(lambda x: x.pct_change().mean()).fillna(0)
    total = mean_returns.abs().sum()
    weights = (mean_returns.abs() / total).sort_values(ascending=False)
    st.write("Suggested Portfolio Weights Based on Return Volatility")
    st.bar_chart(weights)
