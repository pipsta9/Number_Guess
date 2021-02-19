"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
high_score = 1000000

def start_game(high_score):
    ANSWER = random.randint(1,10)
    print(ANSWER)
    user_guess = 0
    attempt_made = 1
    
    while user_guess != ANSWER:
        user_guess = input("Pick a number between 1 and 10:  ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid Entry")
        else:
            if user_guess > 10 or user_guess < 1:
                print("Number you chose is not between 1 and 10")
            elif user_guess > ANSWER:
                attempt_made += 1
                print("The number you chose is greater than the answer!")
            elif user_guess < ANSWER:
                attempt_made += 1
                print("The number you chose is less than the answer!")
        
                
    print("CONGRATULATIONS!!! You guessed correctly! You have made {} attempt(s).".format(attempt_made))
    
    
    
    play_again = input("Would you like to play again? Y/N  ")
    
    if play_again.upper() == "Y":
        if attempt_made < high_score:
            high_score = attempt_made
        
        print("Current high score is {} attempt(s).".format(high_score))
        start_game(high_score)
    elif play_again.upper() == "N":
        print("Game Over. Thank you for playing!")   

start_game(high_score)
