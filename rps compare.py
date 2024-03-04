# checks valid RPS input
# option based on list
def rps_compare(user_w, com_w):

    # if the weapons are the same, tie
    if user_w == com_w:
        result = "tie"

    # There are three ways to win
    elif user_w == "rock" and com_w == "scissors":
        result = "win"

    elif user_w == "paper" and com_w == "rock":
        result = "win"

    elif user_w == "scissors" and com_w == "paper":
        result = "win"

    # if it's not a tie or a win, it's a loss
    else:
        result = "lose"

    return result


to_test = [
    ("rock", "rock", "tie"),
    ("rock", "paper", "lose"),
    ("rock", "scissors", "win"),
    ("paper", "rock", "win"),
    ("paper", "paper", "tie"),
    ("paper", "scissors", "lose"),
    ("scissors", "rock", "lose"),
    ("scissors", "paper", "win"),
    ("scissors", "scissors", "tie")
]

for item in to_test:

    user = item[0]
    com = item[1]
    expected = item[2]

    actual = rps_compare(user, com)

    if actual == expected:
        print(f"✔✔✔Passed! Case: {user} vs {com}, expected: {expected}, received: {actual}✔✔✔")
    else:
        print(f"❌❌❌ Failed! Case: {user} vs {com}, expected: {expected}, received: {actual}❌❌❌")
        