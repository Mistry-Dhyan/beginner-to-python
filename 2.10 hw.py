for i in range(1,11):
    for t in range(75):
        print('_', end='')
    print('',end='\n|')
    for j in range(1,11):
        print(i*j,end='|\t')
    print()
for t in range(75):
    print('_', end='')
print('\n')


p = 3
print(1 * '*')
a = input('do you want to start making a triangle? : ')
while a =='y':
    for i in range(0,p,1):
        print(i * '*')
    a = input('do you want to start drawing a triangle? : ')
    p = p + 1