def checkChar(index,guessedWord,todaysWord): #G correct, Y in word, B, not in word
    letterCode = "B"
    if(guessedWord[index] == todaysWord[index]):
       letterCode = "G"
       #check correct letter
    elif(guessedWord[index] != todaysWord[index]): #check if its in the word
        for i in range(5):
            if(guessedWord[index] == todaysWord[i]):
                letterCode = "Y"
       
    return letterCode
