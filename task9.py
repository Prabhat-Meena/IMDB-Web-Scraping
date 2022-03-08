from pprint import pprint
from task1 import*
import json, os, random, time


top_movies = scrap_top_list()
random_sleep = random.randint(1,3)
# scrap_movie_details = task4
def scrap_movie_details(movie_url):
    movie_id = ''
    for id in movie_url[27:]:
        if '/' not in id:
            movie_id += id
        else:
            break
    file_name = movie_id + '.json'

    text = None
    if os.path.exists(file_name):
        print('hello')
        f = open(file_name)
        text = f.read()
        return text
    if text is None:
        time.sleep(random_sleep)
        print('sorry')

        #task 4
        movie_details = {}
        page = requests.get(movie_url)
        soup = BeautifulSoup(page.text,'html.parser')

        title_div = soup.find('div',class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk")
        movie_details.update({"name":title_div.h1.text})
        director_div = soup.find('div',class_="ipc-metadata-list-item__content-container")
        movie_details.update({"Director":[director_div.get_text()]})
        lng_con_ul = soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        poster_ur = soup.find('a',class_="ipc-lockup-overlay ipc-focusable")['href']

        runtime=title_div.find_all("li",class_="ipc-inline-list__item")
        gener_span = soup.find("span",class_="ipc-chip__text").text

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

        movie_details.update({"gener":[gener_span]})
        
        #task 8
        file1 = open(file_name, 'w')
        raw = json.dumps(movie_details, indent=4)
        file1.write(raw)
        file1.close()

        return movie_details

#scraper = scrap_top_list() = top_movies

def get_movie_list_details(movies):
    movie_list = []

    for i in movies:
        scraper = i['url']
        a = (scrap_movie_details(scraper))
        movie_list.append(a)

    return movie_list

#for i in range(11,251,10):
movieUrl = top_movies

movie_detail = get_movie_list_details(movieUrl)
# pprint(movie_detail)

# url = top_movies[3]['url']
if __name__ == '__main__':
    print(scrap_movie_details(movie_detail))