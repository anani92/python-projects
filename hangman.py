import random
from nltk.corpus import words
import string

word_list = words.words()
def get_valid_word(words):
    word = random.choice(words)
    
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

# print(get_valid_word(word_list))

def hangman():
    word = get_valid_word(word_list).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    while len(word_letters) > 0 and lives > 0:
        print("you have used these letters: ", " ".join(used_letters))
        letter_list = [letter if letter in used_letters else "-" for letter in word]
        print('current word: ', " ".join(letter_list))
        user_letter = input("guess a letter: ").upper()
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('lives left ', lives)
        elif user_letter in used_letters:
            print("already used charachter")
        else:
            print("invalid charachter")
    if lives == 0:
        print('you lost, word was', word)
    else:
        print('you guessed the word', word)


hangman()