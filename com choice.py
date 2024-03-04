import random

rps_list = ["rock", "paper", "scissors", "xxx"]

for item in range(0, 30):
    com_choice = random.choice(rps_list[:-1])
    print(com_choice, end="\t")
