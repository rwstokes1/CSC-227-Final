import random


wordlist = ["python", "octane", "peace", "laptop", "program"]
randwrd = random.choice(wordlist)
chosenwrd = ""
chosenwrd_list = []
guess = ""
guess_letter = ""
guess_correct = False
guess_num = 0
individual_wrd = ""

for i in randwrd:
    chosenwrd = chosenwrd + "_ "
    chosenwrd_list.append(i)

    # I think will go here
    # If guessed letter equals certain index of list, replace said index with that string


print(chosenwrd)

while guess_correct is False and guess != randwrd and guess_num <= 6:
    guess = input("Guess a letter in the word: ").lower()

    while len(guess) != 1:
        if len(guess) > 1:
            print("Please enter a single character")
            guess = input("Guess a letter in the word: ")
        elif len(guess) < 1:
            print("Please enter a letter to guess")
            guess = input("Guess a letter in the word: ")

    if guess in chosenwrd_list:
        index = 0
        while index < len(randwrd):
            if guess == chosenwrd_list[index]:
                ab = chosenwrd.split()
                ab.insert(index, guess)
                ab.pop(index + 1)
                chosenwrd = individual_wrd + " ".join(ab)
                index += 1
            else:
                index += 1
        print(chosenwrd)
    else:
        print("Sorry! Try a different letter!")
        guess_num += 1

    if guess_num > 6:
        print("Out of guesses! You lose...")
        guess_correct = True

    guessing_wrd = True

    while guessing_wrd and guess_num <= 6:
        guess_wrd = input("Would you like to guess the word? Y/N: ")
        if guess_wrd.lower() == "y" or guess_wrd.lower() == "yes":
            guess = input("Enter your guess for the random word: ")
            if guess == randwrd:
                print("Correct! The word is " + randwrd)
                guessing_wrd = False
            else:
                print("Sorry that's not correct")
                guessing_wrd = False
        elif guess_wrd.lower() == "n" or guess_wrd.lower() == "no":
            print("Keep guessing!")
            guessing_wrd = False
        else:
            print("Please Enter \"Y\" or \"N\"")
            guessing_wrd = True

if guess_num >= 6:
    print("Game Over. You Lose.\nThe word is " + randwrd)
    input()
else:
    input()
