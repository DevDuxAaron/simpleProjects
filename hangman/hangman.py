import random
import string

words = ['HOLA', 'MUNDO']

def get_valid_word():
    return random.choice(words)

def hangman(lives = 5):
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # print(alphabet)
    used_letters = set()
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: "," ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", "".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character")
            lives -= 1
        else:
            print("You did not enter a letter")
            lives -= 1
        print(f"Lives remaining: {lives}"+ "\n")
    if lives > 0:
        print(f"Congrats, the word is {word}")
    else:
        print("Sorry")


hangman()