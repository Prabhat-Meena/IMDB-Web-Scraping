
# Import scrap_top_list() from task1
from task1 import scrap_top_list as scrapped
from pprint import pprint


def group_by_year(movies):
    years = []
    for i in movies:
        year = i['year']
        if year not in years:
            years.append(year)
    mov_dict = {i:[] for i in years}
    # for i in years:
    #     mov_dict = {i:[]}
    for i in movies:
        year  = i['year']
        for j in mov_dict:
            if str(j) == str(year):
                mov_dict[j].append(i)
    return mov_dict

if __name__ == '__main__':
    pprint(group_by_year(scrapped()))