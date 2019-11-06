# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 21:40:45 2017

@author: Carlo
"""

import bs4
import requests

def estrapola_sorgente(url):
    if "http://" in url:
        sorgente=requests.get(url).text
        return(sorgente)
    else:
        return ("l'url non è valido")

def estrapola_font(sorgente):
    soup=bs4.BeautifulSoup(sorgente)
    #elenco=soup.findAll("h1")
    elenco=soup.find_all("font-family")
    if elenco:
        for a in elenco:
            print a
            with open("provascrap.txt", "w") as text_file:
                text_file.write(str(a))
        else:
            print "non ci sono font in questa pagina"
            
            
lista_siti=[
        "http://www.repubblica.it",
        "http://www.wired.it",
        "http://www.cucinaconsapevole.it",
        ]

for sito in lista_siti:
    sorgente=estrapola_sorgente(sito)
    print ("elenco dei font di " + sito)
    estrapola_font(sorgente)
    print()