import random


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
        
        - At the start of each round you will be asked to choose your user_weapon
        - you have 4 options; (rock / paper / scissors / xxx)
        - 'xxx' ends the game, use this when you wish to stop playing.
        
        - the rules for the game as are follows:
        
        o   Paper beats rock
        o   Rock beats scissors
        o   Scissors beats paper
        
        good luck!

        ''')


# compares user_weapon choice and returns result
def rps_compare(user_w, com_w):

    # if the weapons are the same, tie
    if user_w == com_w:
        round_result = "tie"

    # There are three ways to win
    elif user_w == "rock" and com_w == "scissors":
        round_result = "win"

    elif user_w == "paper" and com_w == "rock":
        round_result = "win"

    elif user_w == "scissors" and com_w == "paper":
        round_result = "win"

    # if it's not a tie or a win, it's a loss
    else:
        round_result = "lose"

    return round_result


# main routine
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0
rounds_won = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

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

    user_weapon = string_checker("choose your weapon: ", rps_list)

    if user_weapon == "xxx":
        break

    # randomly chooses from the list (excluding the exit code)
    com_weapon = random.choice(rps_list[:-1])
    print("Computer chose ", com_weapon)

    result = rps_compare(user_weapon, com_weapon)

    if result == "tie":
        rounds_tied += 1
        feedback = "You Tied"

    elif result == "lose":
        rounds_lost += 1
        feedback = "You Lost"

    else:
        rounds_won += 1
        feedback = "You Won"

    round_feedback = f"{user_weapon} vs {com_weapon}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if inf mode, increase number of rounds
    if mode == "infinite":
        rounds_to_play += 1

# calculate stats
if rounds_played > 0:
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Stats
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 Lost: {percent_lost:.2f} \t "
          f"⚖ Tied: {percent_tied:.2f}")

    show_history = string_checker("\nDo you want to see the game history? ")
    if show_history == "yes":
        print("\nGame History")

        for item in game_history:
            print(item)

        print()

else:
    print("\n🐔🐔🐔 B'kawk B'kawk - You chickened out 🐔🐔🐔")


print("Thanks for playing!")
