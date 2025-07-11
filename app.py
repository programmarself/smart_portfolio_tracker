import streamlit as st
import pandas as pd
from utils import show_summary, show_visuals, recommend_rebalance
from forecast import forecast_asset_prices

st.set_page_config(page_title="Smart Portfolio Tracker", layout="wide")
st.title("📈 Smart Portfolio Tracker")

uploaded_file = st.file_uploader("Upload your portfolio CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    st.success("✅ Portfolio Data Loaded")
    st.write(df.head())

    show_summary(df)
    show_visuals(df)
    recommend_rebalance(df)
    forecast_asset_prices(df)
