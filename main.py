import random
import methods
from methods import *

f = open('words.txt','r')

converted_ourList = []
ourList = f.readlines()
for element in ourList:
    converted_ourList.append(element.strip())
list = {}
list = set(converted_ourList)

'''for e in ourList:
    print(e, end="")'''

todaysWord = (random.choice(ourList))

print("KEY:\nG = CORRECT LETTER & PLACEMENT\n" +
      "Y = CORRECT LETTER & INCORRECT PLACEMENT\n"+
      "B = LETTER NOT IN WORD\n")

guessedAmount = 0
while guessedAmount <= 6:
    guessedWord = input("Guess a 5 Letter Word: ")
    while(len(guessedWord) != 5 or guessedWord not in list):
        guessedWord = input("Not a Word in our List or Not 5 Letters Try Again: ")
    for i in range(5):
        letterCode = methods.checkChar(i,guessedWord, todaysWord)
        print(guessedWord[i]," ", letterCode)
    if guessedWord[0:5] == todaysWord[0:5]:
        print("You guessed the correct word")
        break
    guessedAmount += 1
if guessedAmount > 6:
    print("Ran out of Guesses the word was " + todaysWord)
    





    

