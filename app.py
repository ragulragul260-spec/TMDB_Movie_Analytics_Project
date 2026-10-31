import streamlit as st

st.set_page_config(
    page_title="TMDB Movie Analytics",
    layout="wide"
)

st.title("🎬 TMDB Movie Analytics Dashboard")

st.markdown("""
### Welcome

Use the navigation menu on the left:

✅ Filters

✅ Dashboard

✅ Query Explorer
""")

import streamlit as st
import pandas as pd

st.title("🎯 Filters")

movies = pd.read_csv(
    "data/cleaned_data_movies.csv"
)

movies["release_date"] = pd.to_datetime(
    movies["release_date"]
)

movies["release_year"] = (
    movies["release_date"].dt.year
)

# Language Filter

languages = sorted(
    movies["original_language"]
    .dropna()
    .unique()
)

st.session_state.language = st.selectbox(
    "Language",
    ["All"] + list(languages)
)

# Rating Filter

st.session_state.min_rating = st.slider(
    "Minimum Rating",
    0.0,
    10.0,
    5.0
)

# Release Year Filter

st.session_state.year_range = st.slider(
    "Release Year",
    int(movies["release_year"].min()),
    int(movies["release_year"].max()),
    (
        int(movies["release_year"].min()),
        int(movies["release_year"].max())
    )
)

# Apply Filters

filtered_movies = movies[
    (movies["vote_average"] >= st.session_state.min_rating)
]

st.metric(
    "Matching Movies",
    len(filtered_movies)
)

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