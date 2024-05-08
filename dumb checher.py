dumb_counter = 0
a = input('Are you dumb or not? : ')
while a.lower() not in 'yesyupyeah':
    dumb_counter += 1
    a = input('SORRY incorect input please try agian : ')
print('You are',dumb_counter / 100 * dumb_counter,'percent dumb')