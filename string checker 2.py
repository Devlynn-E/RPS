# checks valid RPS input
# option based on list
def string_checker(user_response, valid_ans):
    while True:

        user_response = user_response.lower()

        for item in valid_ans:

            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        return "invalid"


to_test = [
    ("Rock", "rock"),
    ("PAPER", "paper"),
    ("scissors", "scissors"),
    ("R", "rock"),
    ("P", "paper"),
    ("S", "scissors"),
    ("XXX", "xxx"),
    ("x", "xxx"),
    ("random", "invalid")
]

for item in to_test:

    case = item[0]
    expected = item[1]

    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    if actual == expected:
        print(f"✔✔✔Passed! Case: {case}, expected: {expected}, received: {actual}✔✔✔")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual}❌❌❌")
        