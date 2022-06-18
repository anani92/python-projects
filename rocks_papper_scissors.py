import random
def play():
    user = input("'r' for rocks, 'p' papper, 's' scissors")
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        print("draw")
    if is_win(user, computer):
        return "player wins"
    return "computer wins"
    
def is_win(player, opponent):

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
      
print(play())