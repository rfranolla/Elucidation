#######################################################################
#                                                                     #
#  This code is Copyright 2018, Riley Franolla, All rights reserved.  #
#                                                                     #
#######################################################################


from time import sleep
import sys
import random

##############################################################################################################
#																											 #
#									    CLASS FOR THE GAME WORLD				     						 #
#																											 #
##############################################################################################################
class Player:
	#Initialize the class
	def __init__(self, location, inventory, health):
		self.location = location
		self.inventory = inventory
		self.health = health
		
class Room:
	#Initialize the class
	def __init__(self, shortdescription, description, open, north, east, south, west, up, down):
		self.shortdescription = shortdescription
		self.description = description
		self.open = open
		self.north = north
		self.east = east
		self.south = south
		self.west = west
		self.up = up
		self.down = down
		
class Item:
	#Initialize the class
	def __init__(self, name, description, location, moveable, available, state):
		self.name = name
		self.description = description
		self.location = location
		self.moveable = moveable
		self.available = available
		self.state = state
		
class Person:
	#Initialize the class
	def __init__(self, name, description, location, statement, response):
		self.name = name
		self.description = description
		self.location = location
		self.statement = statement
		self.response = response
		
		
class Enemy:
	#Initialize the class
	def __init__(self, name, description, location, health, hitrate, damage):
		self.name = name
		self.description = description
		self.location = location
		self.health = health
		self.hitrate = hitrate
		self.damage = damage
		
##############################################################################################################
#																											 #
#										   HELPER FUNCTIONS						     						 #
#																											 #
##############################################################################################################
def slowprint(string):
	count = 0
	for char in string:
		if count > 80 and char == ' ':
			print(char)
			count = 1
		else:
			print(char, end = "", flush = True)
			count+=1
		sleep(0.01)
	print()
	
def combat(enemy, gameData):
	if enemy.name == "Daniel Smith":
		slowprint("As you walk into the room your brother stares to look who as enter but is taken back when he sees your face. ")
		slowprint("'How' he asks and you take the time to explain how your from the future. ")
		slowprint("While talking you are looking around the room and finially put together why you came here. ")
		slowprint("Your brother is going to blow up the New York City encloser, killing everyone inside as they will be exposed to the smog. ")
		slowprint("You pause to look at him, 'Why?' you ask as you gesture around the room. ")
		slowprint("'Because New York doesn't deserve it, the keep it for themselves, not sharing it with the world. Boston showed me why they really are, and now I must stop them. ")
		slowprint("You say that you can't let him do this, how you can't just sit back and watch him kill millions of innocent people. ")
		slowprint("He doesn't care about them and says he isn't not afraid to kill you to carry out his mission. ")
		slowprint("It's up to you now to but an end to all of this. ")
		
	else:
		slowprint("You see standing before you ready to fight, ")
		slowprint(enemy.name + ". " + enemy.description)
	
	
	while enemy.health > 0 and gameData["player"].health > 0:
		text(gameData)
		
		dodge = False
		for word in gameData["text"]:
			# HANDLE PLAYER REGULAR ATTACK
			if word == "ATTACK" or word == "HIT" or word == "PUNCH" or word == "KICK":
				hit = random.randint(1,100)
				if hit <= 75:
					slowprint("With careful aim and skill, you are able to land a hit and they take damage.")
					enemy.health -= 20
				else:
					slowprint("You go in for an attack but lost your footing and missed.")
				break
					
			# HANDLE PLAYER SHOOT
			elif word == "SHOOT" or word == "FIRE":
				found = False
				for pistol in gameData["player"].inventory:
					if pistol.name == "pistol03" or pistol.name == "pistol02" or pistol.name == "pistol01" or pistol.name == "pistol04":
						found = True
						break	
				if found:
					slowprint("With a steady arm you are able to land a shot on them.")
					enemy.health -= 50
				else:
					slowprint("You don't have your pistol with you and can't shoot him.")
			
			# HANDLE PLAYER DODGE
			elif word == "DODGE" or word == "EVADE":
				slowprint("You anticipate their attacke and prepare to move out of the way.")
				dodge = True
				break
				
			# HANDLE IF PLAYER ATTEEMPTS TO RUN/MOVE
			elif word == "GO" or word == "MOVE" or word == "HEAD" or word == "NORTH" or word == "STRAIGHT" or word == "FORWARD" or word == "SOUTH" or word == "BACK" or word == "LEAVE" or word == "BEHIND" or word == "EAST" or word == "RIGHT" or word == "WEST" or word == "LEFT" or word == "UP" or word == "2" or word == "DOWN" or word == "1" or word == "RUN" or word == "ESCAPE":
				slowprint("As you try to run away, the enemy grabs you and pushes you away from the exit. They won't let you escape without a fight.")
				break
				
			# HANDLE IF PLAYER TAKES/GRAB
			elif word == "TAKE" or word == "GRAB":
				if len(gameData["player"].inventory) < 7:
					take = False
					for i in range(len(gameData["items"])):
						for name in gameData["text"]:
							if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True and gameData["items"][i].moveable == True and gameData["items"][i].name.upper() == name:
								gameData["player"].inventory.append(gameData["items"].pop(i))
								slowprint("Item taken")
								take = True
								break
						if take:
							break
					if not take:
						slowprint("Could not take that item")
				else:
					slowprint("You are carrying too many items.")
				break
				
			# HANDLE IF PLAYER DROPS ITEM
			elif word == "DROP" or word == "REMOVE":
				drop = False
				for i in range(len(gameData["player"].inventory)):
					for name in gameData["text"]:
						if gameData["player"].inventory[i].name.upper() == name:
							item = gameData["player"].inventory.pop(i)
							item.location = gameData["player"].location
							gameData["items"].append(item)
							slowprint("Item dropped")
							drop = True
					if drop:
						break
				if not drop:
					slowprint("Could not drop that item")
				break
				
			# HANDLE USE A MEDKIT
			elif word == "USE":
				found = False
				for item in gameData["text"]:
					if item == "MEDKIT":	
						for i in range(len(gameData["player"].inventory)):
							if gameData["player"].inventory[i].name.upper() == item:
								gameData["player"].inventory.pop(i)
								gameData["player"].health = 100
								slowprint("You have been fully healed.")
								found = True
								break		
				if not found:
					slowprint("You don't have the item.")
				break
				
			elif word == gameData["text"][len(gameData["text"])-1]:
				slowprint("Sorry, can't understand what you want to do.")			
			
		# ENEMY ATTACKS IF ALIVE
		hit = random.randint(1,100)
		if enemy.health > 0:
			if hit <= (enemy.hitrate * 100):
				if dodge:
					slowprint("They go in for an attack but you are able to quickly move out of the way.")
				else:
					gameData["player"].health -= enemy.damage
					slowprint(enemy.name + " has landed a hit on you and as a result you have taken some damage.")
			else:
				slowprint(enemy.name + " goes for an attack but they hesitate slightly and miss.")
			
	# SEE IF BOSS IS DEAD
	if enemy.health <= 0:
		if enemy.name == "Daniel Smith":
			gameData["open"] = False
		else:
			slowprint(enemy.name + " goes down. You have won the battle.")
			enemy.location = 0
			
	if gameData["player"].health <= 0:
		gameData["open"] = False
	
