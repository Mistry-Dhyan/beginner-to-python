my_birth_year = 2000
user_birth_year = int(input("What year were you born?"))
print("If I print True, you are older than me!")
print(my_birth_year < user_birth_year)
my_favourite_word = "haberdashery"
your_favourite_word = input("What is your favourite word?")
print("If I print True, your word is longer!")
print(len(your_favourite_word) > len(my_favourite_word))
num1 = float(input("Enter a decimal number: "))
num2 = float(input("Enter a decimal number: "))
print("If I print True, both your numbers round to 4!")
s = round(num1)
r = round(num2)
print(s == 4.0 and r == 4.0)

if user_birth_year > 2000:
    print("I am older than you!")
elif user_birth_year == 2000:
    print("We are the same age!")
else:
    print("You are older than me!")

if len(my_favourite_word) > len(your_favourite_word):
    print("My word is longer!")
elif len(my_favourite_word) < len(your_favourite_word):
    print("Your word is longer!")
else:
    print("Our words have the same length!")
    print("They have", \
    len(my_favourite_word),"letters")

user_pet = input("What kind of pet do you have?")
if user_pet == "dog":
    print("Me too!")
elif user_pet == "cat":
    print("I wish I could have a cat!")
elif user_pet == "bird":
    print("It would be so cool to have a bird.")
elif user_pet == "hamster" or user_pet == "fish":
    print("I used to have a pet like that.")
else:                                                    # this branch is for when the user didn’t answer
    print("That's a unique pet!") # any of the above


num = int(input('what is your favourte number'))
if num < 10:
    print("That's a single digit number!")
elif num == 16:
    print("That's my favourite number,")
elif num < 13:
    print("My age is greater than that number.")
elif num == 10:
    print("There are 10 years in a decade.")
elif num < 100:
    print("That's a 2 digit number.")
else:
    print('that is a very long number!')

user_age = int(input('what is your age? : '))
if user_age < 12 and user_age >=0:
    print('you are very young!')
elif user_age <= 20 and user_age >= 12:
    print('you are a teenager')
elif user_age > 20 and user_age < 100:
    print('you are an adult')
elif user_age >=100:
    print('you are very old')

num = 921
user_num = int(input('guess the number that I have in my head which is form 1 - 1000 : '))
if user_num > num:
    print('your guess is too high!')
elif user_num == num:
    print('you were right it was', num)
elif user_num < num:
    print('Your guess was too low!')

num = int(input('Enter a negitive or a positive number : '))
if num > 0:
    print('your number was a positive integer')
elif num == 0:
    print('your number is not a positive or a negitive integer')
elif num < 0:
    print('your number is a negitive integer')
