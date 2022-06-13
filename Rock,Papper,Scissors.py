# Author: mark
# Code is free to copy and learn from, but I will appreciate referencing me 

# Import the random module
import random
from secrets import choice 

# Do concatenation of strings
print("The rules of winning the Rock Paper Scissors game are: \n"
+"Rock vs Paper >>>>> Paper wins \n"
+"Rock vs Scissors >>>>> Rock wins \n"
+"Paper vs Scissors >>>>> Scissors wins \n")

while True: 
    print("Make your selection \n 1 for Rock, \n 2 for Paper, \n 3 for Scissors \n")

    # Receive the user input 
    choice = int(input("Your turn: "))

    # This loops till the user input value is true
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input: "))
    
    # Assign choice to its variables
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    # Print the user's choice
    print( "Your choice is: " + choice_name)
    print("\nNow, it is the computer's turn ...")

    # The computer chooses a random number
    # The computer is made to use the randint function to choose between 1 and 3

    comp_choice = random.randint(1, 3),

    # To loop until the computer's choice is valid
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print("The computer's choice is: " + comp_choice_name)

    print(choice_name +" Versus " + comp_choice_name)

    # Checking for a draw

    if choice == comp_choice:
        print("Draw >>> ", end = "")
        result = "Draw"
    
    # Condition for winning the game: This needs to be set for when Rock, Paper or Scissors win
    if((choice == 1 and comp_choice == 2) or
          (choice == 2 and comp_choice ==1 )):
            print("paper wins >>> ", end = "")
            result = "Paper"
 
    elif((choice == 1 and comp_choice == 3) or
            (choice == 3 and comp_choice == 1)):
            print("Rock wins >>>", end = "")
            result = "Rock"
    else:
            print("Scissor wins >>>", end = "")
            result = "Scissors"

    # Printing either player or computer wins or draw
    if result == "Draw":
        print("<== Its a tie! ==>")
    if result == choice_name:
        print("<== You win! ==>")
    else:
        print("<== Computer wins! ==>")
         
    print("Do you want to play again? (Y/N)")
    ans = input().upper
 
 
    # if user input n or N then condition is True
    if ans == 'N':
        break

# we print thanks for playing
print("\nThanks for playing")
