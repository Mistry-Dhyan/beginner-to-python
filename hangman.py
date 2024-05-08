ans = '
print("let's play a game of hangman.\n\t\ttopic is animal.\n\t\t\t\t\t\tit has",len (ans),"letters in it.\n")
life = 10
guess = input('enter your first letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')

guess = input('enter your second letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your third letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your fifth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your sixed letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your seventh letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your eighth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your nineth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
guess = input('enter your tenth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
if life == 0:
    print('you lost')
    
guess = input('enter your elevinth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
else:
    if guess == ans:
        print ('you got it correct')
        
if life == 0:
    print('you lost')

guess = input('enter your twelveth letter here : ')
if  len(guess) == 1:
    if guess in ans:
        print('your letter is in the word!')
    else:
        life = life - 1
        print('your letter is not in the word!')
        print('you have',life,'lifes left')
        print('you lost!')

else:
    if guess == ans:
        print ('you got it correct')
        
