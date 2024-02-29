def rounds(question):

    error = "please enter an integer above 0, or <enter> for infinite mode"

    while True:
        try:

            num_rounds = input(question)

            if num_rounds == "":
                ans = "infinite"
                return ans

            elif int(num_rounds) > 0:
                ans = num_rounds
                return ans

            else:
                print(error)

        except ValueError:
            print(error)


# main routine
games = rounds("How many rounds? ")
print(games)
