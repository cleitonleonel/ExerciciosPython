#!/usr/bin/env/python3
# -*- coding: UTF-8 -*-
#
import requests
import re
from bs4 import BeautifulSoup


url = 'https://meuguia.tv/programacao/categoria/Aberta'


def open_url():
    response = requests.get(url)
    html = response.text
    #print(html)
    return html


def programacao_canais():
    lista_programs = {}
    html = open_url()
    #print(html)
    soup = BeautifulSoup(html,'html.parser')
    #print(soup)
    div = soup.find("div",{"class":"mw content"})
    programacao = div.findAll("li")
    #print(programacao)

    resultado = {}
    for item in programacao:
        #print(item)
        numero_canais = {'TV Cultura':2,'TV Globo':4,'Record':6,'SBT':7,'Band Rede':10}
        list_canais = ['TV Cultura','TV Globo','Record','SBT','Band Rede']

        try:
            canal = item.h2.text
        except:
            pass
        if canal in list_canais:
            prog = item.a['title']
            start = item.a.h3.strong.text

            resultado = canal+";"+prog+";"+start
            #lista_canais.append(canal)
            #print(canal)
            #lista_horarios.append(start)
            #print(start)
            #lista_programs.append(prog)
            #print(prog)
            lista_programs[numero_canais[canal]]=resultado

    return lista_programs

if __name__=="__main__":
    programacao_canais()