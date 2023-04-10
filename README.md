
<h1 align="center"> whatsNext </h1>
<h3 align="center"> A simple Movie and TV Show Recommendation System</h3>

<section align="center">
    <a href="https://unsplash.com/@jakobowens1">
        <img src="app/img/clap.jpg" alt="Clapperboard"/>
    </a>
    <div>
        Photo by <a href="https://unsplash.com/@jakobowens1">Jakob Owens</a>
    </div>
</section>

Recommendation systems play a crucial role in the success of streaming platforms
by providing personalized content suggestions to users and increasing user engagement.
Streaming platforms, such as Netflix and Disney+, uses these systems to recommend movies 
and TV shows based on the user's previous viewing history. 

So, in this project, I build a simple **plot description-based** recommendation system 
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

## Quickstart

### Online Version

You can access the recommendation system online [here](https://whatsnext.streamlit.app/).

### Local Version

Clone the repository:

```
git clone https://github.com/dgoenrique/whatsNext.git
```

Install all dependencies at once:

```
pip install -r requirements.txt
```

Go to the *app/* directory and type on your terminal:


```
streamlit run Home.py
```

---
*This Recommendation System is based on [this notebook](https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system)
from [Ibtesam Ahmed](https://www.kaggle.com/ibtesama)*.
