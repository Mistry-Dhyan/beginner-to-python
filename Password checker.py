p = input('TYPE YOUR PASSWORD TO COUNTINUE. OR I DELETE ALL YOUR FILES,YOU HAVE ONLY THREE TRIES : ')
ap = '854235426'
t = 3
if p == ap:
    print('CORRECT PASSWORD , YOU CAN COUNTINUE.')
else:
    print('INCORRECT PASSWORD')
    t == t-1
    p1 = input('TYPE YOUR PASSWORD TO COUNTINUE. OR I DELETE ALL YOUR FILES,YOU HAVE ONLY TWO TRIES LEFT : ')
    if p1 == ap:
        print('CORRECT PASSWORD , YOU CAN COUNTINUE.')
    else :
        print('INCORRECT PASSWORD')
        p2 = input('TYPE YOUR PASSWORD TO COUNTINUE. OR I DELETE ALL YOUR FILES,YOU HAVE ONLY ONE TRY LEFT : ')
        t == t-1
        if p2 == ap:
            print('CORRECT PASSWORD , YOU CAN COUNTINUE.')
        else :
            print('INCORRECT PASSWORD')
            p2 = input('TYPE YOUR PASSWORD TO COUNTINUE. OR I DELETE ALL YOUR FILES,YOU HAVE ONLY TWO TRIES LEFT : ')
            print('BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!!!!!!!!!!!!!ALL YOUR FILES ARE GONE DUMBY BBBBBBBBBBBBBBBBBBBBBBBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM!!!!!!!!!!! ALL OF YOUR FILES ARE GONE!!!!!!!!!!')
            for x in range(9999999999999999):
                print(  )
print("Welcome to my super hard MATH QUIZ!")
print("Get 4 points to be a Rookie, 6 points to be a Big Brain Beginner, 8 points to be a Super Scientist, and 10 to be Mathematical Magician!")
print("Answer the questions right to gain points. Get one wrong and you lose points. You start with 4 points!")
points = 4
        
answer1 = int(input("What is 5 * 3 + 1 : "))
if answer1 == 16:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer1 != 16:
    points = points - 2
    print("INCORRECT! The answer was 16. Score: ", points)

answer2 = int(input("What is (3 + 1) * 2 + 1 : "))
if answer2 == 9:
     points = points + 2
     print("CORRECT! Score: ", points)
elif answer2 != 9:
    points = points - 2
    print("INCORRECT! The answer was",(3+1)*2+1,".Score: ", points)

answer3 = int(input("What is 3 * 5 * 2 : "))

if answer3 == 30:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer3 != 30:
    points = points - 2
    print("INCORRECT! The answer was 30. Score: ", points)

answer4 = int(input("What is 11 - (5 * 2) + 2 : "))
if answer4 == 11-(5*2)+2:
    points = points + 2
    print("CORRECT! Score: ", points)
else:
    points = points - 2
    print("INCORRECT! The answer was ",11-(5*2)+2,". Score: ", points)

answer5 = int(input("What is 100 * 101 : "))
if answer5 == 10100:
    points = points + 2
    print("CORRECT! Score: ", points)
else:
    points = points - 2
    print("INCORRECT! The answer was 10100. Score: ", points)

print("END OF TEST! Let's see your score!")

if points <= 4:
    print("Score: ", points, "Try the test again!")
elif points == 6:
     print("You have a score of ",points,"! Rookie Score!")
elif points == 8:
    print(" A score of ",points,"! That makes you a Big Brain Beginner!")
elif points == 10:
    print("WOAH! A score of  ",points," makes you a Super Scientist!")
elif points > 10:
    print(points," points! We have a Mathematical Magician over here!")