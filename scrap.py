import sys
from os import path
import csv
from bs4 import BeautifulSoup
import requests


def parse_recipe(article):
    ''' return a dict {name, difficulty, prep_time} modelising a recipe'''
    return {'href': article.find('a',class_="btn").string}

def parse(html):
    ''' return a list of dict {name, difficulty, prep_time} '''
    html_p=BeautifulSoup(html, "html.parser")
    print(html_p)
    return [parse_recipe(i) for i in html_p.find_all('div', id_= 'exercise_results')]


if __name__ =="__main__":
    for path in paths:
        print(path)
        response=requests.get(url, params={path:path}).text
        print(parse(response))
