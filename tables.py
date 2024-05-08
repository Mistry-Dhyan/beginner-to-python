# a = int(input('enter a number of a table that you want to know : '))
# for i in range(1,11):
#     print(a,'x',i,'=',a * i)

# let = input('enter any word : ')
# v_counter = 0
# c_counter = 0
# for element in let:
#     if element in 'AEIOUaeiou':
#         v_counter += 1
#     elif element not in 'aeiouAEIOU':
#         c_counter += 1
# print('there are',v_counter,'vovel(s) in your word')
# print('there are',c_counter,'contenent(s) in your word')

# num = int(input('enter a number that you want to find the factors : '))
# for elephant in range(1,num+1):
#     if num % elephant == 0 :
#         print(elephant)

# sw='donkey'
# for letter in sw:
#     print('_',end = ' ')
# live = 10
# for i in range(20):
#     us = input('\ntype any letter or word to see if that letter or word is correct or in the word : ')
#     if us in sw:
#         if us != sw:
#             print('your letter is in the word')
#         else:
#             for i in range(1000):
#                 for i in range(1000):
#                     print('YOU WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#     else:
#         live -= 1
#         print('you have',live,'hearts left')
#         if live == 0:
#             for i in range(1000):
#                 for word_not in range(1000):
#                     print('You Lost!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

# for i in range(5):
#     print(i * '*')
# for i in range(4,0,-1):
#     print(i * '*')


# for i in range(5):
#     print(i * '*')

num = int(input('type a number that you want to know the factors of : '))
for i in range (1,num+1) :
    if num%i == 0:
        print(i)
    