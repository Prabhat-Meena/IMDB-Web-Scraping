from task2 import*
#importing group_by_year() from task2 and scrap_top_list() as scrapped from task1 to task2
movies_by_year = group_by_year(scrapped())

def group_by_decade(movies):
    movie_list = [i for i in movies]
    decade_list = [i for i in range(1950,2021,10)]
    movie_by_decade = {}
    movie_dic_list = []
    
    for i in decade_list:
        for j in movie_list:
            if (j>=i and j<(i+10)):
                movie_dic_list.append(j)
        movie_by_decade.update({i:movie_dic_list})
        movie_dic_list = []
    print(movie_by_decade)
    for i in movie_by_decade:
        for j in range(len(movie_by_decade[i])):
            movie_by_decade[i][j] = movies[movie_by_decade[i][j]]
        #print(movie_by_decade[i][0])

    return movie_by_decade

if __name__ == '__main__':

    pprint(group_by_decade(movies_by_year))