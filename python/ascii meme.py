

#seleziono da un database di ascii meme in base allo stato d'animo
#import random function
import random

#create meme dict
arrabbiato=("┌∩┐(◣_◢)┌∩┐"," (ಠ_ಠ)┌∩┐","╭∩╮（︶︿︶）╭∩╮","┌∩┐(‿|‿)┌∩┐","┌∩┐(◟‿◞◟‿◞)┌∩┐","╭∩╮ (òÓ,) ╭∩╮",)

felice=(" (•̀ᴗ•́)و ̑̑","٩(-̮̮̃•̃) ۶ ٩(̾●̮̮̃ ̾•̃̾)۶"," (｡☉౪ ⊙｡)","✌(◕‿-)✌"," (づ｡◕‿‿◕｡)づ","(づ￣ ³￣)づ"," (｡◝‿◜｡)")

spiritoso=("(╯°□°）╯︵ ┻━┻","┬──┬ ノ( ゜-゜ノ)","ლ(ಠ益ಠლ)","つ ◕_◕ ༽つ","(ಠ_ಠ)"," [¬º-°]¬"," ( ͡° ͜ʖ ͡°)","^⨀ᴥ⨀^")

sensuale=("(. )( .)","( ๏ Y ๏ )","8=D","8=============D","({:})")

thinking=("Mmmmm...fammi provare...ecco!","Allora, aspetta un attimo che mi applico:","Dai, fammi fare un tentativo", "Cosa te ne pare come inizio?", "Scusa eh, ma sono alle prime armi!")

#intro discorsiva e scelta dello stato d'animo
print "Hey! Ciao! Oggi sono qui per farmi due risate assieme a te!"
print "Hai mai sentito parlare di ascii art?ASCII sta per American Standard Code for Information Interchange."
print "Proviamo a combinare punti, asterischi e parentesi e vediamo cosa viene fuori?"
print "Prima di tutto, dimmi un po', come ti senti oggi?"
print ""
print "Arrabbiato? Felice? Spiritoso? O forse...un po' sensuale?"
risposta=raw_input()
print""

while risposta.lower() not in ("arrabbiato", "arrabbiata", "felice", "sensuale","spiritoso","spiritosa"):
  print "Mi sa che non ho capito...puoi ripetere?"
  risposta=raw_input()      

#scelgo dalla lista in base allo stato d'animo
if risposta.lower() in ("arrabbiato","arrabbiata"):
    print random.choice(thinking)
    print ""
    print random.choice(arrabbiato)

elif  risposta.lower() == "felice":
    print random.choice(thinking)
    print ""
    print random.choice(felice) 
    
elif risposta.lower() == "spiritoso":
    print random.choice(thinking)
    print ""
    print random.choice(spiritoso)

elif risposta.lower() == "sensuale":
    print random.choice(thinking)
    print ""
    print random.choice(sensuale)  
else:
    print "Mmmmm...sono stanco, mi riposo per un po'"  
