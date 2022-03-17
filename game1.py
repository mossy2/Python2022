from adventurelib import *

def main():
	start()
@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("brushing teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with
		the gold hairbrush that you have selected from the 
		in the red basket
		""")


space = Room("""
	You are drifting in space. It feels very cold. 
	A slate-blue spaceship sits completely silently to your left, 
	it's airlock open and waiting.
	""")

spaceship = Room("""
	The brigde if the spaceship is shiny and white, with thousands 
	of small, red, blinking lights.
	""")

current_room = space

@when("enterlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	print("entering spaceship")








if __name__ == '__main__':
	main()


