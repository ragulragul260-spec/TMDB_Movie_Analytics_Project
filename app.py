import streamlit as st

st.set_page_config(
    page_title="TMDB Movie Analytics",
    layout="wide"
)

st.title("🎬 TMDB Movie Analytics Dashboard")

st.markdown("""
### Welcome to the TMDB Movie Analytics Dashboard

This project analyzes movie data collected from TMDB and provides insights into:

✅ Movie Revenue Analysis

✅ Movie Ratings & Popularity

✅ Runtime Trends

✅ Budget vs Revenue Performance

✅ Interactive Query Exploration

---

### 📂 Dashboard Pages

🔹 **Filters**  
Apply filters to explore movies by language, rating, popularity, and release year.

🔹 **Dashboard**  
View interactive visualizations and movie analytics.

🔹 **Query Explorer**  
Run pre-built analytical queries and gain business insights.

---

### 🎯 Project Objective

To analyze TMDB movie datasets and identify patterns in movie success, audience engagement, popularity, ratings, and profitability using Python, SQL, and Streamlit.

---
""")

st.success("Use the left navigation menu to begin exploring the dashboard.")
