import recommender as rc 
import streamlit as st

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Report a bug': "https://github.com/dgoenrique/whatsNext/issues/new/choose",
        'About': """
         whatsNext Recommendation System by [Diego Enrique](https://github.com/dgoenrique).
        """
    }
)

def main():
    st.write("# Movie Recommender 🎥")
    movies = rc.open_csv(filepath="../data/clean/title.csv",type='movie')
    indices_movies, cosine_sim_movies = rc.preparation(data=movies)

    index = rc.getTitle(indices=indices_movies, data=movies)
    if index:
        rc.getRecommendation(index=index, data=movies,cosine_sim=cosine_sim_movies)
    
    for key in st.session_state:
        del st.session_state[key]

if __name__ == "__main__":
    main()
