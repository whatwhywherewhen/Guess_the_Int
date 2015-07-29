# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100
tries = 0
trylist = []

# helper function to start and restart the game
def new_game():
    #Generate secret number, wipe trylist, calculate tries and notify of new game
    global secret_number, tries, trylist
    trylist = []
    secret_number = random.randrange(num_range)
    tries = int(math.ceil(math.log(num_range, 2))) #calculate tries based on binary search algorithm
    print ""
    print "====================="
    print "New Game - Range:", num_range
    print "Attempts remaining", tries
    print "Guess my number"
    print ""
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global tries, trylist
    trylist.append(guess) # Add guess to list of guesses (trylist)
    tries = tries - 1
    myguess.set_text("") # Clear the text input box
    print "---------------------"
    print "Guesses so far:", 
    for x in trylist: print x,
    print ""
    print "Guess was", guess
    if guess.isdigit() == False or int(guess) not in range(num_range):
        print "Please enter a valid number in range 0 to", num_range
        tries = tries + 1
    elif tries > 0 and int(guess) < secret_number:
        print "Attempts remaining:", tries
        print "Higher!"
    elif tries > 0 and int(guess) > secret_number:
        print "Attempts remaining:", tries
        print "Lower"
    elif num_guess == secret_number:
        print "Correct"
        new_game()
    else:
        print "Sorry no attempts left"
        print "My Guess was", secret_number
        new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the Interger!", 130, 130)

# register event handlers for control elements and start frame
myguess = frame.add_input("Guess", input_guess, 145)
button1 = frame.add_button("Range: 0 to 100", range100, 150)
button2 = frame.add_button("Range: 0 to 1000", range1000, 150)

# call new_game 
new_game()