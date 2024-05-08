for i in range(7):
    print(i * '*')
print()
for i in range(6,0,-1):
    print(i * '*')
print()

fav_let = input('what is your favrite letter : ')
fav_wor = input('what is your favrite word : ')
a_count = 0
for letter in fav_wor:
    if letter in fav_let:
        a_count = a_count + 1
print('they are',a_count,'of your favriote letter',fav_let,'in your favriote word',fav_wor)

sen = input('Type a sentance : ')
cou = 1
for letter in sen:
    if ' ' in letter :
        cou = cou + 1
print('There are',cou,'words in your sentance.')

for letter in range(0,101,5):
    print(letter)

print('is a repeator')
    
# for letter in range(99999999999999999):
#     for letter in range(999999999):
#         print(letter * '......')
#         print(letter * '......')
#         print(letter * '......')
#         print(letter * '......')
