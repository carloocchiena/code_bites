# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 22:33:47 2017

@author: Carlo
"""

#finding a match with a string given by the user

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = raw_input("Enter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")