# checks valid RPS input
# option based on list
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


# main routine
rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want instructions? ")

print("you chose ", want_instructions)

weapon = string_checker("choose your weapon ", rps_list)

print("You chose ", weapon)
