# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def stream():
    print("In front of you is the small and beautiful stream. ")
    choice=input("You want to go to the east or south?\n>").lower()
    if choice=='east':
        house()
    elif choice=='south':
        grass_field()
    elif choice=='look':
        print("There are a lots of fish is swimming in front of you."
                "One cute rabbit is running and sit down by your side"
                "You can see the small white house to the east and"
                "a large grass field to the south")
    elif choice=='quit':
        print("Thanks for playing")
    else:
        grass_field()
def basement():
    print("Here has very bad smell and everything is messy")
    choice=input("There is a stair if you want to go up\n>")
    if choice=='up':
        house()
    elif choice=='look':
        print("The running machine is broken and you can see some rat are running")
    elif choice=='quit':
        print("Thanks for playing")
    else:
        grass_field()


def kitchen():
    print("You are standing in kitchen")
    choice=input("You want to go down or leave the room to the west?\n>").lower()
    if choice=='down':
        basement()
    elif choice=='west':
        house()
    elif choice=='look':
        print("There is two dead body here and everything is messy around"
                "There is a hold to go down")
    elif choice=='quit':
        print("Thanks for playing")
    else:
        print("Please enter valid exit(down to basement or leave the roomto the west")
def upstair():
    print("You are standing in upstair")
    choice = input("You are standing in upstair\n>").lower()
    if choice=='look':
        print("There is a messy bedroom. The bedsheet was wet by blood and dried blood has a distinct smell")
        go_down=input("There is a stair to go back down\n>")
        if go_down=='down':
            house()
    elif choice=='quit':
        print("Thanks for playing")
    else:
        grass_field()

def house():
    print("Now you are standing in a living room."
          "There is a door on your right hand side and a stair on your left hand side")
    choice=input("Do you want to go left or right?\n>").lower()
    if choice=='left':
        kitchen()
    elif choice=='right':
        upstair()
    elif choice=='look':
        print("There is black sofa and tea table with a  lots opened can and beers")
    elif choice=='quit':
        print("Thanks for playing")
    else:
        grass_field()

def grass_field():
    #promt to user
    print("You are standing at large field")
    print("You can see the small stream to the east and a small white house to the north")
    choice=input("You want to go to the east or the north?\n>").lower()
    if choice =='east':
        stream()
    elif choice =='north':
        house()
    else:
        print("Thanks for playing")

grass_field()
