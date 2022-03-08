from pprint import pprint
from bs4 import BeautifulSoup
import requests

ur = "https://www.imdb.com/india/top-rated-indian-movies/"

r = requests.get(ur)
soup = BeautifulSoup(r.text, 'html.parser')

#print(soup)

def scrap_top_list():
    m_div = soup.find('div', class_="lister")
    tbody = m_div.find('tbody',class_="lister-list")
    trs = tbody.find_all('tr')
    
    movie_name = []
    movie_rank = []
    movie_rating = []
    movie_year = []
    movie_url = []
    #a = 1
    for tr in trs:
        position = tr.find('td', class_="titleColumn").get_text().strip()
        rank = ''
        for i in position:
            if '.' not in i:
                rank = rank+i
            else:
                break
        movie_rank.append(rank)
        title = tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)
        year = tr.find('td',class_="titleColumn").span.get_text()
        year = year[1:5]
        movie_year.append(year)
        url = tr.find('td',class_="titleColumn").a['href']
        movie_url.append("https://www.imdb.com"+url)
        rating  = tr.find('td', class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)
    top_movies = []
    movie_dict = {}
    for i in range(len(movie_rank)):
        movie_dict.update({'position':int(movie_rank[i]),'name':str(movie_name[i]),'year':int(movie_year[i]),'rating':float(movie_rating[i]),'url':movie_url[i]})
        top_movies.append(movie_dict)
        movie_dict = {}
    return top_movies


if __name__ == '__main__':
    print(scrap_top_list())