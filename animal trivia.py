lives = 5
SCORE = 0
a = 0
print('HELLO THERE!\n THIS IS A SUPER HARD TRIVIA THAT YOU HAVE TO COMPLETE OR ITS GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
while q == 'hippopotomus':
    q = input('what is your first guess? : ')
    a += 1
    if a == 3:
        lives -= 1
        print('You have',lives,'lives')