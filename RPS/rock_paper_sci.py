import random

def play():
    user = input("[r]ock [p]aper [s]cissors: ")
    comp = random.choice(['r', 'p', 's'])
    if user == comp:
        return "It's a tie"
    var = ['s', 'r', 'p', 's', 'r']
    if var.index(user) > var.index(comp):
        return "You won"
    else:
        return f"Computer won with {comp}"


print(play())