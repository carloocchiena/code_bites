# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 13:42:36 2017

@author: Carlo
"""


#intro and asking for a name
print("Hello! I'm Renzo, your new robo-friends!")
name = raw_input("What's your name?")
print("Hello "+ name.title() +"!")
 
#talking about the weather
meteo=str(raw_input("What's the weather like, today?"))
count=0
 
while "sunny" not in meteo  and count<3:
    count += 1
    print("mmmm...i'm not getting it...It's sunny, cloudy or rainy?")
    print("Again, what's the weather like, today?")
    meteo=raw_input()
    
else:
        if meteo.lower() in ["sunny","hot"]:
            print(meteo.title()+"? Wow! Wonderful! Let's go to the beach then!")
    
        elif meteo.lower() in ["cloudy"]:
            print(meteo.title()+"? Oh..what a shame...but it could always get better!")
    
        elif meteo.lower() in ["rainy" , "wet"]:
            print(meteo.title()+ "? So...I think it's better to stay inside!")
 