def startScreen(gameData):
	print()
	slowprint("Welcome to ELUCIDATION.")
	print()
	slowprint("In order to play this game, please type short phrases into the command line. "+
			  "The phrases need to follow a verb-noun style. "+
			  "You can type 'LOOK' to get more detail in your surroundings. "+
			  "You can type 'EXAMINE' to get more detail description on the items. "+
			  "Typing 'INVENTORY' lists what you are currently holding. "+
			  "You can type 'GET', 'TAKE', 'DROP' and 'PLACE' to interact with items. "+
			  "To enter a code type 'ENTER' followed by a set of digits. "+
			  "Type 'HELP' at any time for more detailed game instructions. "+
			  "To exit he game type 'EXIT'. Be careful not to confuse this with leaving a room. ")
	print()
	slowprint("Lets begin!")
	print()
	slowprint("You are Richard Smith, a detective at the New York State Police Facility. "+
			  "You've been working for nearly 10 years now and have just taken down the largest "+
			  "mob boss in the city after he stole an illegal time machine. The device has been "+
			  "taken back to the facility and you have been promoted. ")
	print()
	slowprint("Today is also the 10 year anniversary of your older brothers death. "+
			  "His killer was never caught and every year on this day you try to "+
			  "look over his file in the system and try to find something you missed...")
	print()
			  
	slowprint("You are " + gameData["rooms"][gameData["player"].location].shortdescription)
	slowprint(gameData["rooms"][gameData["player"].location].description)
	print()

	slowprint("You see the following: ")
	for i in range(len(gameData["items"])):
		if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
			slowprint(gameData["items"][i].name)
	
def ending(gameData):
	if gameData["player"].health <= 0:
		slowprint("You have taken a lot of damage and cannot continue on. You collapse to the ground while holding your wounds. As you lie there dying, you feel a sense of regret as you were not able to solve your brothers case, but feel happy as the light takes you knowing that you will see him again soon.")
		
	if gameData["enemies"][1].health <= 0:
		gameData["score"] += 10
		slowprint("As your brother falls to the floor, everything starts to come together. You were the one to kill him cause you were the one that laid out all the clues. You are the one that covers everything up, as to protect your brothers name, and becomes the Director of the New York State police. ")
		print()
		slowprint("As you work on cleaning up the scene you start to plan everything. Remembering every detail of how you got here because now you have to send yourself done this path...again.")
		
	slowprint("You finished the game with a total score of " + str(gameData["score"]))

