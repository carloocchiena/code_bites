# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:08:42 2017

@author: Carlo
"""

#import urllib2 module
import urllib2

#input for the url
wiki="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#query the website and return html to the var page
page=urllib2.urlopen(wiki)

#import the Beautiful Soup function to parse the data from the website

from bs4 import BeautifulSoup

#parse the html in page variable and store it in beautiful soup format
soup = BeautifulSoup(page)

#print soup.prettify()

print soup.a
soup.find_all("a")

all_links=soup.find_all("a")
for link in all_links:
    print link.get("href")

all_tables=soup.find_all('table')

right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
right_table

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df

