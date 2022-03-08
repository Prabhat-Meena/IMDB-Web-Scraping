from task6 import*
from requests import models

task7 = get_movie_list_details(movieUrl)
movie_director={}
def analyse_movies_directors(movies_list):
    director = []
    s = ""
    for i in movies_list:
        name = s.join(i["Director"])
        director.append(name)
        movie_director.update({name:director.count(name)})
    return movie_director

if __name__ == "__main__":
    print(analyse_movies_directors(task7))