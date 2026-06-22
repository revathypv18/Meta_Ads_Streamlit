import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meta Ads Analysis", layout="wide")

st.title("📊 Meta Ads Analysis Dashboard")

# Display the Power BI screenshot
st.image("dashboard.png", width="stretch")

# Load all CSV files
ads = pd.read_csv("ads.csv")
campaigns = pd.read_csv("campaigns.csv")
users = pd.read_csv("users.csv")
ad_events = pd.read_csv("ad_events.csv")

# Show the data
st.header("Ads")
st.dataframe(ads)

st.header("Campaigns")
st.dataframe(campaigns)

st.header("Users")
st.dataframe(users)

st.header("Ad Events")
st.dataframe(ad_events)