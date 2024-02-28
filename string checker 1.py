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
    ("yes", "yes"),
    ("Y", "yes"),
    ("No", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("maybe", "invalid")
]

for item in to_test:

    case = item[0]
    expected = item[1]

    actual = string_checker(case, ["yes", "no"])

    if actual == expected:
        print()
