import recommender as rc 
import streamlit as st

st.set_page_config(
    page_title="TV Show Recommender",
    page_icon="🍿",
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
    st.write("# TV Show Recommender 🍿")
    shows = rc.open_csv(filepath="../data/clean/title.csv", type='show')
    indices_shows, cosine_sim_shows = rc.preparation(data=shows)

    index = rc.getTitle(indices=indices_shows, data=shows)
    if index:
        rc.getRecommendation(index=index, data=shows, cosine_sim=cosine_sim_shows)

    for key in st.session_state:
        del st.session_state[key]

if __name__ == "__main__":
    main()
