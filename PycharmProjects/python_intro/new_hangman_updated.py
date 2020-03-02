import hangman_word
import random

#################################### UPDATED HANGMAN VERSION!!!!! #########################

class Word():
    def __init__(self, randomWord, lifeCounter, dash):
        self.randomWord = randomWord
        self.lifeCounter = lifeCounter
        self.dash = dash

    def checkCounter(self, randomWord, lifeCounter, dash):
        lifeCounter = 0
        not_used_list = []
        wordList = []

        print(randomWord)                                                                   #check what the random word is

        while lifeCounter != 10:  # =10
            ask = input("Guess a letter? ")

            if ask.isalpha() == True and len(ask) == 1:                                                     #ONLY string inputs are allowed
                #print(ask.isalpha())
                capAsk = ask.upper()                                                            # convert lowercase to upper, otherWise lowercase won't work with this code: to check print("check: " + capAsk)

                if capAsk not in randomWord:
                    if capAsk not in not_used_list:
                        not_used_list.append(capAsk)                                               # add input letter into new list "list of wrong words"
                        not_used_list = list(dict.fromkeys(not_used_list))                         # removes repeated letters
                        print("Incorrect letters used are: ")
                        print(not_used_list)                                                       # print the list of wrong letters each loop
                        lifeCounter += 1                                                           # 1 life is removed
                        life_remaining_counter = 10 - lifeCounter                                  # life remaining
                        print("Life remaining: " + str(life_remaining_counter))
                        if lifeCounter == 10:                                                      #if life reach 10: GAME OVER
                            return "GAME OVER!"
                    else:                                                                          # if an  input letter already exist in not_used_list => enter NEW LETTER
                        lifeCounter += 0
                        print("Enter a DIFFERENT letter")

                if capAsk in randomWord:
                    if capAsk not in wordList:
                    #create each letter in random word into list, so its easier to compare to each '_' in dash/dashlist
                    #wordList = []
                        for index in randomWord:
                            wordList.append(index)
                        #print(wordList)                                                           #prints the wordlist with each letter in random word as '' = ['','','','']

                        #compare dashlist and random word list -->then insert the letter w. the right index into dash/dashlist
                        for x, elem in enumerate(wordList):
                            if elem == capAsk:                                                      #compares elem in wordList w. input letter
                                dash[x] = capAsk                                                    #if true, index of dash(list) is substituted w. input letter
                        print(dash)                                                                 #print dashlist/dash with added correct letter
                                                                                                    #note: if user inputs the same letter that is already in the wordlist - this has no effect on the wordlist & counter = 'IGNORE'

                        if dash == wordList and lifeCounter != 10:                                 #you win if wordlist and dashlist match & life x reach 10
                            print("CONGRATULATIONS, YOU WIN!")
                            lifeCounter = 10                                                       #end the game
                            return ("Game Over, YOU WIN!")
                    else:
                        print("Enter a DIFFERENT letter")



        else:
            print("Please insert only 1 alphabetical letter")                               #after this goes back to top loop




#random word
selected_word = random.choice(hangman_word.word_list)                                       #random word assigned
#print(selected_word)                                                                        #  Print the random word
no_letter = len(selected_word)                                                              #length of word to find the no. of '_'

#dash
linedash = "_" * no_letter  # string
dashList = []
for i in linedash:                                                                          #add '_' into list = ['_', '_'] for easier comparison with letter in random word
    dashList.append(i)

#clues
print("No. of letters: " + str(no_letter))  # no.letters
print("This is the missing letters: ")
print(dashList)

###assign
count = 10

info = Word(selected_word, count, dashList)
print(info.checkCounter(selected_word, count, dashList))
