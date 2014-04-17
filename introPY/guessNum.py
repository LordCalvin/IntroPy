# Copy code to codeskulptor.org
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
answer = 0
guesses = 0

# helper function to start and restart the game
def new_game():
    frame.start
    if num_range == 100:
        range100()
    else:
        range1000()
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    global answer
    global guesses
    num_range = 100
    answer = random.randrange(num_range)
    guesses = 7
    print "New game. Enter guess between 0 and 100."    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global answer
    global guesses
    num_range = 1000
    answer = random.randrange(num_range * 10)
    guesses = 10
    print "New game. Enter guess between 0 and 1000."
    
def input_guess(guess):
    # main game logic goes here
    global guesses
    print "Guess is ", guess
    guesses -= 1
    if guesses > 0 and int(guess) != answer:
        print "Remaining guesses: ", guesses
        if int(guess) > answer:
            print "Guess lower."
        else:
            print "Guess higher."
    elif int(guess) == answer:
            print "That is correct."
            new_game()
    else:
        print "Out of guesses, try again."
        new_game()
   
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
frame.add_button("Range is (0, 100)", range100, 200)
frame.add_button("Range is (0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

new_game()

# call new_game and start frame



# always remember to check your completed program against the grading rubric

