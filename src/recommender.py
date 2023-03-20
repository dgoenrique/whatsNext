#!/usr/bin/env python

import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')

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

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Identify the index of a movie/show in our metadata DataFrame
    indices = pd.Series(data.index, index=data['title'])

    return indices, cosine_sim

def getTitle(indices=None, data=None):
    """
    Function that gets the 'index searcher' and searches
    the user's title index.
    """
    print('**' * 40)
    title = input("Recommend similar titles to: ") 
    try:
        index = indices[title]  
        
    except:
        print("\n   Title not found") 
        print('**' * 40)
        input("\n(Press anithing)")
        return None

    if isinstance(index, np.int64):
            return index
    else:
        rt = -1
        while rt not in range(len(index)):
            print("\nThere are several titles with this name. Select the one you want: ")
            for i in range(len(index)):
                print(f"{i+1} - {data['title'].iloc[index[i]]}", end= " ")
                print(f"({data['release_year'].iloc[index[i]]})")
            rt = int(input("Title: ")) - 1
            if rt not in range(len(index)):
                clear()
                print('**' * 40)
        return index[rt]

def getRecommendation(index=None, data=None, cosine_sim=None):
    """
    A function that takes a title index, the data, and the 
    cosine similarity  as input and prints on the screen the 
    10 most similar titles based on description.
    """
    print('**' * 40)

    print(f"Symilar to: {data['title'].iloc[index]} ({data['release_year'].iloc[index]})", end="\n\n")

    # Get the pairwsie similarity scores of all movies/shows with that movie/show
    sim_scores = list(enumerate(cosine_sim[index]))

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