##############################################################################################################
#																											 #
#									    INITIALIZE GAME DATA					     						 #
#																											 #
##############################################################################################################
def initialize():
	gameData = {"text": [],
				"player": None,
				"rooms": None,
				"items": None,
				"enemies": None,
				"people": None,
				"score": 0,
				"skip": False,
				"moved": True,
				"open": True}

	playerItems = []
	playerItems.append(Item("ID", "Your New York ID card with your name, 'Richard Smith', and birthdate, 'October 23, 2157'", 0, True, True, 'default'))
	playerItems.append(Item("pocketwatch", "An old pocketwatch that your father gave to you before he left to fight in the war. It has a crack in the glass on the face and it no longer ticks.", 0, True, True, 'default'))
	gameData["player"] = Player(1, playerItems, 100)

	#Create all the rooms the player may go to
	rooms = {}
	rooms[1]  = Room("in the main lobby of the New York State Police Facility.", "The lobby has a granite tile floor and white walls with fluorescent lighting. To your left is the elevator and to your right is the front reception desk for this floor. There is a hallway in fron of you.", True, 11, 3, 0, 2, 0, 0)
	rooms[2]  = Room("inside the elevator.", "The back wall of the elevator is a mirror and the other walls are all white with black decor. There is a panel with 2 buttons labeled 'Floor 1' and 'Floor 2' with Floor 1 currently lit.", True, 1, 0, 1, 0, 12, 0)
	rooms[3]  = Room("standing at the reception desk.", "There is a man working away on the computer at the desk. His desk is neat and tidy, everything looks to be in its own place. Behind him in big letters is 'NEW YOUR STATE POLICE'", True, 0, 0, 1, 0, 0, 0)
	rooms[4]  = Room("standing in one of the offices.", "No one else is in the room, this employee seems to have finished his shift. There is a desk with a black chair and a large window behind them. The walls are all white, the same as the hallway.", True, 0, 0, 11, 0, 0, 0)
	rooms[5]  = Room("in a dimly lit office.", "This office is poorly lit. There is a single lamp that is on and the blinds have been pulled down the window making the room dark. There is a large desk and chair at the back of the room with nothing on the desk.", True, 0, 0, 11, 0, 0, 0)
	rooms[6]  = Room("standing in your office.", "A desk and chair are in the room with a large window overlooking the barren landscape of the outside world. Everything is clean and untouched.", True, 0, 0, 8, 0, 0, 0)
	rooms[7]  = Room("in an offices space.", "There is a women named Karen sitting at her desk eating lunch. There is a wall behind her filled with articles and pictures with string connecting them all. She is working on a murder case.", True, 0, 0, 8, 0, 0, 0)
	rooms[8]  = Room("at the end of the hallway.", "There is a pair of sliding doors to your left and right as well forward. An empty trash bin sits in the cornor of the room.", True, 9, 7, 11, 6, 0, 0)
	rooms[9]  = Room("in the first half of the records room.", "There are shelves filled with old dusty boxes in the room. The shelves are labeled alphabetically starting at A to M. The room continues down to your right.", False, 0, 10, 8, 0, 0, 0)
	rooms[10] = Room("in the second half of the records room.", "The shelves filled with boxes continue starting at N and finishing at Z.", True, 0, 0, 0, 9, 0, 0)
	rooms[11] = Room("in a long hallway", "The floor is tiled the same as the lobby and the walls and ceiling are all painted white. There is a pair of sliding doors to your left and right and the hallway continues forward.", True, 8, 5, 1, 4, 0, 0)
	rooms[12] = Room("inside the elevator.", "The back wall of the elevator is a mirror and the other walls are all white with black decor. There is a panel with 2 buttons labeled 'Floor 1' and 'Floor 2' with Floor 2 currently lit.", True, 14, 0, 14, 0, 0, 2)
	rooms[13] = Room("standing in front of a reception desk.", "There is a women working away on a computer. Her desk is cluttered with paperwork and she appears to be lost in her work. ", True, 0, 0, 14, 0, 0, 0)
	rooms[14] = Room("in a lobby room.", "The floors and walls are the same as the first floor, black granite tiles and white everywhere else. The elevator is to your left and a reception desk to your right. There is a hallway in fron of you.", True, 15, 13, 0, 12, 0, 0)
	rooms[15] = Room("in a long corridor.", "The corridor has the same design as the rest of the building. There are a pair of sliding doors to your right and left. Also, the corridor continues foward.", True, 16, 22, 14, 17, 0, 0)
	rooms[16] = Room("at the end of the long corridor.", "There are three sets of sliding doors to your left, right, and forward. One of the lights in the ceiling has burnt out.", True, 23, 18, 15, 20, 0, 0)
	rooms[17] = Room("inside the Re-creation Room.", "The walls and floor are all made with large white electrical tiles that are giving off slight glow to light up the room.", True, 0, 0, 15, 0, 0, 0)
	rooms[18] = Room("standing in the New York State Police Armory.", "There are shelves in front of you filled with automatic assult weapons, heavy artilery, and tacticle equipment that are all locked up behind an electric barrier. The room continues further forward.", True, 19, 0, 16, 0, 0, 0)
	rooms[19] = Room("at the end of the armory room.", "There is a shelf that holds all the issued pistols with the owners name as well as its serial number.", True, 0, 0, 18, 0, 0, 0)
	rooms[20] = Room("in the office of one of the scientists.", "There is a man that is sleeping at the desk. There are lots of whiteboards around that have been filled with complex equations and algorithms.", True, 0, 0, 16, 0, 0, 0)
	rooms[21] = Room("at the back of the lab room.", "There is a long table with large pieces of equipment on it. Everything is extremely clean. There is an empty closet to your right.", True, 0, 29, 22, 0, 0, 0)
	rooms[22] = Room("in the labratory room.", "The entire room is white with the only colour coming from the lights of the equipment. There are tables filled with small pieces of scientific equipment and the room continues on forward. There is not a spec of dust in the room.", False, 21, 0, 15, 0, 0, 0)
	rooms[23] = Room("standing in the middle of the special evidance lockup.", "There is a large pod in the center of the room with huge cables coming out of it and attching to the ground. The pod looks like it can fit one person. The room also continues to your left and right.", False, 26, 24, 26, 25, 0, 0)
	rooms[24] = Room("amoungst shelves filled with evidance.", "These shelves are filled all the dangerous weapons that have been found over the years. Every item is locked is a special clear glass case.", True, 0, 0, 23, 0, 0, 0)
	rooms[25] = Room("surronded by shelves of computer equipment.", "The shelves have been filled with broken computers and other useless electrical equipment.", True, 0, 0, 23, 0, 0, 0)
	rooms[26] = Room("in standing a very small pod.", "The walls are less than two inches from you on all sides. There is a small window at face level. The only light is the flashing lights in the pod. One of those lights is a button that says 'PUSH TO TRAVEL'.", True, 23, 0, 23, 0, 27, 27)
	rooms[27] = Room("standing outside a small hut by a lake.", "The hut is not big enough to be a house. The door is slightly open and you can hear noise coming from inside", True, 28, 0, 0, 0, 0, 0)
	rooms[28] = Room("inside a single room.", "The place is filled with weapons, blueprints of the New York Stat Police Facility, and explosives. Your brother is working on something.", True, 0, 0, 27, 0, 0, 0)
	rooms[29] = Room("inside an empty closet.", "The walls are a thin sheet metal. There is 5 vent slits at your feet so you can't see outside of it. It is completely dark in here.", True, 21, 0, 21, 0, 0, 0)
	gameData["rooms"] = rooms

	#Create all the items
	items = []
	items.append(Item("plant", "A fake plant in a pot sits in the corner as an attempt to make the lobby more appealing.", 1, False, True, 'default'))
	items.append(Item("pen", "A standered black ball point pen. Mostly used for writing stuff down.", 4, True, True, 'default'))
	items.append(Item("cabinet", "A 4 drawer metal filing cabinet that has a biometric lock.", 4, False, True, 'locked'))
	items.append(Item("map", "The map on the wall gives you a layout of the two floors. The first floor is the offices and records room. The second floor is the Lab, Re-creation Room, Armory, and the Special Lockup.", 11, False, True, 'default'))
	items.append(Item("smallmap", "A pocket sized map for guest visitors. Map tells you the first floor is the offices and records room. Second floor is the Lab, Re-creation Room, Armory, and the Special Lockup.", 3, True, True, 'default'))
	items.append(Item("safe", "A small safe built with solid metal that has a 6 digit passcode on it.", 5, False, True, 'locked'))
	items.append(Item("notebook", "A small red notebook filled with notes from old cases. On the front cover the letters 'S I X' are written in black.", 5, True, True, 'default'))
	items.append(Item("watch", "A very old wrist watch that doesn't seem to be ticking anymore. On the back there is an engraving that says 'To my love, September 19, 2124'", 5, True, True, 'default'))
	items.append(Item("computer", "A computer that is issued in ever office in the building. There is an eye scan to unlock it.", 6, False, True, 'locked'))
	items.append(Item("keycard", "Your own keycard to gain get around the facility.", 6, True, True, 'default'))
	items.append(Item("mug", "A used mug that still smells like this mornings coffee.", 7, True, True, 'default'))
	items.append(Item("painting", "A painting of New York before the shut in. It shows Time Square during the night.", 1, False, True, 'default'))
	items.append(Item("painting", "A picture of what the outside world looks like after the smog took over", 8, False, True, 'default'))
	items.append(Item("painting", "A group of soldiers playing cards together during the war between New York and Boston.", 7, False, True, 'default'))
	items.append(Item("record01", "Amerson, James. Cop. Served 11 years. Born April 17, 2164. Died June 6, 2180. KIA.", 9, True, True, 'default'))
	items.append(Item("record02", "Byers, Nichole. Detective. Served 30 years. Born March 14, 2133. Retired July 31, 2189.", 9, True, True, 'default'))
	items.append(Item("record03", "Fergenson, Bruce. SWAT. Served 7 years. Born February 14, 2150. Died June 23, 2180. KIA.", 9, True, True, 'default'))
	items.append(Item("record04", "Hill, Henery. SWAT. Served 14 years. Born March 10, 2147. Died November 16, 2181. KIA.", 9, True, True, 'default'))
	items.append(Item("record05", "Mathews, Avery. Inteligance. Served 30 years. Born January 9, 2130. Retired September 30, 2175.", 9, True, True, 'default'))
	items.append(Item("record06", "Parkinson, Niel. Cop. Served 25 years. Born January 19, 2145. Retired April 30, 2190.", 10, True, True, 'default'))
	items.append(Item("record07", "Smith, Daniel. Detective. Served 30 years. Born October 21, 2149. Died April 30, 2182. KIA (He appears to have served after his death. This was never on the digital file)", 10, True, True, 'default'))
	items.append(Item("record08", "Turk, Michelle. Cop. Served 25 years. Born May 6, 2143. Retired June 30, 2187.", 10, True, True, 'default'))
	items.append(Item("record09", "There are blueprints of the New York Encloser with 'X' marking the generators. There is also a key to reconstruct the crime scene in the Reconstruction room that was invented only 4 years ago. The Key is '00153890'.", 5, True, False, 'default'))
	items.append(Item("keypad", "A key pad on the wall. It is asking for a 8 digit code.", 17, False, True, 'default'))
	items.append(Item("bullet", "A 3D printed bullet that was used to kill your brother.", 17, True, False, 'default'))
	items.append(Item("map", "The map on the wall gives you a layout of the two floors. The first floor is the offices and records room. The second floor is the Lab, Re-creation Room, Armory, and the Special Lockup.", 15, False, True, 'default'))
	items.append(Item("beaker", "A 500ml beaker that has not yet been washed.", 22, True, True, 'default'))
	items.append(Item("scanner", "A large scanner that will scan pieces of evidance and print out all the results.", 21, False, True, 'default'))
	items.append(Item("labkey", "A keycard that will let someone enter the lab.", 20, True, True, 'default'))
	items.append(Item("pistol01", "Standered 9mm. Owner: Frank Bernard. Serial Number: 1342.", 19, True, True, 'default'))
	items.append(Item("pistol02", "Standered 9mm. Owner: Jessie James. Serial Number: 5645.", 19, True, True, 'default'))
	items.append(Item("pistol03", "Standered 9mm. Owner: Richard Smith. Serial Number: 1989.", 19, True, True, 'default'))
	items.append(Item("pistol04", "Standered 9mm. Owner: Zack Brown. Serial Number: 6574.", 19, True, True, 'default'))
	items.append(Item("medkit", "A kit that has a needle that when injected, will heal all wounds on a person.", 6, True, True, 'default'))
	items.append(Item("medkit", "A kit that has a needle that when injected, will heal all wounds on a person.", 18, True, True, 'default'))
	items.append(Item("book", "A history book about the world after the uncovering. Chapter One details the story of the natural gas miners in Russia, how when attempting to unearth a new deposit they opened an enormous cavern beneath and unleashed the deadly substance known as Smog. Chapter Two explains how the Smog gradually engulfed the earth; at first it killed slowly but quickened as it thickened.  Chapter Three explains how rural communities were destroyed, but the urban centres survived by fortifying. Large metropolises created climate-controlled buildings connected by underground tunnels, eventually turning whole cities into a single, expansive building. Chapter Four describes the wars; cities attacked each other for food, water, and energy. The Boston/New York War was the worst, the loss of life – civilian and combatant – was unprecedented. Towards the end Boston’s resources were dwindling, and they had lost the most lives; but New York was operating at full capacity, unable to accommodate a larger population and forced to turn away refugees. The fifth and final chapter details the Shut In. When the smog got so bad even gas masks couldn’t filter it and stepping outside would immediately kill someone. All urban centres sealed off their entrances, closing themselves inside their sprawling network of tunnels and skyscrapers. With no way to leave, all the wars ceased. Attempts at communicating with other cities have failed, the smog seems to quench all wavelengths. Attempts at creating technology to leave have also been unsuccessful, but it’s speculated that – because of estimates that Boston’s already dwindled resources are nearly empty – the enemy will be renewing their efforts to reach NYC. The book is a grim reminder of your claustrophobic reality.", 4, True, True, 'default'))
	gameData["items"] = items
	
	#Create all the NPCs
	people = []
	people.append(Person("Stephen Santiago", "He is hard at work.", 3, "It has been a long week. I can't wait to go home", ["records", "You use your keycard to get into the records room. How could you forget?"]))
	people.append(Person("Claire Vandermer", "She is eating a homemade ceaser salad.", 13, "I am so sick of this diet. I want to eat cake.", ["lab", "Henery is the man in charge for that stuff. He might be in his office down the hall."]))
	people.append(Person("Karen Manchester", "She looks to be frustrated with something.", 7, "I am so close to cracking this case.", ["war", "Don't you remember? 12 years ago New York and Boston went to war because Boston didn't have enough resources so they attacked New York."]))
	people.append(Person("Henery Carlyl", "He is snoozing away", 20, "zzzZZZZZzzzzZZZZzzz", ["lab", "ZZzzzZZZzzzzZZZ"]))
	people.append(Person("Mr. Mystery", "He is a tall man dressed in all black suit", 0, "I got my eye on you boy.", ["record", "That is none of your concern"]))
	people.append(Person("The Director", "The man who has worked here the longest. He wears a dark cloak so you can't see his face.", 0, "Everything will make sense soon enough", ["brother", "All in due time will the answers come."]))
	people.append(Person("Paul Serfano", "A man who enjoys being a janitor.", 6, "I have seen more messes than you've seen crime scenes my friend.", ["life", "Life's a fucking bitch if you ask me."]))
	gameData["people"] = people
	
	#Create all the Enemies
	enemies = []
	enemies.append(Enemy("Mr. Mystery", "He is a tall man dressed in all black suit and he looks pissed", 0, 60, 0.50, 10))
	enemies.append(Enemy("Daniel Smith", "Your brother, who looks very much like you at this age.", 28, 100, 0.75, 30))
	enemies.append(Enemy("Bostonian Grunt", "He has no weapons but he isn't afraid of anything.", 0, 65, 0.35, 15))
	enemies.append(Enemy("Bostonian Marksmen", "He has a rifle but not a steady aim.", 0, 75, 0.40, 20))
	enemies.append(Enemy("Heavy Bostonian", "He has large muscular man ready for a fight.", 0, 80, 0.20, 20))
	gameData["enemies"] = enemies
	
	return gameData

