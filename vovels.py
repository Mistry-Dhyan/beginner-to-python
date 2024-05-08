a = input('enter a word that you want to knoe the vovels of? : ')
for letter in a:
    if letter in "aeiouAEIOU":
        print(letter,end='')
    else:
        print('_',end='')
print()