import random

player_name = input("Hello Adventurer-what is your name?\n")

print ("\nWelcome {}. Your mission is to navigate the maze, and find and defeat the dragon at it's centre!".format(player_name))
print("""Lets determine your starting stats.\n
First, your strength and constitution will be determined at random - \
this will be the basis for your HP, attack and armour stats.""")

# def get_stats():
#     player_stats=[]
#     strength = random.randint(1,6)*5
#     constitution = random.randint(1,6)*5
#     hp = round(((strength+constitution)/2))
#     attack = round(strength /3)
#     defence = round(constitution /3) 
#     player_stats.append(strength)
#     player_stats.append(constitution)
#     player_stats.append(hp)
#     player_stats.append(attack)
#     player_stats.append(defence)
#     return player_stats

class Player():
    def __init__(self,name):
        self.name = name
    
   
        
    def get_stats(self):
        self.player_stats=[]
        self.strength = random.randint(1,6)*5
        self.constitution = random.randint(1,6)*5
        self.maxhp = round(((self.strength+self.constitution)/2))
        self.hp = round(((self.strength+self.constitution)/2))
        self.attack = round(self.strength /3)
        self.defence = round(self.constitution /3) 
        self.player_stats.append(self.strength)
        self.player_stats.append(self.constitution)
        self.player_stats.append(self.hp)
        self.player_stats.append(self.attack)
        self.player_stats.append(self.defence)
        self.potion = 0
      #  return self.player_stats
    
    def __repr__(self):
        description = "\nYou have a strength of {s} and a constitution of {c}. You have {hp} current HP, \
with a maximum of {maxhp} HP. You have a +{a} attack bonus, and a +{d} defence bonus "\
.format(s=self.strength, c=self.constitution, hp=self.hp, maxhp=self.maxhp, a=self.attack, d=self.defence)
        return description

    
    def upgrade_attack(self,amount):
        self.attack += amount
            
    def upgrade_defence(self,amount):
        self.defence += amount
        
    def heal(self,amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print("You have healed for {heal} hp. You now have {hp} left.".format(heal=amount,hp=self.hp))
    
    def take_damage(self,amount):
        self.hp -= amount
        if self.hp <= 0:
            print ("Sorry, you have been defeated by the dragon! Try again!")
        print("You have been hit for {damage} damage. You have {hp} hp left.".format(damage=amount,hp=self.hp))
        
    def gain_potion(self):
        self.potion += 1
        
    def use_potion(self):
        self.potion -= 1
        print("You use your health potion.")
    


#Get player stats - STR, CON, HP, attack & AC
player = Player(player_name)
player.get_stats()


print(player)

#print(player_stats)
# print("\nYou have a strength of {s} and a constitution of {c}. You have {hp} current HP, with a maximum of {maxhp} HP. \
# You have a +{a} attack bonus, and a +{d} defence bonus "\
#       .format(s=player_stats[0],c=player_stats[1],hp=player_stats[2],maxhp=player_stats[2],a=player_stats[3],d=player_stats[4]))
#initialise inventory = keys & health potions
player_inventory = []
#
#DRAGONS STATS(STR, CON, HP, attack, AC)
dragon_stats = [15,24,25,5,8]


    
print("\nGreat job, {name}! Let's enter the maze. There may be some things in here you can find which will help you fight the dragon!".format(name=player_name))



#The maze 
def direction1():
    direction = input("You enter the maze and come to a junction. Do you turn left or right?\n")
    while direction != "left" and direction != "right":
        direction = input ("You must type left or right!\n")
    if direction == "left":
        direction5a()
    if direction == 'right':
        direction2a()

def direction2a():
    direction = input("You walk along, turn left and continue along. You come to a path \
that branches off to the left. Do you carry on forward or turn left?\n")
    
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
        
    if direction == "left":
        print ("\nYou travel down a narrow path.\
It looks like a dead end! You search around and find a key. You pocket the key - it might come in useful later.\
You turn around and head back to the junction, and go forwards instead.")
        
        if "key1" not in player_inventory:
            player_inventory.append("key1")
        direction3a()
        
    if direction == "forward":
            direction3a()


def direction3a():
    direction = input("\nYou walk along and come to a path that branches off to the left.\
Do you carry on forward or turn left?\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        direction4a()
    if direction == "forward":
        direction4b()
        
def direction4a():
    direction = input("\nYou turn left and after a while the path turns left again.\
You think you can hear a faint hum coming from in front of you. You can turn right, or continue forward.\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction == "right":
        print("\nYou turn away from the humming noise, and continue along the path. The path turns right\
and then immediately left. You see what you think is a pile of clutter in the corner, but on\
closer inspection you see that it has a useful shield you can use!")
        if "armour1" not in player_inventory:
            player_inventory.append("armour1")
            player.upgrade_defence(1)
            direction5a()
    if direction == "forward":
        print("\nThe hum gets louder as you continue and turn right. You find a locked chest.")
        if "key1" in player_inventory:
            print("\nYou notice that the symbol on the chest matches a key you found earlier! You unlock the\
chest to find a razor-sharp sword. This will definitely help you later!")
            if "chest1" not in player_inventory:
                player_inventory.append("chest1")
                player.upgrade_attack(3)
        else:
            print("\nTry as you might, you cannot open the chest! If only there was a key somewhere...")
        print("You carry on past the chest. The path turns left. You see what you think is a pile of \
clutter in the corner, but on closer inspection you see that it has a useful shield you can use!")
        if "armour1" not in player_inventory:
            player_inventory.append("armour1")
            player.upgrade_defence(1)
        direction5a()

    
def direction4b():
    direction = input("\nYou walk further along and come to a small path that branches off to the left.\
Do you carry on forward or turn left?\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        print ("\nYou travel down a narrow path.\
It looks like a dead end! You search around and find a health potion! You pocket the potion - it might come in useful later.\
You turn around and head back to the junction, and go forwards instead.\n") 
        if "potion1" not in player_inventory:
            player_inventory.append("potion1")
            player.gain_potion()             
        direction5b()
    if direction == "forward":
        direction5b()
        
def direction5a():
    direction = input("\nYou reach a T-junction. You can see the maze entrance to your left, so turn right.\
 There is a path to your right you can take, or you can continue forwards.\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction == "right":
        direction6c()
    if direction == "forward":
        direction6d()
        
def direction5b():
    direction = input("\nYou carry on down the path for a short while. A large pathway splits off to the left.\
Do you turn left or carry on forward?\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        direction6a()
    if direction == "forward":
        direction6b()
        
def direction6a():
    direction = input("\nYou turn left and continue down the path. You take a left turn and can \
either turn right or continue forwards.\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="forward":
        direction1 = input("\nYou continue onwards, and follow the path around to the right. You reach a junction where you can\
 turn right or continue on. There is an electric-type energy coming from the small passage way forwards.")
        direction1 = input("\n You can choose to go forward or right.")
        while direction1 != "right" and direction1 != "forward":
            direction1 = input ("You must type left or forward!\n")
        if direction1 == "forward":
            direction7c()
        if direction1 == "right":
            direction7d()
    if direction =="right":
        direction7d()
            
def direction6b():
    direction = input("\nYou keep walking down the path for a while. A strange, sweet smell is eminating from a pathway\
off to the left. Do you turn left or keep on going forwards?\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        print ("\nYou travel towards the smell.\
You find a small bottle containing a glowing liquid with a label that says 'HEALTH' on it.\
You pocket the potion - it might come in useful later.\
You keep travelling down the pathway. It turns to the left, and then to the right.")
        if "potion3" not in player_inventory:
            player_inventory.append("potion3")
            player.gain_potion()

        direction7a()
    if direction == "forward":
        print("\nYou decide to resist the sweet smell and continue down th path. It turns to the left.")
        direction7b()
        
def direction6c():
    direction = input("\nTurning right, you continue along. You reach a narrow passage way on your left. \
There is an electric energy coming from here- choose to investigate it further or continue forward.\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        direction7c()
    if direction =="forward":
        direction7d()
    
def direction6d():
    direction = input("\nWould you like to turn right, or carry on straight ahead?\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="right":
        direction7e()
    if direction == "forward":
        direction7f()
        
def direction7a():
    direction = input("\nDecide whether to keep following the path forward, or change direction\
 and take the path on the right\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="forward":
        direction8a()
    if direction == "right":
        direction7b()
        
def direction7b():
    print("\nThe path continues onwards")
    direction8b()
    
def direction7c():
    print("\nYou squeeze down the passage way, and come into the middle of a long corridor. Down the right end \
of the corridor you find a vial of liquid on a plinth, labelled 'health'. You take it, thinking it could help you later.\n")
    if "potion2" not in player_inventory:
        player_inventory.append("potion2")
        player.gain_potion()
    print("At the other end of the corridor you find a sword in a stone.\n")
    if player.strength >= 10:
        print("You pull with all your strength, and the sword comes loose! You take it, knowing that this will \
really help you in the upcoming battle\n")
        if "attack1" not in player_inventory:
            player.upgrade_attack(2)
            player_inventory.append("attack1")
    else:
        print("You pull with all your strength, but the sword just doesn't budge. You should bulk up more!\n")
    print("You turn back, and choose the other direction.\n")
    direction7d()
        
def direction7d():
    direction = input ("\nYou reach a junction. There is a signpost pointing in one direction, which says 'NORTH'\
and another in the other direction saying 'WEST'. Which way do you go?\n")
    while direction != "north" and direction != "west":
        direction = input ("You must type north or west!\n")
    if direction =="north":
        direction9a()
    if direction =="west":
        direction9b()
        
def direction7e():
    direction = input ("\nYou reach a junction. There is a signpost pointing in one direction, which says 'NORTH'\
and another in the other direction saying 'WEST'. Which way do you go?\n")
    while direction != "north" and direction != "west":
        direction = input ("You must type north or west!\n")
    if direction == "north":
        print("\nYou travel onwards, and turn a corner.")
        direction9b()
    if direction == "west":
        direction8c()
        
    
    
def direction7f():
    direction = input ("\nYou reach a junction. There are two signposts pointing 'NORTH' and 'WEST'.\
 Which way do you go?\n")
    while direction != "north" and direction != "west":
        direction = input ("You must type north or west!\n")
    if direction == "north":
        direction8d()
    if direction == "west":
        print("\nYou travel onwards and turn right.")
        direction8e()
    
    
    
    
def direction8a():
    direction = input ("\nYou choose to carry on and the path twists and turns until you come to the end. You are \
able to see a faint glow off to the right. Choose to investigate the glow to the right, or turn left.\n")
    while direction != "right" and direction != "left":
        direction = input ("You must type right or left!\n")
    if direction =="right":
        direction8b()
    if direction =="left":
        direction9a()
        
def direction8b():
   
    if ("key3") not in player_inventory:
        print("\nYou can see a faint glow, which gets brighter the further along you walk, and you find a small glowing key. \
You put the key in your pocket.")
        player_inventory.append("key3")
    direction = input("\nThe key in your pocket feels hotter when you look down the corridor to the south. Do you \
continue on forwards ignoring the key, or turn down the south corridor?\n")
    while direction != "forward" and direction != "south":
        direction = input ("You must type forward or south!\n")
    if direction =="south":
        direction9a()
    if direction =="forward":
        direction9c()

def direction8c():
    direction = input("\nA short time later you find yourself at a T-junction. You can turn left or right.N")
    while direction != "right" and direction != "left":
        direction = input ("You must type right or left!\n")
    if direction == "left":
        direction9d()
    if direction == "right":
        print("You happen upon a chest which has a faint tune eminating from it.")
        if "key2" in player_inventory:
            print("\nYou recognise the tune to be the same as a key you have! You place the key in the lock and it clicks \
 open, the chest and key now singing in perfect harmony. Inside the chest is a vial of poison with a dragon on it...\
 dragon poison? That sure will be useful!")
            if ("chest2") not in player_inventory:
                dragon_stats[4]-=3
                player_inventory.append("chest2")
        else:
            print("You cannot open the chest without the macthing key!")
        direction9e()
        
def direction8d():
    direction = input("\n You travel along the path until you reach a junction. You can see something glinting \
down the path to your left. Do you take the left path or continue forward?\n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "left":
        if ("armour2") not in player_inventory:
            player_inventory.append("armour2")
            print("\nYou find a steel helm which luckily is the perfect for for your head! You put it on and feel \
more protected already!")
            player.upgrade_defence(1)
        direction1 = input("\nDo you want to turn around and continue on the other way, or continue forward on this path?\n")
        while direction1 != "turn" and direction1 != "forward":
            direction1 = input ("You must type turn or forward!\n")
        if direction1 == "turn": 
            direction9g()
        if direction1 == "forward":
            direction9f()
            
def direction8e():
    direction = input("\n You travel along the path until you reach a junction. You can see something glinting \
down the path to your right. Do you take the left path or continue forward?\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="right":
        if ("armour2") not in player_inventory:
            player_inventory.append("armour2")
            print("\nYou find a steel helm which luckily is the perfect for for your head! You put it on and feel \
more protected already!")
            player.upgrade_defence(1)
        direction9f()
    if direction == "forward":
        direction9f()       
   
    

def direction9a():
    if "key3" in player_inventory:
        print("\nThe key in your pocket gets hotter and hotter, and it leads you down a small dead end alley way. \
At the bottom of the path is a locked chest which is glowing. You take the hot key and open the chest.\
Inside is a potion of fortitude which gives you a boost to you HP!\n")
        if "chest3" not in player_inventory:
            player.maxhp += 3
            player.heal(3)
            player_inventory.append("chest3")
        direction = input("\nYou can choose to go left and go back to where you were before \
and continue, or can go right.\n")
        while direction != "right" and direction != "left":
            direction = input ("You must type right or left!\n")
        if direction == "left":
            direction9c()
        if direction =="right":
            direction9b()
        
    else:
        print("\nYou see a little dead end passage way. At the bottom of the path is a locked chest which is glowing.\
 You try desperately to open the chest, but cannot. Maybe a key would have been useful here!")
        direction = input("\nYou can choose to go right and go back to where you were before \
and continue, or can go left.\n")
        while direction != "right" and direction != "left":
            direction = input ("You must type right or left!\n")
        if direction == "left":
            direction8b()
        if direction =="right":
            direction9b()
            
def direction9b():
    direction = input("\n You travel along the corridor. You have a chouce whether to carry straight on forward \
or turn right. Do you take the right path or continue forward?\n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction == "forward":
        direction8c()
    if direction == "right":
        direction10a()
        
def direction9c():
    direction = input("\n Continuuing on, you feel a warm energy coming from the path off to the left. \
Do you carry on forwards, ignoring the energy, or find out what it is down the left path? \n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction == "forward":
        direction10b()
    if direction == "left":
        direction10c()
        
def direction9d():
    direction = input("\n Ahead of you, you hear a faint song. You can follow the song or turn right and ignore it. \n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="forward":
        if ("key2") not in player_inventory:
            print("You find a tiny key from which the song is coming from! You take the key .")
            player_inventory.append("key2")
            if "chest2" not in player_inventory: 
                print("It's a dead end, so you turn around and take the other direction. On this path the key pulls\
you towards a hidden passage way. You see a chest, eminating a similar sound to the key.\ You place the key in the lock \
and it clicks open, the chest and key now singing in perfect harmony.\
Inside the chest is a vial of poison with a dragon on it...dragon poison? That sure will be useful!")
                player_inventory.append("chest2")
                dragon_stats[4]-=3
                player_inventory.append("chest2")
                print("You continue onwards.")
                dragon()
            else:
                print("You continue onwards.")
                dragon()
                                
    if direction =="right":
                dragon()




def direction9e():
    if "chest2" not in player_inventory:
        direction = input("\n You travel onwards and reach a T-junction. To he left you can hear a faint tune, \
similar to the one you just head, but slightly different. Do you tun left to the song, or turn right? \n")
        while direction != "right" and direction != "left":
            direction = input ("You must type right or left!\n")
        if direction =="left":
            print("You find a tiny key from which the song is coming from! You recognise the tune to be the same as \
the one you heard earlier! You return, place the key in the lock and it clicks open, the chest and key now singing \
in perfect harmony.\
Inside the chest is a vial of poison with a dragon on it...dragon poison? That sure will be useful!")
            player_inventory.append("key2")
            dragon_stats[4]-=3
            player_inventory.append("chest2")
            print("You continue onwards and take the other direction.")
            dragon()
        if direction =="right":
            dragon()
    else:
        print("You continue onwards.")
        dragon()
            
def direction9f():
    direction = input("\n Do you go forwards to turn right? \n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction == "forward":
        direction10d()
    if direction =="right":
        direction9g()
        
def direction9g():
    if "potion4" not in player_inventory:
        print("You find a small health potion!")
        player_inventory.append("potion4")
        player.gain_potion()
        dragon()
    else:
        dragon()
    
        
def direction10a():
    direction = input("\n You quickly reach a point where you need to choose to pick to carry on forward, towards \
a weird energy, or turn right towards a quiet tune?  \n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="forward":
        direction10c()
    if direction =="right":
        print("You happen upon a chest which has a faint tune eminating from it.")
        if "key2" in player_inventory:
            print("\nYou recognise the tune to be the same as a key you have! You place the key in the lock and it clicks\
 open, the chest and key now singing in perfect harmony.\
 Inside the chest is a vial of poison with a dragon on it...dragon poison? That sure will be useful!")
            if ("chest2") not in player_inventory:
                dragon_stats[4]-=3
                player_inventory.append("chest2")
        else:
            print("You cannot open the chest without the macthing key!")
        direction9e()
    
def direction10b():
    direction = input("\n Do you carry on forward or turn right? \n")
    while direction != "right" and direction != "forward":
        direction = input ("You must type right or forward!\n")
    if direction =="right":
        direction11a()
    if direction == "forward":
        print("You travel onwards and see a snall dead-end path off to the left. You look down and see something shiny.\
 You find a breast plate that seems to fit you perfectly. You feel more protected already.")
        player_inventory.append("armour3")
        player.upgrade_defence(2)
        direction11b()
        

def direction10c():
    if "attack2" in player_inventory:
        direction11a()
    else:
        if "attack1" not in player_inventory and "chest1" not in player_inventory:
            print("The energy leads you to a glistening long sword, propped up against the wall. You take it, knowing \
such a weapon will definitely be useful.")
            player.upgrade_attack(2)
            player_inventory.append("attack2")
            direction11a()
        else:
            print("You find a circular stone from which the energy is coming from. You feel like it is the perfect \
shape to sharpen your sword on. You sharpen your sword to a razor edge. This thing could cut anything now!")
            player.upgrade_attack(1)
            player_inventory.append("attack2")
            direction11a()


def direction10d():
    if "potion5" not in player_inventory:
        print("The path winds around to the left and you find a small flask with a glowing liquid in it labelled 'HEALTH'. \
You pocket it and carry on your way.") 
        player_inventory.append("potion5")
        player.gain_potion()
    if "attack3" not in player_inventory:
        print("You turn left and find a beautiful bracelet. You out it on and immediatley feel more powerful, like \
there is a much lower chance of missing an attack!")
        player.upgrade_attack(1)
        player_inventory.append("attack3")
        dragon()
    else:
        dragon()
        

              
            

def direction11a():
    dragon()
    
def direction11b():
    direction = input("\n Do you carry on forward or turn left? \n")
    while direction != "left" and direction != "forward":
        direction = input ("You must type left or forward!\n")
    if direction =="left":
        if "attack3" not in player_inventory:
            print("You turn left and find a beautiful bracelet. You out it on and immediatley feel more powerful, like \
there is a much lower chance of missing an attack!")
            player.upgrade_attack(1)
            player_inventory.append("attack3")
            dragon()
        else:
            dragon()
     
    if direction == "forward":
        print("You walk along the path for a while, taking a few twists and turns along the way.")
        direction10d() 
    

def dragon():
    
    print("You walk onwards and you hear a strange rumbling getting louder. You can also feel the air getting hotter \
around you. You turn the corner and you see a terrifying, giant dragon! \
You ready yourself.")
    dragon1()
    
def dragon1():
    player.get_stats
    choice=input("\nDo you wish to attack or heal? \n")
    while choice != "attack" and choice != "heal":
        choice = input ("You must type attack or heal!\n")
    if choice == "heal":
        player_heal()
    if choice =="attack":
        player_attack()
        
def player_heal():
    if player.potion > 0:
        player.use_potion()
        player.heal(5)
        dragon_turn()
    else:
        print("You are all out of health potions! Attack it is!")
        player_attack()
            
def player_attack():            
    if player.attack > dragon_stats[4]:
        print("You hit the dragon well!")
        dragon_stats[2] -= player.attack
        if dragon_stats[2] <= 0:
            win()
        else:
            dragon_turn()
    else:
        print("You hit the dragon, but you feel like you're not strong enough to do full damage.")
        dragon_stats[2] -= round(player.attack/2)
        if dragon_stats[2] <= 0:
            win()
        else:
            dragon_turn()
            
def dragon_turn():
    print("The dragon rears up to attack you.")
    if dragon_stats[3] > player.defence:
        print("You're not strong enough to defend yourself fully and take a lot of damage!")
        player.take_damage(dragon_stats[3])
    else:
        print("You do a good job of defending yourself!")
        player.take_damage(round(dragon_stats[3]/2))
    if player.hp <= 0:
        lose()
    dragon1()
                

def win():
    print("Congratulations! You have defeated the dragon!")
    
def lose():
    print("Better luck next time!!")





  
direction1()  



    

    
       