import time


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:

        user_response = input(question).lower()

        for item in valid_ans:

            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()


def instructions():

    print('''

        **** Instructions ****

        At the start of each round, the user and the computer each roll two dice.  
        The initial number of points for each player is the total shown by the dice.  Then, taking turns, 
        the user and computer each roll a single die and add the result to their points.  
        The goal is to get 13 points (or slightly less) for a given round.  
        Once you are happy with your number of points, you can ‘pass’.

        - If you go over 13, then you lose the round (and get zero points).

        - If the computer goes over 13, the round ends and your score is the number of points that you have earned.

        - If the computer gets more points than you eg: you get 10 and they get 11, 
          then you lose your score stays the same 

        - If you get more points than the computer (but less than 14 points), you win and add your points to your score.  
          The computer’s score stays the same. 

        - If the first roll of your dice is a double, then your score is increased by double the number of points,
          provided you win.  If the computer’s first roll of the dice is a double, then its points are not doubled 
          (this gives the human player a slight advantage).

        - The ultimate winner of the game is the first one to get to the specified score goal.

        ''')


# main routine
print("\n💎📄✂ Rock / Paper / Scissors Game ✂📄💎")
print()

want_instructions = string_checker("Do you want instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("Program continues")
