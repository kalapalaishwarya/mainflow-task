# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(page_title="Data Visualization App", layout="wide")
st.title("📊 Interactive Data Visualization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        st.subheader("🔍 Preview of Uploaded Data")
        st.dataframe(df.head())

        # Get numeric and all columns
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        all_columns = df.columns.tolist()

        # Select visualization type
        vis_type = st.select
