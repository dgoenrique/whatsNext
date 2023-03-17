#!/usr/bin/env python

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def dataPreparation(data=None):
    #Define a TF-IDF Vectorizer Object. 
    #This remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words='english')

    #Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(data['description'])

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Identify the index of a movie/show in our metadata DataFrame
    indices = pd.Series(data.index, index=data['title'])

    return indices, cosine_sim

def getTitle(indices=None):
   pass 

def getRecommendation(title=None, data=None, indices=None, cosine_sim=None):
    
    idx = indices[title]
      
    print('**' * 40)

    print(f"Symilar to: {data['title'].iloc[idx]} ({data['release_year'].iloc[idx]})", end="\n\n")

    # Get the pairwsie similarity scores of all movies/shows with that movie/show
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies/shows based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies/shows
    sim_scores = sim_scores[1:11]

    # Get the movie/show indices
    data_indices = [i[0] for i in sim_scores]
    
    for i in data_indices:
        print(data['title'].iloc[i], end=' ')
        print(f"({data['release_year'].iloc[i]})")

    print('**' * 40)

if __name__ == "__main__":
    pass
