import random
import time


def morra():
  segni=["carta","forbici", "sasso"]
  win=False

  while win==False:
    
    player1turn=input("scegli un segno: carta, forbici, sasso:\n")

    if player1turn in segni:
      pass
    else:
      print ("Amico hai scelto un segno non valido, riprova")
      morra()  

    pcturn=random.choice(segni)
    print ("ora tocca a me...")
    time.sleep(0.5)
    print (f"io scelgo {pcturn}")

    if player1turn=="carta" and pcturn=="sasso" or player1turn == "forbici" and pcturn == "carta" or player1turn=="sasso" and pcturn =="forbici":
      print ("Hai vinto")
      again=input("un'altra?")
      if again.lower() == "sì" or again.lower() == "si":
        morra()
      else:
        print ("va bene! basta così")
        win==False  
      break
    elif player1turn == pcturn:
      print ("Pareggio!")
    else:
      print ("Hai perso")
      again=input("un'altra?")
      if again.lower() == "sì" or again.lower() == "si":
        morra()
      else:
        print ("va bene! basta così")
        win==False  
      break
        
if name = "__main__":
  morra()




 
