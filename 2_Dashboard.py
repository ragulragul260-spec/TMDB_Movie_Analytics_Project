import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv(
    "data/cleaned_data_movies.csv"
)

cast = pd.read_csv(
    "data/cast_cleaned.csv"
)

st.title("📊 Dashboard")

# KPI Cards

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Movies",
        movies["movie_id"].nunique()
    )

with c2:
    st.metric(
        "Genres",
        19
    )

with c3:
    st.metric(
        "Actors",
        cast["actor_name"].nunique()
    )

with c4:
    st.metric(
        "Average Rating",
        round(
            movies["vote_average"].mean(),
            2
        )
    )

# Top Revenue Movies

st.subheader("Top 10 Movies by Revenue")

top10 = (
    movies
    .sort_values(
        "revenue",
        ascending=False
    )
    .head(10)
)

fig, ax = plt.subplots(
    figsize=(10,5)
)

sns.barplot(
    data=top10,
    x="revenue",
    y="title",
    ax=ax
)

st.pyplot(fig)

# Budget vs Revenue

st.subheader("Budget vs Revenue")

fig, ax = plt.subplots(
    figsize=(8,6)
)

sns.scatterplot(
    data=movies,
    x="budget",
    y="revenue",
    ax=ax
)

st.pyplot(fig)

st.success(
    """
    Insight:

    Most high-budget movies generate larger revenues.
    Avatar remains one of the strongest box-office performers.
    """
)