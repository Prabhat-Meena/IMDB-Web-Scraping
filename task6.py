from task5 import*
task5 = get_movie_list_details(movieUrl)
movie_language={}
def analyse_movies_language(movies_list):
    #movie_language = {}
    language1=[]
    b=""
    for i in movies_list:
        c=b.join(i["language"])
        language1.append(c)
        movie_language.update({c:language1.count(c)})
    return movie_language

if __name__ == '__main__':
    pprint(analyse_movies_language(task5))