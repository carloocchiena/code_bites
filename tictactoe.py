# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:45:21 2019

@author: carlo
"""


#tictactoe demo game 

#variabili globali

A=[0,0,0,0,0,0,0,0,0]

PLAYED=[]


def board():
    print (" ".join(str(i) for i in A[0:3]))
    print (" ".join(str(i) for i in A[3:6]))
    print (" ".join(str(i) for i in A[6:9]))
  
def game():
  mark=0
   
  COUNT=0  #count is used to understand if a game is tie
  
  WIN=False 
  
  while not WIN:
    
    #player1 turn
    board()
    
    mark = int(input ("Player 1, select a cell from 1 to 9: "))

    if (mark) in PLAYED:
      print ("Nope man, this cell is already taken")
      pass
    else: 
      A[mark-1]=1
        
      PLAYED.append(mark)

      COUNT+=1

      #check if player 1 wins. If wins ask to play again and if y, clean the board and redo

      if A[0:3]==[1,1,1] or A[3:6]==[1,1,1] or A[6:9] ==[1,1,1] or (A[0]==1 and A[4]==1 and A[8]==1) or (A[2]==1 and A[4]==1 and A[6]==1):
          WIN = True
          board()
          print ("Yeah Player1 you win")
          bis=input("Do you want to play again?\n" "Y\\N\n")
          if bis == "y":   
              A[0:8]=[0,0,0,0,0,0,0,0,0]
              PLAYED[0:len(PLAYED)]=[]
              game()
          else:    
              break 


    #player2 turn. 
    board()
    
    mark = int(input ("Player 2, select a cell from 1 to 9: "))

    if (mark) in PLAYED:
      print ("Nope man, this cell is already taken")
      pass
    else: 
      A[mark-1]=2
        
      PLAYED.append(mark)

      COUNT+=1
      
      #check if player 1 wins. If wins ask to play again and if y, clean the board and redo

      if A[0:3]==[2,2,2] or A[3:6]==[2,2,2] or A[6:9] ==[2,2,2] or (A[0]==2 and A[4]==2 and A[8]==2) or (A[2]==2 and A[4]==2 and A[6]==2):
          WIN = True
          board()
          print ("Yeah Player2 you win")
          bis=input("Do you want to play again?\n" "Y\\N\n")
          if bis == "y":
              A[0:8]=[0,0,0,0,0,0,0,0,0]
              PLAYED[0:len(PLAYED)]=[]
              game()
          else:    
              break 
    
    if COUNT>=9:
      print ("DRAW MATCH")
      break
    
   
    
#this cell is just to run the game, but in the function should be included
game()



