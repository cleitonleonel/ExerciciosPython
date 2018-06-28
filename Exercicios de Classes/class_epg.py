#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
import requests
import re
from bs4 import BeautifulSoup


url = 'https://meuguia.tv/programacao/categoria/Aberta'


def open_url(url):
    response = requests.get(url)
    html = response.text
    #print(html)
    return html


def programacao_canais(url):
    html = open_url(url)
    #print(html)
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)
    div = soup.find("div",{"class":"mw content"})
    programacao = div.findAll("li")
    #print(programacao)
    for item in programacao:
        #print(item)
        list_canais = ['Band Rede','Record','SBT','TV Cultura','TV Globo']
        try:
            canal = item.h2.text
        except:
            pass
        if canal in list_canais:
            prog = item.a['title']
            start = item.a.h3.strong.text
            print(start)
            print(prog)
            print(canal)


if __name__ == '__main__':
    programacao_canais(url)