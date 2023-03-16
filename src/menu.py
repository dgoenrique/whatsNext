#!/usr/bin/env python

import recommender as rc
import os

clear = lambda : os.system('cls' if os.name == 'nt' else 'clear')

def show_menu(movies=None, shows=None):
    """
    Show the recommendation options on the screen
    """
    ret = -1
    while ret not in range(3):
        print('**' * 40)    
        print("Select your option:")
        print('1 - Movie recomendation')
        print('2 - TV Show recommendation')
        print('3 - Exit')
        print('**' * 40)
        ret = int(input('Ret: '))

        if ret == 1:
            rc.getMovieRecommendation(movies=movies)
        elif ret == 2:
            rc.getShowRecomendation(shows=shows)

        ret-=1
        clear()

if __name__ == "__main__":
    menu()
