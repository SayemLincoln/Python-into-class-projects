# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:59:40 2017

@author: srlin
"""
#proj04 by Sayem Lincoln
print("Hangman: guess letters until you can guess the whole word or phrase. "
       "In this game you get six tries.")
print()
print("Please select a word betweeen A-Z.")

random_word= str(input("Phrase: ")).lower() #phrase that you input
while not random_word.isalpha():
    print("Only letters are allowed as input.")
    random_word= str(input("Phrase: ")).lower() #phrase that you input
print("Phrase Entered: ", random_word) #printing the phrase inputed

guessed_letter = None
guess=0 
guessed_word=[] #list for current guessed word
previous_letters=[] #list of previously guessed letters
print('',guess, "guess out of 6: ", guessed_letter  )
word_found=False 
for i in range(0,len(random_word)): #loop for the length of the phrase/word
    guessed_word.append("-") 

#loop for finding position and checking letter
def check_found(check_found): 
        global word_choice
        x=0
        for i in guessed_word:
            if i!= "-":
                x+=1            
        if x ==len(random_word):
             return True
           
while (guess<6) and "-"  in guessed_word : #loop for guess and append in word to be guessed
        print("Current:" , ''.join(guessed_word)) 
        guessed_letter=str(input("Guess a letter or whole word/phrase: ")).lower()
                    
        if len(guessed_letter)>1: # condition if guessed letter > 1
            if len(guessed_letter)==len(random_word) and guessed_letter==random_word:
               print(("You Won. {} was the word.").format(random_word))
               break
            else:
               print(("You Lost. The word was {}.").format(random_word))
               break
        
        if not guessed_letter.isalpha(): # condition for guessed letter in alphabet 
                print("Only letters and spaces are allowed as input.")
        elif guessed_letter in previous_letters: # condition for guessed letter in previous guess
                print("You have already guessed that letter. Please try again.")
        
        else:  #printing conditions      
            guess+=1 
            if guessed_letter not in random_word: #condition for letter in phrease or not
                    print("Letter not in Phrase.")
            print('',guess, "guess out of 6: ", guessed_letter  )
            previous_letters.append(guessed_letter)
            print("Previous Words inputed: ", previous_letters,)
            x=0
            
            #loop for finding position and checking letter
            for i in random_word:
                if i==guessed_letter:
                    guessed_word[x]=i
                x+=1
            checker=check_found(guessed_word)
            if checker==True:
               word_found = True

#printing conditions and commands
if  "-" not in guessed_word: 
   print(("You Won. {} was the word.").format(random_word))
elif guess==6 and "-" in guessed_word:
   print(("You Lost. The word was {}.").format(random_word))

#joining word
if word_found==random_word:  
  print(" ".join(x))
#	Questions
#	Q1:	7
#	Q2:	2
#	Q3:	1
#	Q4:	7
#	Q5:	7  
                
             