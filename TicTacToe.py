import random
d1 = {1: "-", 2: "-", 3: "-"}
d2 = {4: "-", 5: "-", 6: "-"}
d3 = {7: "-", 8: "-", 9: "-"}

def roll_dice(num):
    r = random.randint(1,2)
    if r == num:
        return "player"
    elif r != num:
        return "computer"

def round_one(character):
    if character == "player":
        print("Player goes first!")
        print(d1)
        print(d2)
        print(d3)
        square_update(int(input("select a square, 1-9:")), "X"),
        print("Computer goes first!")
        comp_moves()
    elif character == "computer":
        print("Computer:")
        comp_moves()
    round_p()

def round_p():
    square_update(int(input("Your turn! select a square, 1-9:")), "X") #2-3
    winner1()

def round_c():
    print("Computer")
    comp_moves()
    winner2()

def comp_moves():
    cm = square_update(random.randint(1, 9), "O")
    if cm == "invalid input":
        comp_moves()
    else:
        return

def square_update(number, mark):
    if number <4 and d1[number] == "-":
        d1[number] = mark
    elif number >3 and number <7 and d2[number] == "-":
        d2[number] = mark
    elif number >6 and d3[number] == "-":
        d3[number] = mark
    else:
        return "invalid input"
    print(d1)
    print(d2)
    print(d3)

def winner1():
    ch = check_for_winner()
    if ch != "Keep Playing!":
        print(ch)
    elif ch == "Keep Playing!":
        round_c()
def winner2():
    ch = check_for_winner()
    if ch != "Keep Playing!":
        print(ch)
    elif ch == "Keep Playing!":
        round_p()

def check_for_winner():
    ooo = ["O", "O", "O"]
    xxx = ["X", "X", "X"]
    col1 = [d1[1], d2[4], d3[7]]
    col2 = [d1[2], d2[5], d3[8]]
    col3 = [d1[3], d2[6], d3[9]]
    diag1 = [d1[1], d2[5], d3[9]]
    diag2 = [d1[3], d2[5], d3[7]]
    end = [d1[1], d1[2], d1[3], d2[4], d2[5], d2[6], d3[7], d3[8], d3[9]]
    if d1.values() == ooo or  d2.values() == ooo or d3.values() == ooo:
        return "Computer wins!"
    elif d1.values() == xxx or  d2.values() == xxx or d3.values() == xxx:
        return "Player wins!"
    elif col1 == ooo or  col2 == ooo or col3 == ooo:
        return "Computer wins!"
    elif col1 == xxx or  col2 == xxx or col3 == xxx:
        return "Player wins!"
    elif diag1 == ooo or  diag2 == ooo:
        return "Computer wins!"
    elif diag1 == xxx or  diag2 == xxx:
        return "Player wins!"
    elif "-" not in end:
        return "Tie"
    else:
        return "Keep Playing!"

print("The rules are simple, pick three squares in a row!")
print("If you pick a previous square, you forfeit the turn.")
dice = int(input("Choose your player, 1 or 2:"))
first_move = roll_dice(dice)
print(round_one(first_move))