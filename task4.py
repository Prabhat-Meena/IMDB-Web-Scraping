from bs4 import BeautifulSoup
from pprint import pprint
import requests
from task1 import*

scraper = scrap_top_list()
def scrap_movie_details(movie_url):
    movie_details = {}
    page = requests.get(movie_url)
    soup = BeautifulSoup(page.text,'html.parser')

#name= '', director=[], country='',language=[],
#poster_url='', bio='', runtime=int, gener=[]
    #title_div.h1.text se movie title scrape kr sakte hai
    title_div = soup.find('div',class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk")
    movie_details.update({"name":title_div.h1.text})
    #print(title_div.h1.text)
    # director.get_text() se movies directors name scrap karenge
    director_div = soup.find('div',class_="ipc-metadata-list-item__content-container")
    movie_details.update({"Director":[i.get_text() for i in director_div]})
    #print(director.get_text())
    lng_con_ul = soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    poster_ur = soup.find('a',class_="ipc-lockup-overlay ipc-focusable")['href']

    #bio_div = soup.find('div',class_="GenresAndPlot__ContentParent-sc-cum89p-8 hTqGWn Hero__GenresAndPlotContainer-sc-kvkd64-11 iEHpKn").p.span.get_text()
    runtime=title_div.find_all("li",class_="ipc-inline-list__item")
    gener_span = soup.find("span",class_="ipc-chip__text")#.text

    for j in lng_con_ul:
        language = []
        if "Language" in j.text:
            li = j.find_all("li")
            # print(c)
            for i in li:
                if "Language" in i.text:
                    div = i.find("div")
                    atag = div.find_all("a")
                    for k in atag:
                        language.append(k.get_text())
                    movie_details.update({'language':language})
                if "Country" in i.text:
                    a = i.find("a")
                    movie_details.update({"country":a.get_text()})

    movie_details.update({"posterUrl":"https://www.imdb.com"+poster_ur})
    try:
        bio_div = soup.find('div',class_="GenresAndPlot__ContentParent-sc-cum89p-8 hTqGWn Hero__GenresAndPlotContainer-sc-kvkd64-11 iEHpKn").p.span.get_text()
        movie_details.update({"bio":bio_div})
    except Exception as e:
        pass

    a = 0
    for i in runtime:
        if a == 2:
            movie_details.update({"runtime":i.text})
        a = a+1

    movie_details.update({"gener":[i.get_text() for i in gener_span]})

    return movie_details

inp = int(input('Enter any movie rank 1 to 250 : '))
url = scraper[inp-1]['url']
#url = 'https://www.imdb.com/title/tt8176054/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=ZEHT60X0B4ASE24WXQB0&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1'
if __name__ == '__main__':
    print(scrap_movie_details(url))
