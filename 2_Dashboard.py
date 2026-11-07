import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
movies = pd.read_csv("data/cleaned_data_movies.csv")
cast = pd.read_csv("data/cast_cleaned.csv")

st.title("📊 Movie Dashboard")

# ======================
# KPI CARDS
# ======================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🎬 Movies",
              movies["movie_id"].nunique())

with c2:
    st.metric("🎭 Genres", 19)

with c3:
    st.metric("👥 Actors",
              cast["actor_name"].nunique())

with c4:
    st.metric(
        "⭐ Avg Rating",
        round(movies["vote_average"].mean(), 2)
    )

st.divider()

# ======================
# TWO CHARTS IN SAME ROW
# ======================

col1, col2 = st.columns(2)

# Top Revenue Movies

with col1:

    st.subheader("💰 Top 10 Movies by Revenue")

    top_revenue = (
        movies
        .sort_values(
            "revenue",
            ascending=False
        )
        .head(10)
    )

    fig1, ax1 = plt.subplots(
        figsize=(8,5)
    )

    sns.barplot(
        data=top_revenue,
        x="revenue",
        y="title",
        palette="Blues_r",
        hue="title",
        legend=False,
        ax=ax1
    )

    ax1.set_xlabel("Revenue")
    ax1.set_ylabel("Movie")

    st.pyplot(fig1)

# Top Rated Movies

with col2:

    st.subheader("⭐ Top Rated Movies")

    top_rated = (
        movies
        .sort_values(
            "vote_average",
            ascending=False
        )
        .head(10)
    )

    fig2, ax2 = plt.subplots(
        figsize=(8,5)
    )

    sns.barplot(
        data=top_rated,
        x="vote_average",
        y="title",
        palette="Greens_r",
        hue="title",
        legend=False,
        ax=ax2
    )

    ax2.set_xlabel("Rating")
    ax2.set_ylabel("Movie")

    st.pyplot(fig2)

# ======================
# FULL WIDTH CHART
# ======================

st.subheader("📈 Budget vs Revenue")

fig3, ax3 = plt.subplots(
    figsize=(12,6)
)

sns.scatterplot(
    data=movies,
    x="budget",
    y="revenue",
    alpha=0.7,
    color="red",
    ax=ax3
)

ax3.set_title(
    "Relationship Between Budget and Revenue"
)

st.pyplot(fig3)

# ======================
# INSIGHTS
# ======================

st.subheader("💡 Key Insights")

st.success(
    """
    • Higher budget movies generally earn higher revenue.

    • Avatar, Avengers and Titanic are among the top revenue generators.

    • Highly rated movies tend to receive stronger audience engagement.

    • Revenue and popularity show a positive trend for blockbuster films.
    """
)
