for a in range(0,101,1):
    if a % 5 == 0 and a % 3 == 0:print('fizzbuzz')    
    elif a % 3 == 0:print('fizz')    
    elif a % 5 == 0:print('buzz')     
    else: print(a)

p = 0
while p != 10:
    for i in range(7):
        print(i * ' ' * i, end='*\n')
    for i in range(7,0,-1):
        print(i * ' ' * i, end='*\n')
    p += 1



for i in range(11):
    a = float(input('Enter amount in cash : '))
    t = 0
    l = 0
    q = 0
    d = 0
    n = 0
    p = 0
    while a >= 2:
        t += 1
        a -= 2
    while a >= 1:
        l += 1
        a -= 1
    while a >= .25:
        q += 1
        a -= .25
    while a >= .10:
        d += 1
        a -= .10
    while a >= .5:
        n += 1
        a -= .5
    while a >= .01:
        p += 1
        a -= .01
    print('The least amount of change results in',t,'toonies,',l,'loonies,',q,'quarters,',d,'dimes,',n,'nickels and',p,'pennies')


