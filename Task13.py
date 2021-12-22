from Task1_IMDB import scrapped
from Task12 import scrape_movie_cast
from Task5 import all_movies
import json

def casting():
    list=[]
    for i in range(10):
        list.append(all_movies[i])
    for i in range(10):
        api=scrapped[i]["movie_url"]
        sd=scrape_movie_cast(api)
        list[i]["cast"]=sd

    with open("Task13_casting.json","w") as file:
        json.dump(list,file,indent=4)

    return list

cast=casting()