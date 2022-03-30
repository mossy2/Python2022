from adventurelib import *



space = Room("""
	You are drifting in space. It feels very cold. 
	A slate-blue spaceship sits completely silently to your left, it's airlock open and waiting.

	""")

spaceship = Room("""
	The spaceship is shiny and white, with thousands of small, red, blinking lights.
	""")

hallway = Room("""
	The hallway connecting all the rooms
	""")

quarters = Room("""
	The captains private quarters
	""")

bridge = Room("""
	Basically the cockpit
	""")

cargo = Room("""
	All the ships shipment
	""")
#variables
current_room = space

spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge
hallway.north = cargo

@when("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exits(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())
		
@when("enterlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check if action can be done
	if current_room is not space:
		say("There is no airlock here")
		return
	
	else:
		current_room = space
		print("""You heave yourself into the spaceship and slam your hand on the button to close the door.
		""")
		

@when("look")
def look():
	print(current_room)
	print(f"there are exits to the {current_room.exits()}.")
	if len(current_room.items)>0:
		print("you also see:")
		for item in current_room.item:
			print(item)

#define Items
Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red card")
red_keycard.description = "It's a red keycard"


def main():
	start()

if __name__ == '__main__':
	main()
	

