#!/usr/bin/env python

import recommender as rc
import os

clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')

def main_menu(movies=None, shows=None):
    """
    Show the recommendation options on the screen.
    """
    
    print("Loading...")
    indices_movies, cosine_sim_movies = rc.preparation(data=movies)
    indices_shows, cosine_sim_shows = rc.preparation(data=shows)
    clear()

    ret = -1
    while ret != 3:
        print('**' * 40)    
        print("Select your option:\n")
        print('1 - Movie recomendation')
        print('2 - TV Show recommendation')
        print('3 - Exit')
        print('**' * 40)
        ret = int(input('Ret: '))

        if ret == 1:
            clear()
            index = rc.getTitle(indices=indices_movies)
            if index:
                rc.getRecommendation(index=index, data=movies, cosine_sim=cosine_sim_movies)
                input("\n(Press anithing)")
        elif ret == 2:
            clear()
            index = rc.getTitle(indices=indices_shows)
            if index:
                rc.getRecommendation(index=index, data=shows, cosine_sim=cosine_sim_shows)
                input("\n(Press anithing)")

        clear()

if __name__ == "__main__":
    main_menu()
