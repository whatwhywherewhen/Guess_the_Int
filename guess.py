# "Guess the number" mini-project
# Run via http://www.codeskulptor.org/#user40_tBR27MOHxL0bLds.py

import simplegui
import random
import math

num_range = 100
tries = 0
trylist = []
player_score = 0
computer_score = 0

# helper function to start and restart the game
def new_game():
    #Generate secret number, wipe trylist, calculate tries and notify of new game
    global secret_number, tries, trylist
    trylist = []
    secret_number = random.randrange(num_range)
    tries = int(math.ceil(math.log(num_range, 2))) #calculate tries based on binary search algorithm
    print '\n', "==============================", '\n', "SCORE: Player:", \
    player_score, "| Computer:", computer_score, '\n', "New Game - Range:", \
    num_range, '\n', "Attempts remaining", tries, '\n',"Guess my number"
        
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
    # main game logic
    global tries, trylist, player_score, computer_score
    myguess.set_text("") # Clear the text input box
    print "---------------------", '\n' ,"Guesses so far:", 
    guess = guess.strip( )
    for x in trylist: print x,
    print "", '\n', "Guess was", guess
    if guess == "reset":
        player_score = 0
        computer_score = 0
        new_game()
    elif not guess.isdigit() or int(guess) not in range(num_range):
        print "Please enter a valid number in range 0 to", num_range
    elif guess in trylist:
        print "You already guessed that!"
    elif tries > 1 and int(guess) < secret_number:
        tries -= 1
        print "Attempts remaining:", tries, '\n', "Higher!"
        trylist.append(guess) # Add guess to list of guesses (trylist)
    elif tries > 1 and int(guess) > secret_number:
        tries -= 1
        print "Attempts remaining:", tries, '\n', "Lower"
        trylist.append(guess) # Add guess to list of guesses (trylist)
    elif int(guess) == secret_number:
        print "Correct"
        player_score = player_score + 1
        new_game()
    else:
        print "Sorry no attempts left", '\n', "My Guess was", secret_number, '\n'
        computer_score = computer_score + 1
        new_game()
        
# create frame
frame = simplegui.create_frame("Guess the Interger!", 130, 160)

# register event handlers for control elements and start frame
myguess = frame.add_input("Type your Guess!", input_guess, 145)
button1 = frame.add_button("Range: 0 to 100", range100, 150)
button2 = frame.add_button("Range: 0 to 1000", range1000, 150)
label1 = frame.add_label("Type reset to wipe scoreboard")

# call new_game 
new_game()