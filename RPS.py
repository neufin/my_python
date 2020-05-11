import random
rps = "Rock, Paper, or Scissors?"
pmove = input(rps)
cmove = random.randint(1,3)

def checker():
    if pmove == "Rock" or pmove == "rock":
        return 1
    elif pmove == "Paper" or pmove == "paper":
        return 2
    elif pmove == "Scissors" or pmove == "scissors":
        return 3

def display():
    if cmove == 1:
        return "Computer chose Rock."
    elif cmove == 2:
        return "Computer chose Paper."
    elif cmove == 3:
        return "Computer chose Scissors."

def winner():
    if checker() == cmove:
        return "We have a tie!"
    elif (checker() == 1 and cmove == 2) or (checker() == 2 and cmove == 3) or (checker() == 3 and cmove == 1):
        return "Computer Wins!"
    elif (checker() == 3 and cmove == 2) or (checker() == 1 and cmove == 3) or (checker() == 2 and cmove == 1):
        return "Player Wins!"
    else:
        return "You chose an invalid Input!"

print(display())
print("You chose "+pmove)
print(winner())