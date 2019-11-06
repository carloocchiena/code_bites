# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 21:52:55 2017

@author: Carlo
"""
#import webbrowsert module
import webbrowser


#allowing user to pick the language and checkin for errors
translate=str(raw_input("Select the desired translaction: ITAENG or ENGITA:\n"))
while translate.lower() not in ("itaeng","engita", "eng", "ita"):
    print "Please, translator only works for inputs ITAENG or ENGITA."
    translate=str(raw_input("Select the desired translaction: ITAENG or ENGITA:\n"))

#input for the word to be used 
try:
    word=str(raw_input("Which word do you want to translate?\n"))
except ValueError:
    print "Please, input a valid word!"
    word=str(raw_input("Which word do you want to translate?\n"))

if translate.lower() in ("engita", "eng"):
    webbrowser.open("http://www.wordreference.com/enit/"+word)
elif translate.lower() in ("itaengl", "eng"):
    webbrowser.open("http://www.wordreference.com/iten/"+word)
    