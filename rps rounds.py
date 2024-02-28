def rounds(question):

    error = "please enter an integer above 0, or <enter> for infinite mode"

    while True:
        try:

            num_rounds = int(input(question))

            if num_rounds > 0:
                return num_rounds

            elif num_rounds == "":
                return num_rounds

            else:
                print(error)

        except ValueError:
            print(error)

