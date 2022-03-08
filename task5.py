from task1 import*
from task4 import scrap_movie_details
from pprint import pprint

scraper = scrap_top_list()

def get_movie_list_details(movies):
    movie_list = []

    for i in movies:
        scraper = i['url']
        a = (scrap_movie_details(scraper))
        movie_list.append(a)

    return movie_list

#for i in range(11,251,10):
movieUrl = scraper

if __name__ == '__main__':
    pprint(get_movie_list_details(movieUrl))
