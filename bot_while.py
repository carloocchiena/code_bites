# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 21:39:41 2017

@author: Carlo
"""
#chatboat trial

#intro and asking for a name
print "Hello! I'm Renzo, your new robo-friends!"
name = raw_input("What's your name?")
print "Hello "+ name.title() +"!"

#talking about the weather

print
meteo=str(raw_input("What's the weather like, today?"))
count=0
#define statement true \ false for while loop and counter
while "sunny" in meteo or "hot" in meteo or "cloudy" in meteo or "rainy" in meteo \
or "wet" in meteo:
    
    if "sunny" in meteo or "hot" in meteo and count <3:
        count+=4
        print meteo.title()+"? Wow! Wonderful! Let's go to the beach then!"


    elif "cloudy" in meteo and count <3:
        count+=4
        print meteo.title()+"? Oh..what a shame...but it could always get better!"


    elif "rainy" in meteo or "wet" in meteo and count <3:
        count+=4
        print meteo.title()+ "? So...I think it's better to stay inside!"


else:
    count=+1
    print "mmmm...i'm not getting it...It's sunny, cloudy or rainy?"
    meteo=raw_input()




