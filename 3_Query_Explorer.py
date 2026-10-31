import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv(
    "data/cleaned_data_movies.csv"
)

st.title("🔍 Query Explorer")

query = st.selectbox(
    "Select Saved Query",
    [
        "Top Revenue Movies",
        "Top Rated Movies",
        "Most Popular Movies",
        "Longest Runtime Movies"
    ]
)

if query == "Top Revenue Movies":

    result = (
        movies
        .sort_values(
            "revenue",
            ascending=False
        )
        .head(10)
    )

    column = "revenue"

    insight = (
        "Blockbuster movies dominate total revenue."
    )

elif query == "Top Rated Movies":

    result = (
        movies
        .sort_values(
            "vote_average",
            ascending=False
        )
        .head(10)
    )

    column = "vote_average"

    insight = (
        "These movies have the highest audience ratings."
    )

elif query == "Most Popular Movies":

    result = (
        movies
        .sort_values(
            "popularity",
            ascending=False
        )
        .head(10)
    )

    column = "popularity"

    insight = (
        "These movies generated the highest public interest."
    )

else:

    result = (
        movies
        .sort_values(
            "runtime",
            ascending=False
        )
        .head(10)
    )

    column = "runtime"

    insight = (
        "These are the longest movies in the dataset."
    )

st.dataframe(result)

fig, ax = plt.subplots(
    figsize=(10,5)
)

sns.barplot(
    data=result,
    x=column,
    y="title",
    ax=ax
)

st.pyplot(fig)

st.info(insight)