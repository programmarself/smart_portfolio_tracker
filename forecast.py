import pandas as pd
import streamlit as st
from prophet import Prophet

def forecast_asset_prices(df):
    st.subheader("📉 Asset Forecasts (Next 30 Days)")
    assets = df["Asset"].unique()
    for asset in assets[:3]:  # Limit to 3 assets for performance
        st.write(f"Forecast for {asset}")
        data = df[df["Asset"] == asset][["Date", "Price"]].rename(columns={"Date": "ds", "Price": "y"})
        model = Prophet()
        model.fit(data)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        st.line_chart(forecast.set_index("ds")["yhat"])
