#!/usr/bin/env python

import opencsv as op
import menus

def main():
    movies, shows = op.open_csv(filepath='../data/clean/title.csv')
    menus.main_menu(movies=movies,shows=shows)

if __name__ == "__main__":
    main()
