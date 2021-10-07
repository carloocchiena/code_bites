# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 21:11:41 2019

@author: Carlo
"""

#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#setting max size for the pandas table
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 200)

#getting the data from the forecast page, prettifying it and create var for the html attribute 
page= requests.get("https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XC0c3lVKgrg")
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())    

#create var & print html element of interest as find in text
period = tonight.find(class_= "period-name").get_text()
short_desc = tonight.find(class_= "short-desc").get_text()
temp = tonight.find(class_= "temp").get_text()

print()
print(period)
print(short_desc)
print(temp)

img = tonight.find("img") 
desc = img["title"]
print(desc)


#create var for all the week searching html tag in bundle
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

print (periods)

short_descs = [sd.get_text() for sd in seven_day.select (".tombstone-container .short-desc")]
temps = [t.get_text () for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print (short_descs)
print (temps)
print (descs)
print(periods)
#vediamo se i dati da mettere in tabella sono tutti lungi uguali altrimenti mi da un errore di array
print (len(short_descs), len(temps), len(descs), len(periods))
print ("\n")
print ("\n")

#organize our data in pandas
weather = pd.DataFrame({
        "Period": periods,
        #"short_desc": short_descs,
        "Temp": temps,
        #"desc": descs
        })
weather

print (weather)

temp_nums = weather["Temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype("int")
temp_nums

temp_avg= weather["temp_num"].mean()


round(temp_avg,2)

print ("\n")
print ("Temp average: ", temp_avg)





