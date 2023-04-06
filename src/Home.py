import recommender as rc
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Report a bug': "https://github.com/dgoenrique/whatsNext/issues/new/choose",
        'About': """
         whatsNext Recommendation System by [Diego Enrique](https://github.com/dgoenrique).
        """
    }
)

def main():

    st.markdown("""
       # whatsNext

       ### A simple Movie and Tv Show Recommendation System

    """)

    img = Image.open('../img/clap.jpg')
    st.image(img, caption='Photo by Jakob Owens')

    st.markdown("""
       Recommendation systems play a crucial role in the success of streaming platforms
       by providing personalized content suggestions to users and increasing user engagement.
       Streaming platforms, such as Netflix and Disney+, uses these systems to recommend movies 
       and TV shows based on the user's previous viewing history. 

       So, in this project, I build a simple plot description-based recommendation system 
       for Movies and TV Shows with the data from these streaming platforms:

       * [Disney+](https://www.disneyplus.com/)
       * [AppleTV+](https://www.apple.com/apple-tv-plus/)
       * [Amazon Prime Video](https://www.primevideo.com/)
       * [HBO Max](https://www.hbomax.com/)
       * [Netflix](https://www.netflix.com/)
       * [Paramount+](https://www.paramountplus.com/)
       
       The data was collected from [JustWatch](https://www.justwatch.com/us) in April 2023, 
       containing data available in the United States.

       This Recommender System is not perfect. Sometimes it may recommend something not quite related.
       But it was a good test to try some skills I learned.
    """)

    st.markdown("""
        ## Get a Recommendation 
    """)

    l_column, r_column = st.columns(2)
    movie_button = l_column.button("Movie Recommendation")
    show_button = r_column.button("TV Show Recommendation")
    if movie_button:
        switch_page("Movie Recommender")
    if show_button:
       switch_page("TV Show Recommender")
    
    st.markdown("""
        ---
       *This Recommendation System is based on [this notebook](https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system)
       from [Ibtesam Ahmed](https://www.kaggle.com/ibtesama)*.
    """)


if __name__ == "__main__":
    main() 
