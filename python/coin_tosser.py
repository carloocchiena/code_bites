# coin tosser generator
import random

count=0
coin=["head", "cross"]
toss=[]

coinflip=int(input("How many time do you want to toss the coin?\n"))


while count < coinflip:

    flip=random.choice(coin)
    toss.append(flip)
    count +=1

recaphead=toss.count("head")
recapcross=toss.count("cross")

print (f"You have {recaphead} heads and {recapcross} cross!")
