#a simple game: guess the number, receive advice from the system

#import random function
import random 

#create a list from 1 to 100 included
lista=range(1,101)

#randomply picking a number
unknown_number=random.choice(lista)

#uncomment to show the number picked
#print unknown_number 

try:
  guess=int(raw_input("Pick a number from 1 to 100:"))
except ValueError:
  print "You should input a value!"
  guess=int(raw_input("Pick a number from 1 to 100:"))

while guess != unknown_number:
  
  if guess not in lista:
    print "nope man...pick a number from 1 to 100."
    guess=int(raw_input())
    
  elif guess > unknown_number:
    print "mmm, too big! Try a smaller number"
    guess=int(raw_input())
       
  elif guess < unknown_number:
    print "mmmm, too small! Try a bigger number"
    guess=int(raw_input())
      
else:
  print "whoa! that's great! Right number!"
      
      

#print unknown_number

