# option based on a list
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


# checks for valid number of rounds
def rounds(question):
    error = "please enter an integer above 0, or <enter> for infinite mode"

    while True:

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


def instructions():

    print('''

        **** Instructions ****

        - You will be asked for the amount of rounds you wish to play
        - to play infinite mode, just press <enter>
        
        - At the start of each round you will be asked to choose your weapon
        - you have 4 options; (rock / paper / scissors / xxx)
        - 'xxx' ends the game, use this when you wish to stop playing.
        
        - the rules for the game as are follows:
        
        o   Paper beats rock
        o   Rock beats scissors
        o   Scissors beats paper
        
        good luck!

        ''')


# main routine
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📄✂ Rock / Paper / Scissors Game ✂📄💎")
print()

# instructions

want_instructions = string_checker("do you want instructions? ")

if want_instructions == "yes":
    instructions()

# ask for number of rounds (checks for infinite mode)
num_rounds = rounds("How many rounds do you want to play? <enter> for infinite ")

if num_rounds == "infinite":
    mode = "infinite"
    rounds_to_play = 37

else:
    rounds_to_play = num_rounds

# games loop starts
while rounds_played < rounds_to_play:

    # rounds heading
    if mode == "infinite":
        heading = f"\n♾♾♾ Round {rounds_played + 1} (infinite mode) ♾♾♾"

    else:
        heading = f"\n🥊🥊🥊 Round {rounds_played + 1} of {rounds_to_play} 🥊🥊🥊"

    print(heading)

    weapon = string_checker("choose your weapon: ", rps_list)

    if weapon == "xxx":
        break

    rounds_played += 1

    # if inf mode, increase number of rounds
    if mode == "infinite":
        rounds_to_play += 1
