p = 1
for i in range(1,12):
    for i in range(70):
         print('_', end='')
    print('│',p,'│', end='\t')
    p = p + 1
    if p == 11:
        p = 0
    for r in range(1,10,p):
        print(r,'│', end='\t')
    print('')