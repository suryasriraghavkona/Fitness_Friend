import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def show_dashboard(data):
    df = pd.DataFrame(data, columns=["date", "activity", "value"])

    st.subheader("📊 Data")
    st.dataframe(df)

    st.subheader("📈 Daily Progress")
    df["date"] = pd.to_datetime(df["date"])
    trend = df.groupby("date")["value"].sum()
    st.line_chart(trend)

    st.subheader("🥧 Activity Distribution")
    pie = df.groupby("activity")["value"].sum()

    fig, ax = plt.subplots()
    pie.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    st.pyplot(fig)