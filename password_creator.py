import random

def psw_maker():
    
    alpha="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    spec="!'£$%&/()?^*+/-"
    psw=""
    
    length=int(input("how many characters do you want your password to be?\n"))
    
    for i in range(0, length):
        char=random.choice(alpha)+random.choice(num)+random.choice(spec)+random.choice(alpha.upper())
        psw += str(char)
        
    return psw 