##############################################################################################################
#																											 #
#									    	PROCESS INPUT    					     						 #
#																											 #
##############################################################################################################
def text(gameData):
	print()
	print("Current score is: ", str(gameData["score"]),"   Current Health is:", str(gameData["player"].health))
	gameData["text"] = input("Your input:  ").upper().split(' ')
	print()

##############################################################################################################
#																											 #
#									    	UPDATE GAME WORLD  					     						 #
#																											 #
##############################################################################################################
def update(gameData):
	# reset skip
	if gameData["skip"]:
		gameData["skip"] = False
		
	# HANDLE PLAYER MOVEMENT
	for direction in gameData["text"]:
		if direction == "NORTH" or direction == "STRAIGHT" or direction == "FORWARD":
			if gameData["rooms"][gameData["player"].location].north != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].north].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].north
				gameData["moved"] = True
			elif gameData["rooms"][gameData["player"].location].north != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].north].open == False:
				slowprint("That room is locked. You need a keycard to get in.")
				
		if direction == "SOUTH" or direction == "BACK" or direction == "LEAVE" or direction == "BEHIND":
			if gameData["rooms"][gameData["player"].location].south != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].south].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].south
				gameData["moved"] = True
			elif gameData["rooms"][gameData["player"].location].south != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].south].open == False:
				slowprint("That room is locked. You need a keycard to get in.")

		if direction == "EAST" or direction == "RIGHT":
			if gameData["rooms"][gameData["player"].location].east != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].east].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].east
				gameData["moved"] = True
			elif gameData["rooms"][gameData["player"].location].east != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].east].open == False:
				slowprint("That room is locked. You need a keycard to get in.")

		if direction == "WEST" or direction == "LEFT":
			if gameData["rooms"][gameData["player"].location].west != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].west].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].west
				gameData["moved"] = True
			elif gameData["rooms"][gameData["player"].location].west != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].west].open == False:
				slowprint("That room is locked. You need a keycard to get in.")

		if direction == "UP" or direction == "2":
			if gameData["rooms"][gameData["player"].location].up != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].up].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].up
				gameData["moved"] = True

		if direction == "DOWN" or direction == "1":
			if gameData["rooms"][gameData["player"].location].down != 0 and gameData["rooms"][gameData["rooms"][gameData["player"].location].down].open == True:	
				gameData["player"].location = gameData["rooms"][gameData["player"].location].down
				gameData["moved"] = True

	
	# HANDLE THE NPC AND ENEMY MOVEMENT IN THE GAME
	for word in gameData["text"]:
		if word == "GO" or word == "MOVE" or word == "HEAD" or word == "NORTH" or word == "STRAIGHT" or word == "FORWARD" or word == "SOUTH" or word == "BACK" or word == "LEAVE" or word == "BEHIND" or word == "EAST" or word == "RIGHT" or word == "WEST" or word == "LEFT" or word == "UP" or word == "2" or word == "DOWN" or word == "1" or word == "WAIT":
			for person in gameData["people"]:
				# Janitor will randomly move around the first floor.
				if person.name == "Paul Serfano" and person.location != 0:
					x = random.randint(1, 100)
					if x > 75:
						int = random.randint(1, 4)
						if int == 1:
							if gameData["rooms"][person.location].north != 0 and gameData["rooms"][person.location].north != 9:	
								person.location = gameData["rooms"][person.location].north
								
						elif int == 2:
							if gameData["rooms"][person.location].east != 0 and gameData["rooms"][person.location].east != 9:	
								person.location = gameData["rooms"][person.location].east
								
						elif int == 3:
							if gameData["rooms"][person.location].south != 0 and gameData["rooms"][person.location].south != 9:	
								person.location = gameData["rooms"][person.location].south
								
						elif int == 4:
							if gameData["rooms"][person.location].west != 0 and gameData["rooms"][person.location].west != 9:	
								person.location = gameData["rooms"][person.location].west
				
				# Mr. Mystery will wounder the halls on the first floor until he becomes an enemy
				if person.name == "Mr. Mystery" and person.location != 0:
					if gameData["rooms"][person.location].south != 0:
						person.location = gameData["rooms"][person.location].south
					else:
						person.location = 9
				
				# The Director will follow you to help you fight when he enters. He is slow so he moves in after you.
				if person.name == "The Director" and person.location != 0 and gameData["player"].location < 26:
					person.location = gameData["player"].location
					
			for enemy in gameData["enemies"]:
				if enemy.location != 0:
					# MR. MYSTERY WILL MOVE AROUND THE TOP FLOOR LOOKING FOR YOU
					if enemy.name == "Mr. Mystery":
						int = random.randint(1, 4)
						if int == 1:
							if gameData["rooms"][enemy.location].north != 0 and gameData["rooms"][enemy.location].north != 23 and gameData["rooms"][enemy.location].north != 29:	
								enemy.location = gameData["rooms"][enemy.location].north
							
						elif int == 2:
							if gameData["rooms"][enemy.location].east != 0 and gameData["rooms"][enemy.location].east != 23 and gameData["rooms"][enemy.location].north != 29:	
								enemy.location = gameData["rooms"][enemy.location].east
								
						elif int == 3:
							if gameData["rooms"][enemy.location].south != 0 and gameData["rooms"][enemy.location].south != 23 and gameData["rooms"][enemy.location].north != 29:	
								enemy.location = gameData["rooms"][enemy.location].south
							
						elif int == 4:
							if gameData["rooms"][enemy.location].west != 0 and gameData["rooms"][enemy.location].west != 23 and gameData["rooms"][enemy.location].north != 29:	
								enemy.location = gameData["rooms"][enemy.location].west
							
					# MARKSMEN WILL MOVE AROUND THE BOTTEM FLOOR 
					if enemy.name == "Bostonian Marksmen":
						int = random.randint(1, 4)
						if int == 1:
							if gameData["rooms"][enemy.location].north != 0 and gameData["rooms"][enemy.location].north != 9:	
								enemy.location = gameData["rooms"][enemy.location].north
							
						elif int == 2:
							if gameData["rooms"][enemy.location].east != 0 and gameData["rooms"][enemy.location].east != 9:	
								enemy.location = gameData["rooms"][enemy.location].east
								
						elif int == 3:
							if gameData["rooms"][enemy.location].south != 0 and gameData["rooms"][enemy.location].south != 9:	
								enemy.location = gameData["rooms"][enemy.location].south
							
						elif int == 4:
							if gameData["rooms"][enemy.location].west != 0 and gameData["rooms"][enemy.location].west != 9:	
								enemy.location = gameData["rooms"][enemy.location].west
								
					# HEAVY WILL MOVE AROUND THE LOCKUP WAITING FOR YOU
					if enemy.name == "Heavy Bostonian":
						int = random.randint(1, 3)
						if int == 1:	
							enemy.location = 25
							
						elif int == 2:
							enemy.location = 24
								
						elif int == 3:
							enemy.location = 23
							
	# HANDLE IF ENCOUNTER ENEMY. IF SO MOVE TO COMBAT AND MUST DEFEAT BEFORE CAN DO ANYTHING ELSE
	for enemy in gameData["enemies"]:
		if enemy.location == gameData["player"].location:
			combat(enemy, gameData)
			gameData["skip"] = True
	
	
	# HANDLE OBJECTIVES
	# OBJECTIVE 1
	if gameData["rooms"][9].open and gameData["score"] == 0:
		gameData["score"] += 10
	
	# OBJECTIVE 6
	if gameData["rooms"][22].open and gameData["score"] == 50:
		gameData["score"] += 10
		
	# OBJECTIVE 8
	if gameData["player"].location == 18 and gameData["score"] == 70:
		gameData["score"] += 10
		
	for word in gameData["text"]:
		#OBJECTIVE 2
		if word == "EXAMINE" or word == "TAKE":
			for file in gameData["text"]:
				if file == "RECORD07" and gameData["player"].location == 10 and gameData["score"] == 10:
					gameData["score"] += 10
					slowprint("You start to examine the file. It turns out to be your brothers file and you notice something does not seem right, "+
							  "but before you can look at it further a man dressed in all black takes the file from your hands. "+
							  "'You shouldn't be in here, looking through stuff that doesn't concern you.' he says through the grit of his teeth. "+
							  "You try to explain how that file is about your dead brother but he does not care. "+
							  "'This file will be secure in my locked safe in my office' he says barking at you. "+
							  "You watch him walk away with a distgusted look on your face.")
					for i in range(len(gameData["items"])):
						if gameData["items"][i].name == "record07":
							gameData["items"][i].location = 5
							gameData["items"][i].available = False
					gameData["people"][4].location = 8
					gameData["skip"] = True
					
		# OBJECTIVE 3
		if word == "ENTER":
			for code in gameData["text"]:
				if code == "190924" and gameData["player"].location == 5 and gameData["score"] == 20:
					for i in range(len(gameData["items"])):
						if gameData["items"][i].name == "record07":
							gameData["items"][i].available = True
					gameData["items"].append(Item("reckey", "A key that you enter into the Re-creation Room to recreate a crime scene. This one is 00153890. It fell out of your brothers file.", 5, True, True, 'default'))
					gameData["skip"] = True
					gameData["score"] += 10
					for i in range(len(gameData["items"])):
						if gameData["items"][i].name == "record07":
							gameData["items"][i].available = True
							
					slowprint("You have opened the safe and can now see the following items.")
					for i in range(len(gameData["items"])):
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
							slowprint(gameData["items"][i].name)
							
		# OBJECTIVE 4
		if word == "EXAMINE":
			for file in gameData["text"]:
				if file == "RECORD07":
					for i in range(len(gameData["items"])):
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True and gameData["items"][i].name.upper() == file and gameData["score"] == 30:
							slowprint(gameData["items"][i].description)
							gameData["score"] += 10
							gameData["skip"] = True

					for i in range(len(gameData["player"].inventory)):
						if gameData["player"].inventory[i].name.upper() == file and gameData["score"] == 30:
							slowprint(gameData["player"].inventory[i].description)
							gameData["score"] += 10
							gameData["skip"] = True
							
		# OBJECTIVE 5
		if word == "ENTER":
			for code in gameData["text"]:
				if code == "00153890" and gameData["player"].location == 17 and gameData["score"] == 40:
					gameData["score"] += 10
					gameData["skip"] = True
					gameData["items"].append(Item("bullet", "A special 3D printed bullet that can be scanned by the scanner. This was the bullet that was used to kill your brother.", 17, True, True, 'default'))
							
					slowprint("There is a click and the tiles all around start to flicker as they warm up. "+
							  "The surroundings change and everything is a digital outline. ")
					gameData["rooms"][17].description = "You are in a digital reconstruction of the hut your brother was murdered in. There are tables that are empty and there is a body on the floor with a single bullet to the head. The bullet that killed him has been recreated into a physical object."
					print()
					slowprint(gameData["rooms"][gameData["player"].location].description)
					slowprint("You see the following: ")
					for i in range(len(gameData["items"])):
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
							slowprint(gameData["items"][i].name)
					for i in range(len(gameData["people"])):
						if gameData["people"][i].location == gameData["player"].location:
							slowprint("A person named "+gameData["people"][i].name+". "+gameData["people"][i].description)
					print()
					
		# OBJECTIVE 7
		if word == "PLACE" or word == "USE":
			for item in gameData["text"]:
				if item == "SCANNER" and gameData["player"].location == 21 and gameData["score"] == 60:
					for i in range(len(gameData["player"].inventory)):
						if gameData["player"].inventory[i].name == "bullet":
							gameData["score"] += 10
							gameData["skip"] = True
							gameData["items"].append(Item("result", "The bullet is from a modern issued side arm from the New York State Police Department, serial number 1989.", 21, True, True, 'default'))
							slowprint("You place the bullet into the scanner and it starts to make a light. However, you here the voice of the Mystery man outside of the room. He is looking for you and he sounds mad. ")
							slowprint("You now see the following: ")
							for i in range(len(gameData["items"])):
								if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
									slowprint(gameData["items"][i].name)
							for i in range(len(gameData["people"])):
								if gameData["people"][i].location == gameData["player"].location:
									slowprint("A person named "+gameData["people"][i].name+". "+gameData["people"][i].description)
							print()
							gameData["people"][4].location = 0
							gameData["enemies"][0].location = 22							
		
		# OBJECTIVE 9
		if word == "EXAMINE":
			go = False
			for pistol in gameData["text"]:
				if pistol == "PISTOL03":
					for i in range(len(gameData["items"])):
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].name.upper() == pistol and gameData["score"] == 80:
							slowprint(gameData["items"][i].description)
							go = True
							break

					for i in range(len(gameData["player"].inventory)):
						if gameData["player"].inventory[i].name.upper() == pistol and gameData["score"] == 80:
							slowprint(gameData["player"].inventory[i].description)
							go = True
							break
			# OBJECTIVE 10
			if go:
				gameData["score"] += 10
				gameData["skip"] = True
				slowprint("As you discover that somehow it was your gun that killed your brother there is a loud explosion and the Director appears in the room. However, before you can even get a word out there is another loud explosion that rings throughout the facility.")
				slowprint("'Fight with me.' the director says 'The Bostonians are attacking the facility. They want to take over this facility so that New York will be defenseless when they wage war again.'")
				slowprint("A man rushes into the room.")
				
				# ADD ENEMIES
				gameData["enemies"][2].location = gameData["player"].location
				gameData["enemies"][3].location = 1
				gameData["enemies"][4].location = 14
				
				# GET RID OF THE NPC (THEY ARE HIDING FROM THE ATTACKERS	
				for person in gameData["people"]:
					if person.location != 0 and person.name != "The Director":
						person.location = 0
				combat(gameData["enemies"][2], gameData)
				gameData["score"] += 10
				slowprint("As the grunt falls to the ground, the Director hands you an odd looking key.")
				slowprint("'This is the key to get into the special lockup.' he says giving it to you, 'You know what you need to do. Go. I will help you fight off any more intruders.'")
				gameData["player"].inventory.append(Item("timekey", "A special key that will give the person access to the special lockup room in the facility.", 0, True, True, 'default')) 
				found = False
				for pistol in gameData["player"].inventory:
					if pistol.name == "pistol03":
						found = True
				if not found:
					slowprint("Before you leave he also hands you your pistol.")
					for pistol in gameData["items"]:
						if pistol.name == "pistol03":
							gameData["player"].inventory.append(pistol)
							gameData["items"].remove(pistol)
				
		# OBJECTIVE 11
		if word == "USE" or word == "PUSH":
			if gameData["player"].location == 26 and gameData["score"] == 100:
				gameData["score"] += 10
				gameData["skip"] = True
				gameData["player"].location = 27
				slowprint("The pod starts to rumble and the sound of motors turning becomes louder and louder. You look out of the small window to see the Director easily taking down the invaders. Before you are blinded by a flahing light the Director turns to you and shows his face, which looks remarkably like you.")
				slowprint("Your eyesight starts to come back after a few seconds.")
				slowprint("This is what you see, ")
				slowprint(gameData["rooms"][gameData["player"].location].description)
				slowprint("You see the following: ")
				for i in range(len(gameData["items"])):
					if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
						slowprint(gameData["items"][i].name)
				for i in range(len(gameData["people"])):
						if gameData["people"][i].location == gameData["player"].location:
							slowprint("A person named "+gameData["people"][i].name+". "+gameData["people"][i].description)
				print()
				
	# OBJECTIVE 12 IS COMPLETEING THE GAME. SO MUST DEFEAT YOUR BROTHER (DONE IN COMBAT FUNCTION)			
					
					
