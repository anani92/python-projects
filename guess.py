import random
from re import X

def guess(x):
    random_num = random.randint(1,x) 
    guess = 0
    while guess != random_num:
        guess = int(input(f"guess a number betweem 1 and {x} : "))
        if guess == random_num:
            print("your guess is correct")
        elif guess < random_num:
            print("your guess is lower")
        else:
            print("your guess is high")

def computer_guess(x):
    low = 1
    high = x
    feed_back = ""
    while feed_back != "c" and low != high:
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feed_back = input(f'is {guess} too High(H), or too low(l), correct"C ?').lower()
        if feed_back == "h":
            high = guess -1
        elif feed_back == "l":
            low = guess +1
            
    print(f'the computer guessed the number: {guess} correctly')


computer_guess(10)


# guess(10)