import hangman_word
import random


# selected_word = random.choice(hangman_word.word_list)
# print(selected_word)

class Word():
    def __init__(self, randomWord, lifeCounter, dash):
        self.randomWord = randomWord
        self.lifeCounter = lifeCounter
        self.dash = dash

    def checkCounter(self, randomWord, lifeCounter, dash):
        lifeCounter = 0
        not_used_list = []
        print(randomWord)                                                                   #check what the random word is

        while lifeCounter != 10:  # =10
            ask = input("Guess a letter? ")
            capAsk = ask.upper()                                                            # convert lowercase to upper, otherWise lowercase won't work with this code: to check print("check: " + capAsk)

            if capAsk not in randomWord:
                not_used_list.append(capAsk)                                                #add input letter into new list "list of wrong words"
                not_used_list = list(dict.fromkeys(not_used_list))                          # removes repeated letters
                print("Incorrect letters are: ")
                print(not_used_list)                                                        # print the list of wrong letters each loop
                lifeCounter += 1                                                            #1 life is removed
                print("Life remaining: " + str(10-lifeCounter))
                if lifeCounter == 10:
                    return "GAME OVER!"                                                     #if life reach 10: GAME OVER

            if capAsk in randomWord:

                #create each letter in random word into list, so its easier to compare to each '_' in dash/dashlist
                wordList = []
                for index in randomWord:
                    wordList.append(index)
                #print(wordList)                                                           #prints the wordlist with each letter in random word as '' = ['','','','']

                #compare dashlist and random word list -->then insert the write index into dash/dashlist
                for x, elem in enumerate(wordList):
                    if elem == capAsk:
                        dash[x] = capAsk
                print(dash)                                                                 #print dashlist/dash with added correct letter
                                                                                            #note: if user inputs the same letter that is already in the wordlist - this has no effect on the wordlist & counter = 'IGNORE'



#random word
selected_word = random.choice(hangman_word.word_list)                                       #random word assigned
print(selected_word)                                                                        #  Print the random word
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
