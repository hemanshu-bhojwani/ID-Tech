import pyglet

morality = 0
cash = 200.0

import random, time

import pyglet
song = pyglet.media.load('intro.wav')
song.play()


print("Hello")
print("Welcome to the adventure")
print("Enter your player name")
name = input("What is your name?")
print("Your name is",name,"yes or no")
choice = input("Yes or No?")

if choice.lower() == "no":
    print("Please type your name in again")
    name = input()
    print("Welcome to the adventure")

elif choice.lower() == "yes":
    print("welcome to the adventure")

else:
    print("Please type your name again")
    name =  input("What is your name")


print("Choose your enemys name")

enemyName = input("What is your enemy's name?")

print("")
print("Hi ",name," my name is Bob and I am going to show you around the town of springfield.")
e=input()
print("This world is usually a place of happiness and prosperity but lately the evil wizard ",enemyName," has come and attacked the world")
e=input()
print("This town is the last surviving outpost that has not been taken over by the wizard")
e=input()
print("right in front of you is a monster that has been created by ",enemyName)
e=input()
print("This monster has 50 health and you have 200")
e=input()
print("you must kill the monster before it kills you")

song = pyglet.media.load('final.wav')
song.play()

player_health = 200
class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self):
        time.sleep(1)
        print ("what move would you like to make? (punch, kick or poke?)")
        print("")

        answer = input()



        if answer == "punch" or answer == "Punch":
            self.health -= (random.randint(20,30)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "kick" or answer == "Kick":
            self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "poke" or answer == "Poke":
            self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        else:
                print ("Try again, What move would you like to make? (punch, kick or poke?)")
                print("")
                answer = input()

                if answer == "punch" or answer == "Punch":
                    self.health -= (random.randint(5,30)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "kick" or answer == "Kick":
                    self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "poke" or answer == "Poke":
                    self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)

                else:
                    print ("Too Bad!")
                    print ("")


        time.sleep(1)

        print (self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global player_health
        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        player_health = player_health - (self.strength * random.uniform(0.1, 1.4))
        player_health = int(player_health)
        time.sleep(1)
        print ("Your health is now " + str(int(player_health)))
        print ("")
        return int(player_health)

    def battle_script(self):
        global player_health
        print ("An enemy " + self.name + " appears...")
        print ("")
        time.sleep(1)
        while player_health > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <=0:
               break
            self.enemy_attack()
            if player_health <=0:
                break
        if self.health <= 0:
            time.sleep(1)
            song = pyglet.media.load('win.wav')
            song.play()

            print ("You have killed the " + self.name)

        if player_health <= 0:
            time.sleep(1)
            song = pyglet.media.load('gameend.wav')
            song.play()
            print ("Sorry, you are dead")
            print ("Game Over!!!")
            exit()


enemies = [Enemy("Bear", 10, 5, 20), Enemy("Wolf", 20, 10, 20), Enemy("Lion", 30, 20, 20), Enemy ("Dragon", 40, 30, 25)]

random_enemy = random.choice(enemies)
random_enemy.battle_script()

print("Congratulations! you just killed a monster")
e=input()
print("Bob takes you to a blacksmith")
e=input()
print("You can pick between a bow and a sword")
e=input()
print("which weapon would you like?")
weapon = input("which weapon would you like?")
print("Bob decides to take you to his house so you can stay the night there.")
e=input()
print("Bob tells you that you are the chosen one and explains what that means")
e=input()
print("You see two chests and you feel that you want to loot the box because it could contain something very awesome.")
e=input()
print("Do you want to loot the Chests or not")

chest = input("would you like to loot the boxes? yes or no?")

if chest.lower() == "no":
    print("you leave the house")
    morality += 25
else:
    print("The chests were empty.... you have become more evil")
    print("you leave the house")
    morality -= 50
print("your morality is ",morality)
e=input()
print("if your morality is in the negatives, you are evil")
e=input()
print("if your morality is in the positives, you are good")
e=input()
print("after leaving your house you meet up with bob at the training academy")
e=input()
print("Bob shows you around and starts training")
e=input()
print("a few months later, you become a master at dueling with weapons")
e=input()
print("you leave the training academy with your",weapon)
e=input()
print("And begin a journey to a sacred temple that is very heavily guarded by some of the most powerful soldiers.")
e=input()
print("inside the temple is a totem that was used thousands of years ago to defeat the wizard ")
e=input()
print("The journey is very long so you get a lot of food for the journey")
e=input()
print("To reach the temple you must go through many different areas.")
e=input()
print("Your first obstacle is going through a forest that is said to be filled with many of",enemyName,"'s minions")


import random, time
from random import randint

player_health = 200

song = pyglet.media.load('final.wav')
song.play()


class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self):
        time.sleep(1)
        print ("what move would you like to make? (punch, kick, poke, shoot or slash?)")
        print("")

        answer = input()

        from random import randint


        if answer == "punch" or answer == "Punch":
            self.health -= (random.randint(5,30)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "kick" or answer == "Kick":
            self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "poke" or answer == "Poke":
            self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "shoot" or answer == "Shoot":
            self.health -=   (random.randint(20,60)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "slash" or answer == "Slash":
            self.health -=   (random.randint(35,90)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        else:
                print ("Try again, What move would you like to make? (punch, kick, poke, shoot or slash?)")
                print("")
                answer = input()

                if answer == "punch" or answer == "Punch":
                    self.health -= (random.randint(5,30)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "kick" or answer == "Kick":
                    self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "poke" or answer == "Poke":
                    self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "shoot" or answer == "Shoot":
                    self.health -=   (random.randint(20,60)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "slash" or answer == "Slash":
                    self.health -=   (random.randint(35,90)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)

                else:
                    print ("Too Bad!")
                    print ("")




        time.sleep(1)

        print (self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global player_health
        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        player_health = player_health - (self.strength * random.uniform(0.1, 1.4))
        player_health = int(player_health)
        time.sleep(1)
        print ("Your health is now " + str(int(player_health)))
        print ("")
        return int(player_health)

    def battle_script(self):
        global player_health
        print ("An enemy " + self.name + " appears...")
        print ("")
        time.sleep(1)
        while player_health > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <=0:
               break
            self.enemy_attack()
            if player_health <=0:
                break
        if self.health <= 0:
            time.sleep(1)
            print ("You have killed the " + self.name)
            song = pyglet.media.load('win.wav')
            song.play()

        if player_health <= 0:
            time.sleep(1)
            song = pyglet.media.load('gameend.wav')
            song.play()
            print ("Sorry, you are dead")
            print ("Game Over!!!")
            exit()


enemies = [Enemy("Monkey", 10, 5, 100.), Enemy("Giant Lizard", 20, 10, 100), Enemy("Big Snake", 30, 20, 100), Enemy]
thisEnemy = Enemy("Overgrown human",10,30,120)
thisEnemy.battle_script()
random_enemy = random.choice(enemies)
random_enemy.battle_script()

print("Congratulations!")
e=input()
print("Now we can move on")
e=input()
print("Look! up ahead is a temple")
e=input()
print("would you like to enter the temple?")
choice = input("Would you like to enter?")

if choice.lower() == "yes":
    print("You have entered the temple")
    print("would you like to go left or right?")
    choice = input("choose left or right one leads to death while the other leads to cash")

    if choice.lower() == "right":
        print("You entered the treasure room and got $800")
        cash += 800
        print("You have $",cash,"now")
        print("You have left the table")
    else:
        exit()

if choice.lower() == "no":
    print("You ignore the temple")


print("You find a village and ask to stay for the night")
e=input()
print("would you like to stay? If you do it will cost $100")

choice = input("It costs $100 to stay the night. do you want to stay? Yes or No?")

if choice.lower() =="yes":
    print("you pay $100")
    cash -= 100
    print("you now have $",cash)
    e=input()
    print("you leave the village in the morning and find some people fighting some monsters")

elif choice.lower() == "no":
    print("You sleep in the middle of the forest")
    print("you wake up in the morning in the middle of a fight between people and monsters")


choice = input("do you help them? Yes or No?")

if choice.lower() == "yes":
    morality += 30
    print("They survive")
else:
    print("The humans died and the monsters became more powerful")

print("Your morality is",morality)
e=input()
print("While you are walking through the forest you hear an arrow and it nearly misses your head.")
e=input()
print("you quickly look at where the arrow came from")
e=input()
print("You see a man with a mask looking straight at you.")
e=input()
print("With all of your training you quickly remove your",weapon,"and hit him with it")
e=input()
print("On the floor, he asks you to kill him")
print("would you kill him?")
e=input()

choice = input("would you kill him or not?")

if choice.lower() == "don't kill him" or "not to kill him" or "do not kill him":
    print("He joins you on your quest to the temple")
    e=input()
    print("Because you saved him, he gave you a special",weapon)
    e=input()
    print("This",weapon,"is of an ancient kind and contains special powers")
    e=input()
    morality += 60

elif choice.lower() == "kill him" or "kill":
    print("you kill him and you become more evil")
    e=input()
    morality -= 50
    print("You have the choice to loot his body would you like to?")

    choice = input("Would you like to loot his body?")

    if choice.lower() == "loot" or "loot his body":
        print("You find nothing but maps and an old sword... You become more evil")
        morality -= 90

    elif choice == "do not loot" or "don't loot":
        print("You ignore his body and go away")
        morality += 15

print("Your morality is now",morality)


print("You leave the forest and climb up a mountain.")
e=input()
print("This mountain was once climbed by the ancient one to place the idol in a safe place away from all doom until the day came")
e=input()
print("when the wizard returned")
e=input()
print("After a long hike you eventually find the temple.. You enter")
e=input()
print("You see two doors, would you like to go left or right?")

choice = input("Left or Right?")

if choice.lower() =="right":
    print("You are lead into a trap full of arrows")
    e=input()
    print("The arrows hit you hit you on your legs  and chest ... you fall to the ground ")
    e=input()
    print("GAME OVER!")
    song = pyglet.media.load('gameend.wav')
    song.play()
    e=input()
    exit()

elif choice.lower() =="left":
    print("You enter a large room with the idol on a pedestal in the middle of the room")
    e=input()
    print("You go to the middle and pick up the idol")
    e=input()
    print("You hear someone at the door and you turn around")
    e=input()
    print("You see a tall man wearing a robe")

e=input()

print("It's the wizard you whisper to yourself")
e=input()
print("You look at the idol and point it at the wizard")
e=input()
print("nothing happened")
e=input()
print("You inspect the idol and find a small opening where your",weapon,"can fit")
e=input()
print("You stick your",weapon,"inside and when you remove it you see that it has a sacred glow")
e=input()
print("Being very scared, you throw the",weapon,"at the wizard and nothing happens")
e=input()
print("The wizard has a shield around him that blocked the attack")

import random, time
from random import randint

player_health = 500

class Enemy:

    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def attack_enemy(self):
        time.sleep(1)
        print ("what move would you like to make? (punch, kick, poke, shoot or slash?)")
        print("")

        answer = input()

        from random import randint


        if answer == "punch" or answer == "Punch":
            self.health -= (random.randint(5,30)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "kick" or answer == "Kick":
            self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "poke" or answer == "Poke":
            self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "shoot" or answer == "Shoot":
            self.health -=   (random.randint(50,100)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        elif answer == "slash" or answer == "Slash":
            self.health -=   (random.randint(50,120)/(random.uniform(0,1)* self.defense))
            self.health = int(self.health)
        else:
                print ("Try again, What move would you like to make? (punch, kick, poke, shoot or slash?)")
                print("")
                answer = input()

                if answer == "punch" or answer == "Punch":
                    self.health -= (random.randint(5,30)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "kick" or answer == "Kick":
                    self.health -= (random.randint(10,40)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "poke" or answer == "Poke":
                    self.health -=   (random.randint(5,10)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "shoot" or answer == "Shoot":
                    self.health -=   (random.randint(50,100)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)
                elif answer == "slash" or answer == "Slash":
                    self.health -=   (random.randint(50,120)/(random.uniform(0,1)* self.defense))
                    self.health = int(self.health)

                else:
                    print ("Too Bad!")
                    print ("")




        time.sleep(1)

        print (self.name + "'s health is now: " + str(int(self.health)))
        print("")

        return int(self.health)

    def enemy_attack(self):
        global player_health
        time.sleep(1)
        print ("The enemy " + self.name + " " + "attacks...")
        print("")
        player_health = player_health - (self.strength * random.uniform(0.1, 1.4))
        player_health = int(player_health)
        time.sleep(1)
        print ("Your health is now " + str(int(player_health)))
        print ("")
        return int(player_health)

    def battle_script(self):
        global player_health
        print ("An enemy " + self.name + " appears...")
        print ("")
        time.sleep(1)
        while player_health > 0 and self.health > 0:
            self.attack_enemy()
            if self.health <=0:
               break
            self.enemy_attack()
            if player_health <=0:
                break
        if self.health <= 0:
            time.sleep(1)
            print ("You have killed the " + self.name)

        if player_health <= 0:
            time.sleep(1)
            print ("Sorry, you are dead")
            print ("Game Over!!!")
            exit


enemies = [Enemy(enemyName, 20, 30, 250)]

random_enemy = random.choice(enemies)
random_enemy.battle_script()




if morality > 0:
    print("You quickly run to cover as he starts to attack you")
    e=input()
    print("You find bones right next to you and you find a bow and arrow")
    e=input()
    print("You put the arrow in the idol and enchant it")
    e=input()
    print("You shoot the arrow and a small open spot in the shield and you hit the wizard")
    e=input()
    print("The wizard was banished to the underworld and will never return")
    e=input()
    print("The story of your journey will forever be remembered and told for generations")
    e=input()
    print("You won the good way")
    e=input()
    print("GAME OVER")
    song = pyglet.media.load('win.wav')
    song.play()
    e=input()
    exit()


elif morality == 0:
    if weapon.lower() == "sword":
        print("You make one final push at the wizards")
        e=input()
        print("He prepares to defend and block against you killing you")
        e=input()
        print("You reach him before he is done casting his spell and stab him")
        e=input()
        print("The enchantment on thee sword allows it to instantly kill the wizard")
        e=input()
        print("After he dies you see all of his monsters disappear")
        e=input()
        print("Peace has been restored to the earth")
        e=input()
        print("Or at least for now")
        e=input()
        print("GAME OVER!")
        song = pyglet.media.load('win.wav')
        song.play()
        e=input()
        exit()
    else:
        print("You have one arrow left and aim it at the wizard")
        e=input()
        print("You shoot and it lands dead center on the wizard hearts")
        e=input()
        print("It kills him in one hit and all his monsters disappear")
        e=input()
        print("Peace has been restored to the earth")
        e=input()
        print("Or at least for now")
        e=input()
        print("GAME OVER!")
        song = pyglet.media.load('gameend.wav')
        song.play()
        e=input()
        exit()

elif morality < 0:
    print("You join the wizard and take over the world")
    e=input()
    print("You will forever be remembered as an evil man that helped the wizard take over the world")
    e=input()
    print("You failed your journey")
    e=input()
    print("GAME OVER")
    song = pyglet.media.load('gameend.wav')
    song.play()
    e=input()
    exit()




