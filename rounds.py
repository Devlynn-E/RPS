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


# main routine
mode = "regular"
rounds_played = 0

print("💎📄✂ Rock / Paper / Scissors Game ✂📄💎")
print()

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

    weapon = input("choose your weapon: ")

    if weapon == "xxx":
        break

    rounds_played += 1

    # if inf mode, increase number of rounds
    if mode == "infinite":
        rounds_to_play += 1
