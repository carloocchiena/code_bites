from random import choice

class Sprite:
    
    count = 0
    
    def __init__ (self, name, health, attack, alignment):
        self.name = name
        self.health = health
        self.attack = attack
        self.alignment = alignment
        
    def hit(self):
        return choice(range(self.attack))
    
    def damage(self, attack):
        self.count +=1
        self.health -= attack
        return self.health, self.count
    
    def alive(self):
        if self.health < 1:
            #print (f"{self.name} is dead.")
            return False
        else:
            return True
        
    def __str__(self):
        return f"{self.name} is {self.alignment} it has {self.health} life points, been hit {self.count} times"
        
imp = Sprite("Imp", 20, 10, "evil")
revenant = Sprite("Revenant", 75, 25, "evil")
cacodemon = Sprite ("Cacodemon", 20, 15, "evil")
doomguy = Sprite ("Doomguy", 50, 25, "good" )

enemy_list = [revenant, cacodemon, imp]

def play():
    
    print ("Hell on Earth")
    print (f"we have {len(enemy_list)} demons and {doomguy.name}, the proud hero.")
    print (f"{doomguy}\n")
    
    defeated_enemies = []
            
    while doomguy.alive():
        
        if len(enemy_list)  > 0:
            enemy = choice(enemy_list)
            enemy_list.remove(enemy)
            print (f"An evil {enemy.name} appears!")

            while enemy.alive():
                enemy.damage(doomguy.hit())
                print (f"{doomguy.name} hit {enemy.name}!")
                if enemy.alive() is False:
                    defeated_enemies.append(enemy.name)
                    print (f"{enemy.name} is dead!")
                    pass 
                doomguy.damage(enemy.hit())
                print (f"{enemy.name} hit {doomguy.name}!")
                if doomguy.alive() is False:
                    break 
                print (doomguy)
                print (enemy)
            else:
                if len(enemy_list) > 0:
                    enemy = choice(enemy_list)
                    enemy_list.remove(enemy)
       
        else:
            print (f"{doomguy.name}'s' won.")
            print (f"Doomguy defeated: {defeated_enemies}")
            print ("Game Over")
            break

    else:
        print (f"{doomguy.name}'s' dead.")
        print (f"Doomguy defeated: {defeated_enemies}")
        print ("Game Over")

play()
