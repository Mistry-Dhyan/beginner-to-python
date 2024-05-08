#STUDENT VERSION

# Here are all your hangman drawings
hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========= '''

hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''

hangman4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''

hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''

hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''


# S1 - ask for user's name and word to guess
player1_name = (input("What is player one's name? : "))
player2_name = (input("What is player two's anme? : "))
full_answer = (input(player1_name + "  don't show/tell " + player2_name + " the answer and what is the answer? : "))
for i in range(100):
  print('')
# S2 - initialize important variables
wrong_letters = ''
correct_letters = ''
lives = 6
won = False
while lives >= 0: # S7
  # S3
  for letter in full_answer:
    if letter in correct_letters:
      print(letter,end=' ') 
    else:
      print('_',end=' ')
  print()
  # S4
  if lives == 6:print(hangman0)
  elif lives == 5:print(hangman1)
  elif lives == 4:print(hangman2)
  elif lives == 3:print(hangman3)
  elif lives == 2:print(hangman4)
  elif lives == 1:print(hangman5)
  else:
    print(hangman6)
    break
  if len(full_answer) == len(correct_letters):
    won = True
    break
  # S5
  guessed_letter = input(player2_name+' guess a letter or a word : ')
  #S6
  if guessed_letter in full_answer:
    if guessed_letter == full_answer:
      won = True
      break
    elif guessed_letter in correct_letters :
      print('you all ready geussed this letter!')
    else:
      correct_letters += guessed_letter
  else:
    if guessed_letter in wrong_letters:
      print('you all ready geussed this letter!')
    else:
      wrong_letters += guessed_letter
      lives -= 1

# S9, S10 and S11
if won == True:
  print('CONGRATS',player2_name,'YOU HAVE GOTTEN THE AWNSER CORRECT!!!!!!!')
else:
  print('You lost',player2_name,'that was a nice try but you are 100 percent going to get it correct on the next try you have. The awnser was',full_answer, player2_name)