##############################################################################################################
#																											 #
#									    	DISPLAY TEXT    					     						 #
#																											 #
##############################################################################################################
def display(gameData):
	# CHECK TO SEE IF TO SKIP IT. IT SKIPS WHEN THERE IS A 'CUT SCENE'/COMPLETED AN OBJECTIVE
	if not gameData["skip"]:
		for word in gameData["text"]:
			# HANDLE MOVEMENT 
			if word == "GO" or word == "MOVE" or word == "HEAD" or word == "NORTH" or word == "STRAIGHT" or word == "FORWARD" or word == "SOUTH" or word == "BACK" or word == "LEAVE" or word == "BEHIND" or word == "EAST" or word == "RIGHT" or word == "WEST" or word == "LEFT" or word == "UP" or word == "2" or word == "DOWN" or word == "1":
				if gameData["moved"]:
					#Print room description
					slowprint("You are " + gameData["rooms"][gameData["player"].location].shortdescription)
					slowprint(gameData["rooms"][gameData["player"].location].description)
					print()
					
					#Print all the items in the room
					slowprint("You see the following: ")
					for i in range(len(gameData["items"])):
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
							slowprint(gameData["items"][i].name)
							
					#Print people in the room
					for i in range(len(gameData["people"])):
						if gameData["people"][i].location == gameData["player"].location:
							slowprint("A person named "+gameData["people"][i].name+". "+gameData["people"][i].description)
					print()
					gameData["moved"] = False
				else:
					slowprint("Sorry, you can't go that way.")
				break
			
			# HANDLE LOOK
			elif word == "LOOK":
				slowprint("This is what you see")
				slowprint(gameData["rooms"][gameData["player"].location].description)
				slowprint("You see the following: ")
				for i in range(len(gameData["items"])):
					if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True:
						slowprint(gameData["items"][i].name)
				for i in range(len(gameData["people"])):
						if gameData["people"][i].location == gameData["player"].location:
							slowprint("A person named "+gameData["people"][i].name+". "+gameData["people"][i].description)
				print()
						
			# HANDLE TAKE/GRAB
			elif word == "TAKE" or word == "GRAB":
				if len(gameData["player"].inventory) < 7:
					take = False
					for i in range(len(gameData["items"])):
						for name in gameData["text"]:
							if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True and gameData["items"][i].moveable == True and gameData["items"][i].name.upper() == name:
								gameData["player"].inventory.append(gameData["items"].pop(i))
								slowprint("Item taken")
								take = True
								break
						if take:
							break
					if not take:
						slowprint("Could not take that item")
				else:
					slowprint("You are carrying too many items.")
				break
				
			# HANDLE DROP
			elif word == "DROP" or word == "REMOVE":
				drop = False
				for i in range(len(gameData["player"].inventory)):
					for name in gameData["text"]:
						if gameData["player"].inventory[i].name.upper() == name:
							item = gameData["player"].inventory.pop(i)
							item.location = gameData["player"].location
							gameData["items"].append(item)
							slowprint("Item dropped")
							drop = True
					if drop:
						break
				if not drop:
					slowprint("Could not drop that item")
				break
				
			# HANDLE EXAMINE
			elif word == "EXAMINE":
				found1 = False
				for i in range(len(gameData["items"])):
					for name in gameData["text"]:
						if gameData["items"][i].location == gameData["player"].location and gameData["items"][i].available == True and gameData["items"][i].name.upper() == name:
							slowprint(gameData["items"][i].description)
							found1 = True
							break
					if found1:
						break
				
				found2 = False
				for i in range(len(gameData["player"].inventory)):
					for name in gameData["text"]:
						if gameData["player"].inventory[i].name.upper() == name:
							slowprint(gameData["player"].inventory[i].description)
							found2 = True
							break
					if found2:
						break
						
				if not found1 and not found2:
					slowprint("Could not find that item.")
				break
				
			# HANDLE INVENTORY
			elif word == "INVENTORY":
				slowprint("You have the following items on your personal:")
				for i in range(len(gameData["player"].inventory)):
					slowprint(gameData["player"].inventory[i].name)
				print()
				
			# HANDLE TALK
			elif word == "TALK":
				found = False
				for name in gameData["text"]:
					for person in gameData["people"]:
						if person.name.split(' ')[0].upper() == name and person.location == gameData["player"].location:
							found = True
							break	
					if found:
						slowprint("They say '"+person.statement+"'")
						break 
				if not found:
					slowprint("That person is not in the room. You are talking to your self.")
				break
			
			# HANDLE ASK
			elif word == "ASK":
				found = False
				for name in gameData["text"]:
					for person in gameData["people"]:
						if person.name.split(' ')[0].upper() == name and person.location == gameData["player"].location:
							found = True
							knows = False
							for keyword in gameData["text"]:
								if keyword.upper() == person.response[0].upper():
									slowprint("Their response is '"+person.response[1]+"'")
									knows = True
							if not knows:
								slowprint("Their response is 'Sorry, I do not know what you mean.'")
				if not found:
					slowprint("That person is not in the room. You are talking to your self.")
				break
								
			# HANDLE OPEN/UNLOCK
			elif word == "OPEN" or word == "UNLOCK":
				for item in gameData["text"]:
					if item == "DOOR":
						if gameData["player"].location == 8:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if  gameData["player"].inventory[i].name.upper() == "KEYCARD" and gameData["rooms"][9].open == False:
									gameData["rooms"][9].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "KEYCARD" and gameData["rooms"][9].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
								
						if gameData["player"].location == 15:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if  gameData["player"].inventory[i].name.upper() == "LABKEY" and gameData["rooms"][22].open == False:
									gameData["rooms"][22].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "LABKEY" and gameData["rooms"][22].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
								
						if gameData["player"].location == 16:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if gameData["player"].inventory[i].name.upper() == "TIMEKEY" and gameData["rooms"][23].open == False:
									gameData["rooms"][23].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "TIMEKEY" and gameData["rooms"][23].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
								
					
					if item == "COMPUTER":
						if gameData["player"].location == 6:
							for i in range(len(gameData["items"])):
									if  gameData["items"][i].name.upper() == "COMPUTER" and gameData["items"][i].state.upper() == "LOCKED":
										gameData["items"][i].state = "unlocked"
										slowprint("You unlocked your computer only to find that all the files have been erased. They must have changed your computer when you got the promotion.")
									elif gameData["items"][i].name.upper() == "COMPUTER" and gameData["items"][i].state.upper() == "UNLOCKED":
										slowprint("Your computer is already unlocked and there is nothing on it. They changed your computer when you got the promotion.")
					
					if item == "CABINET":
						if gameData["player"].location == 4:
							slowprint("You try to unlock it but it fails. It is not registared to your biometrics.")
							
					if item == "SAFE":
						if gameData["player"].location == 5:
							slowprint("You need to enter a code.")
				break
							
			# HANDLE WAIT
			elif word == "WAIT":
				slowprint("You don't move from you current location.")
				break

			# HANDLE USE
			elif word == "USE":
				found = False
				for item in gameData["text"]:
					if item == "MEDKIT":	
						for i in range(len(gameData["player"].inventory)):
							if gameData["player"].inventory[i].name.upper() == item:
								gameData["player"].inventory.pop(i)
								gameData["player"].health = 100
								slowprint("You have been fully healed.")
								found = True
								break
					elif item == "SCANNER":
						if gameData["player"].location == 21:
							slowprint("You have nothing that needs to be scanned at the moment.")
							break
						else:
							slowprint("You can't do that here.")
							break
					elif item == "COMPUTER":
						if gameData["player"].location == 6:
							for i in range(len(gameData["items"])):
									if  gameData["items"][i].name.upper() == "COMPUTER" and gameData["items"][i].state.upper() == "LOCKED":
										slowprint("Your computer is locked and needs to be unlocked.")
										found = True
										break
					if item == "KEYCARD":
						if gameData["player"].location == 8:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if  gameData["player"].inventory[i].name.upper() == "KEYCARD" and gameData["rooms"][9].open == False:
									gameData["rooms"][9].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "KEYCARD" and gameData["rooms"][9].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
								
						if gameData["player"].location == 15:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if  gameData["player"].inventory[i].name.upper() == "LABKEY" and gameData["rooms"][22].open == False:
									gameData["rooms"][22].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "LABKEY" and gameData["rooms"][22].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
								
						if gameData["player"].location == 16:
							found = False
							for i in range(len(gameData["player"].inventory)):
								if gameData["player"].inventory[i].name.upper() == "TIMEKEY" and gameData["rooms"][23].open == False:
									gameData["rooms"][23].open = True
									slowprint("You have unlocked the door.")
									found = True
								elif gameData["player"].inventory[i].name.upper() == "TIMEKEY" and gameData["rooms"][23].open == True:
									slowprint("All doors are open.")
									found = True
							if not found:
								slowprint("You do not have the right keycard")
						
					
				if not found:
					slowprint("You don't have the item.")
				break
							
						
				
			# HANDLE HELP
			elif word == "HELP":
				slowprint("Try to be as specific as possible but also as simple as possible. " +
				"The vocab that will be understod is limited. " + 
				"Never use single letters, always use full words. " + 
				"For movement you can simply type the direction you wish to go. " + 
				"If rooms are locked it means that you need a special key and you must then open it. " + 
				"You can only carry 7 items at a time. " + 
				"To enter a code type 'ENTER' followed by a set of digits. "+
				"Leave no stone unturned, or in the case, no item unexamined. " + 
				"To attack an enemy, say attack or if you have a firearm you can use that as well. " + 
				"Or you can evade attacks. " + 
				"You can type 'LOOK' to get more detail in your surroundings. "+
			    "You can type 'EXAMINE' to get more detail description on the items. "+
			    "Typing 'INVENTORY' lists what you are currently holding. "+
			    "You can type 'GET', 'TAKE', 'DROP' and 'PLACE' to interact with items. "+
			    "To enter a code type 'ENTER' followed by a set of digits. "+
			    "Type 'HELP' at any time for more detailed game instructions. "+
			    "To exit he game type 'EXIT'. Be careful not to confuse this with leaving a room. " +
				"And remeber. You are trying to find your brothers killer so follow the clues. " +
				"Good Luck. ")
				break
			
			# HANDLE EXIT
			elif word == "EXIT":
				sys.exit()
				
			elif word == gameData["text"][len(gameData["text"])-1]:
				slowprint("Sorry, can't understand what you want to do.")
			


##############################################################################################################
#																											 #
#									    	MAIN GAME LOOP    					     						 #
#																											 #
##############################################################################################################
	
def main():
	# Initialize Data
	gameData = initialize()
	
	# Introduction to game
	startScreen(gameData)
    
	# Begin Game Loop
	while gameData["open"]:
		text(gameData)
		update(gameData)
		display(gameData)
		
	ending(gameData)
	#Keep window open for 60 seconds before closing 
	sleep(60)


if __name__ == "__main__":
    main()