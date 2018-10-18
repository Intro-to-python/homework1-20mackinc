#homework1
#Due 10/10/18

# Problem 2
#Write a Python program to guess a number between 1 to 9.
# User is prompted to enter a guess. If the user guesses wrong then
#the prompt appears again until the guess is correct, on successful guess,
#user will get a "Well guessed!" message, and the program will exit.
#(Hint use a while loop)
#Don't forget to import random

#targetNum = (1,9)
#guessNum = input("Guess a number: ")
#while x>0:
    #print("Well guessed!")
#while x<10:
    #print("Well guessed!")
#else:
    #print(Sorry. Try again!)

import random
def randint():
  random.randint(1,9), 0
def guessnumberloop():
    targetNum, guessNum = random.randint(1,9), 0
    while targetNum != guessNum:
        guessNum = int(input("Guess a number between 1 and 9 until you get it right: "))
    print("Well guessed!")

print(randint())
print(guessnumberloop())
