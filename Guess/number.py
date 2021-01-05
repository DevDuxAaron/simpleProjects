import random


def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print("Too low" if  guess < rand_num else "Too high")
    print(f"Congrats. You have guessed the number {rand_num}")

guess(10)

def comp_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input("[h]igh, [l]ow or [c]orrect")
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess + 1
    print("Computer won this round")