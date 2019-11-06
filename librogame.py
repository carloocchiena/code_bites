#call the webbrowser module
import webbrowser

#defining the range of actions
action= { "a":"The skatepark looks gorgeous",
          "b":"Let's see what the streets have to offers! Keep pushin!",
          "c":"You head the rail full speed and...snap! Nailed a solid 5050 grind!",
          "d":"You try a slow approach...but hum! You're not able to hold on the tricks...you crashed!",
          "e":"You pop a solid ollie over the coping and snap an huge sad air! RAD!",
          "f":"You approach the coping and go for a stylish handplant! Way to go dude!",
          "g":"Feeling huge in the air, upside down for a great vert classic!" ,
          "h":"Blasting the transfer with a solid one, rollin in a clean landing in the pool!" ,
          "i":"You are almost reaching 88mph! Boom! What an ollie dude!" ,
          "j":"Just a quick look on the street and nailing it down with a proper nose manual!",
          "fault":"nope man! please, pick one of above"
        }

#printing the intro 
print "It's a beautiful sunny day. You just finished work for the week and now you"
print "can enjoy some hours of pure skateboarding!"
print "Cruising down the street you arrive near the hometown skatepark."
print "Where do you wanna go?"

#first choice, creating count and score variables
pick=raw_input("Heading to the skatepark? Press a. Keep kickin' down the street? Press b:____")
count=0
score=0

#defining the exit while code for wrong answers
while pick not in ("a","b") and count <3:
  print action["fault"]
  pick=raw_input ()
  count+=1

if count ==3:
    print "game over, dude"
    print "score: %d" % (score)
  
else:
    print action[pick]

#first round, skatepark or street    

#skatepark    
    if pick =="a":
        webbrowser.open("http://californiaskateparks.com/wp-content/uploads/2015/06/venice5473747_DSC6212skatepark.jpg")
        print "Time to catch some air dude!"
        trick02=raw_input("Down the pool, will you go for a sad air? press e. Or would you push an handlplant? Press f.____")

        while trick02 not in ("e","f") and count <3:
          print action["fault"]
          trick02=raw_input ()
          count+=1
      
        if count ==3:
          print "game over, dude"
          print "score: %d" % (score)
        else:
          print action[trick02]
      
        if trick02 == "e":
          webbrowser.open("http://www.confuzine.com/wp-content/uploads/2016/05/Pedrito-Bs-Sad-LLSP.jpg")
          score+=50
          print "score: +50"
          print ""
      
        if trick02 =="f":
          webbrowser.open("https://gonesk8ing.files.wordpress.com/2013/10/777.jpg")
          score+=100
          print "score: +100"
          print ""
          
        print "Next you head to the pool for a nasty bowl transfer! Which trick do you want to try?"
        trick03=raw_input("Backflip? Press g. Kickflip indy? Press h.____")
        
        while trick03 not in ("g","h") and count <3:
          print action["fault"]
          trick03=raw_input ()
          count+=1
      
        if count ==3:
          print "game over, dude"
          print "score: %d" % (score)
        else:
          print action[trick03]
      
        if trick03 == "g":
          webbrowser.open("https://i.ytimg.com/vi/5ydYOW_o_N4/hqdefault.jpg")
          score+=200
          print "score: +200"
          print ""
      
        if trick03 =="h":
          webbrowser.open("http://www.briansumner.net/wp-content/gallery/skate-career/39-Kick-flip-indy.jpg")
          score+=150
          print "score: +150"
          print ""


#street    
    if pick =="b":
      print "After a while you see a rad rail with a stairset."
      webbrowser.open("https://s-media-cache-ak0.pinimg.com/736x/0f/81/52/0f8152514d0ed8ef979c702ef4533d2d--nyjah-huston-skate-photos.jpg")
      print "Wanna try a trick?"
      trick01=raw_input("Easy 5050 grind? Press c. A stylish frontside feeble? Press d:____")
      
      while trick01 not in ("c","d") and count <3:
          print action["fault"]
          trick01=raw_input ()
          count+=1
      
      if count ==3:
          print "game over, dude"
          print "score: %d" % (score)
      else:
          print action[trick01]
      
      if trick01 == "c":
          webbrowser.open("http://imgur.com/rDahyFX")
          score+=150
          print "score: +150"
          print ""
      
      if trick01 =="d":
          webbrowser.open("http://pictures.boxxspring.net/pictures/600x0/76205?crop=none")
          score-=100
          print "score: -100"
          print ""
      
      print "You keep cruising the concrete jungle, just enjoying the ride."
      print "A well famous road gap is ahead of you. What do you want to try?"
      trick04=raw_input("Cleaning it with a huge ollie? Press i. Manuals it? Press j.____")
        
      while trick04 not in ("i","j") and count <3:
        print action["fault"]
        trick04=raw_input ()
        count+=1
      
      if count ==3:
        print "game over, dude"
        print "score: %d" % (score)
      else:
        print action[trick04]
      
      if trick04 == "i":
        webbrowser.open("https://goo.gl/Zr4grK")
        score+=250
        print "score: +250"
        print ""
      
      if trick04 =="j":
        webbrowser.open("https://goo.gl/h54udo")
        score+=100
        print "score: +100"
        print ""
        
#outro and final game        
        
print ""
print "The tunes stop and your iPhone warns you about an incoming calls. Sally!"
print "Damn, dude! Looks like you forget about the night out with your girlfriend!"
print "Hurry up! time to head home!"
print ""
print "She asked you for a gift. But since she's quite strange" 
print"(it's not my fault if you just like girls that way!)"
print "She tells you to go to the goldsmith and pick the ring she already liked and tryed on."
print "But you have to pick in among three boxes. You can make just one pick!"
print ""
print "Based upon the inscriptions on the boxes (none or just one of them is true), choose one box where the ring is hidden."
print ""
print "Golden box: The ring is in this box."
print "Silver box: The ring is not in this box."
print "Lead box: The ring is not in the golden box."
print ""
answer=raw_input("So in which box is the ring? Golden, silver or lead?")

if answer.lower() == "lead":
  print "Great that's it! You can go partying with your girl tonight!"
  print "You're a boss!"
  score+=500
  print "score: +500 "
  
else: 
  print "Nope....!!The ring is not here!"
  print "Good luck explaining it to your girfriend now!"
  print "Maybe you'd like to spend the night skateboarding instead than going home!"
  score-=200
  print "score: -200"

print ""
print "GAME OVER"
print "Total Score: %d" % (score)        
