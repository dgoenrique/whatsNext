import streamlit as st
import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


@st.cache_data
def open_csv(filepath="None", type=None):
    """
    Function that takes as input a file path and 
    returns the data  from Movies and Tv Shows.
    """
    data = pd.read_csv(filepath)

    if type == 'movie':
        movies = data[data['type'] == 'MOVIE'].copy().reset_index()
        movies.drop(['index'], axis=1, inplace=True)
        movies['streaming_platform'] = movies['streaming_platform'].str.replace('[','').str.replace("'",'').str.replace(']','')
        return movies
    else:
        shows = data[data['type'] == 'SHOW'].copy().reset_index()
        shows.drop(['index'], axis=1, inplace=True)
        shows['streaming_platform'] = shows['streaming_platform'].str.replace('[','').str.replace("'",'').str.replace(']','')
        return shows 

@st.cache_resource
def preparation(data=None):
    """
    A function that prepares the cosine similarity function
    and the 'index searcher'.
    """
    #Define a TF-IDF Vectorizer Object. 
    #This remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(data['description'])

    #Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Identify the index of a movie/show in our metadata DataFrame
    indices = pd.Series(data.index, index=data['id'])

    return indices, cosine_sim


def getTitle(indices=None, data=None):
    """
    Function that gets the 'index searcher' and searches
    the user's title index.
    """
    #Use a text_input to get the keywords to filter the dataframe
    title = st.text_input("**Search for similar titles to:**", key='title').lower()

    try:
        #Mask to search for a title
        mask = data['title'].str.lower().str.contains(title)
    except:
        return

    search = data[mask]

    placeholder = st.empty()

    with placeholder.container():
        number_cards = 3
        if title:
            st.write("## Select a Title:")
            for n_row, row in search.reset_index().iterrows():
                i = n_row%number_cards
                if i==0:
                    st.write("---")
                    cols = st.columns(number_cards, gap="large")
                #draw the card
                with cols[n_row%number_cards]:
                    st.markdown(f"### {row['title'].strip()} ({row['release_year']})")
                    st.markdown(f"**Genre:** {row['genre'].strip().title()}")
                    st.markdown(f"**Description:** {row['description'].strip()}")
                    st.markdown(f"**IMDb Score ⭐:** {row['imdb_score']}")
                    st.markdown(f"**TMDB Score ⭐:** {row['tmdb_score']}")
                    st.markdown(f"**Available on:** {row['streaming_platform'].title()}")
                    if st.button("Select this title", key=f"button_{row['id']}"):
                        index = indices[row['id']] 
                        placeholder.empty()
                        return index


def getRecommendation(index=None, data=None, cosine_sim=None):
    """
    A function that takes a title index, the data, and the 
    cosine similarity  as input and prints on the screen the 
    10 most similar titles based on description.
    """
    #Get the pairwsie similarity scores of all movies/shows with that movie/show
    sim_scores = list(enumerate(cosine_sim[index]))

    #Sort the movies/shows based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    #Get the scores of the 10 most similar movies/shows
    sim_scores = sim_scores[1:11]

    #Get the movie/show indices
    data_indices = [i[0] for i in sim_scores]

    st.markdown(f"# Similar Titles to {data['title'].iloc[index]} ({data['release_year'].iloc[index]}):")

    for i in data_indices:
        st.write("---")
        st.markdown(f"### {data['title'].iloc[i].strip()} ({data['release_year'].iloc[i]})")
        st.markdown(f"**Genre:** {data['genre'].iloc[i].strip().title()}")
        st.markdown(f"**Description:** {data['description'].iloc[i].strip()}")
        st.markdown(f"**IMDb Score ⭐:** {data['imdb_score'].iloc[i]}")
        st.markdown(f"**TMDB Score ⭐:** {data['tmdb_score'].iloc[i]}")
        st.markdown(f"**Available on:** {data['streaming_platform'].iloc[i].title()}")

