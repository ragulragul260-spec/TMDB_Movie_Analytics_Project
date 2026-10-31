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