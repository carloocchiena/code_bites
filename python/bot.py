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

print "What's the weather like, today?"
meteo=raw_input()
count=0

if "sunny" in meteo or "hot" in meteo: 
    print "Wow! Wonderful! Let's go to the beach then!"
    count+=1
    
elif "cloudy" in meteo:
    print "oh..what a shame...but it could always get better!"
    count+=1
elif "rainy" in meteo or "wet" in meteo:
    print "so...I think it's better to stay inside!"
    count+=1
else:
    print "mmmm...i'm not getting it...It's sunny, cloudy or rainy?"
    count+=1
        
print count         
