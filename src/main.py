#!/usr/bin/env python

import opencsv as op
import menu

def main():
    movies, shows = op.open_csv(filepath='../data/clean/title.csv')
    menu.show_menu(movies=movies,shows=shows)

if __name__ == "__main__":
    main()
