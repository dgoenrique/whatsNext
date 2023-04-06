#!/usr/bin/env python

import pandas as pd

def open_csv(filepath="../data/clean/title.csv"):
    """
    Function that takes as input a file path and 
    returns the data  from Movies and Tv Shows.
    """
   
    data = pd.read_csv(filepath)

    movies = data[data['type'] == 'MOVIE'].copy().reset_index()
    movies.drop(['index'], axis=1, inplace=True)

    shows = data[data['type'] == 'SHOW'].copy().reset_index()
    shows.drop(['index'], axis=1, inplace=True)

    return movies, shows


if __name__ == "__main__":
    movies, shows = open_csv()
    print(len(movies), len(shows))
