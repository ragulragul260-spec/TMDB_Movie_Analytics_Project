import streamlit as st
import pandas as pd

st.title("🎯 Movie Filters")

# Load Data
movies = pd.read_csv(
    "data/cleaned_data_movies.csv"
)

movies["release_date"] = pd.to_datetime(
    movies["release_date"],
    errors="coerce"
)

movies["release_year"] = (
    movies["release_date"]
    .dt.year
)

# =====================
# FILTERS
# =====================

col1, col2 = st.columns(2)

with col1:

    languages = sorted(
        movies["original_language"]
        .dropna()
        .unique()
    )

    language = st.selectbox(
        "🌍 Select Language",
        ["All"] + list(languages)
    )

with col2:

    min_rating = st.slider(
        "⭐ Minimum Rating",
        0.0,
        10.0,
        5.0
    )

year_range = st.slider(
    "📅 Release Year Range",
    int(movies["release_year"].min()),
    int(movies["release_year"].max()),
    (
        int(movies["release_year"].min()),
        int(movies["release_year"].max())
    )
)

# =====================
# FILTER LOGIC
# =====================

filtered_movies = movies.copy()

if language != "All":

    filtered_movies = (
        filtered_movies[
            filtered_movies[
                "original_language"
            ] == language
        ]
    )

filtered_movies = (
    filtered_movies[
        filtered_movies[
            "vote_average"
        ] >= min_rating
    ]
)

filtered_movies = (
    filtered_movies[
        (
            filtered_movies["release_year"]
            >= year_range[0]
        )
        &
        (
            filtered_movies["release_year"]
            <= year_range[1]
        )
    ]
)

# =====================
# KPI CARDS
# =====================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🎬 Matching Movies",
        len(filtered_movies)
    )

with c2:
    st.metric(
        "⭐ Avg Rating",
        round(
            filtered_movies[
                "vote_average"
            ].mean(),
            2
        ) if len(filtered_movies) > 0 else 0
    )

with c3:
    st.metric(
        "💰 Avg Revenue",
        f"{filtered_movies['revenue'].mean()/1000000:.1f}M"
        if len(filtered_movies) > 0
        else "0"
    )

# =====================
# PREVIEW TABLE
# =====================

st.subheader(
    "📄 Filtered Movies Preview"
)

st.dataframe(
    filtered_movies[
        [
            "title",
            "original_language",
            "release_year",
            "vote_average",
            "revenue"
        ]
    ].head(20),
    use_container_width=True
)
