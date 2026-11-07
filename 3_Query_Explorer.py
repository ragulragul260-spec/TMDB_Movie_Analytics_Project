import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv("data/cleaned_data_movies.csv")

st.title("🔍 Query Explorer")

query = st.selectbox(
    "Select Saved Query",
    [
        "Top Revenue Movies",
        "Top Rated Movies",
        "Most Popular Movies",
        "Longest Runtime Movies",
        "Highest Vote Count",
        "Lowest Rated Movies",
        "Shortest Runtime Movies",
        "Most Profitable Movies",
        "Top Budget Movies",
        "Latest Released Movies"
    ]
)

# Query 1
if query == "Top Revenue Movies":

    result = movies.sort_values(
        "revenue",
        ascending=False
    ).head(10)

    column = "revenue"

    insight = (
        "These movies generated the highest box office revenue."
    )

# Query 2
elif query == "Top Rated Movies":

    result = movies.sort_values(
        "vote_average",
        ascending=False
    ).head(10)

    column = "vote_average"

    insight = (
        "These movies received the best audience ratings."
    )

# Query 3
elif query == "Most Popular Movies":

    result = movies.sort_values(
        "popularity",
        ascending=False
    ).head(10)

    column = "popularity"

    insight = (
        "These movies achieved the highest popularity scores."
    )

# Query 4
elif query == "Longest Runtime Movies":

    result = movies.sort_values(
        "runtime",
        ascending=False
    ).head(10)

    column = "runtime"

    insight = (
        "These are the longest movies in the dataset."
    )

# Query 5
elif query == "Highest Vote Count":

    result = movies.sort_values(
        "vote_count",
        ascending=False
    ).head(10)

    column = "vote_count"

    insight = (
        "These movies attracted the highest number of audience votes."
    )

# Query 6
elif query == "Lowest Rated Movies":

    result = movies.sort_values(
        "vote_average",
        ascending=True
    ).head(10)

    column = "vote_average"

    insight = (
        "These movies received the lowest ratings."
    )

# Query 7
elif query == "Shortest Runtime Movies":

    result = movies.sort_values(
        "runtime",
        ascending=True
    ).head(10)

    column = "runtime"

    insight = (
        "These movies have the shortest runtime."
    )

# Query 8
elif query == "Most Profitable Movies":

    movies["profit"] = (
        movies["revenue"]
        - movies["budget"]
    )

    result = movies.sort_values(
        "profit",
        ascending=False
    ).head(10)

    column = "profit"

    insight = (
        "These movies earned the highest profit after production costs."
    )

# Query 9
elif query == "Top Budget Movies":

    result = movies.sort_values(
        "budget",
        ascending=False
    ).head(10)

    column = "budget"

    insight = (
        "These movies had the highest production budgets."
    )

# Query 10
else:

    movies["release_date"] = pd.to_datetime(
        movies["release_date"]
    )

    result = movies.sort_values(
        "release_date",
        ascending=False
    ).head(10)

    column = "vote_average"

    insight = (
        "These are the most recently released movies."
    )

# Display Data

st.subheader("Query Results")

st.dataframe(
    result,
    use_container_width=True
)

# Visualization

fig, ax = plt.subplots(
    figsize=(12, 6)
)

sns.barplot(
    data=result,
    x=column,
    y="title",
    palette="viridis",
    ax=ax
)

ax.set_title(query)
ax.set_xlabel(
    column.replace("_", " ").title()
)
ax.set_ylabel("Movie Title")

plt.tight_layout()

st.pyplot(fig)

# Insight

st.subheader("Insights")

st.info(insight)
