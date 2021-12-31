# create a list of hash from random input 

import itertools
import hashlib

temp = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=5)
f = open("passwords.txt", "w")
for pw in temp:
    p = ''.join(pw)
    encode = hashlib.md5(p.encode()).hexdigest() 
    f.write(p + " " + encode + "\n")
f.close()
