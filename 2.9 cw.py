age = 0
while age < 100:
    age += 1
    for i in range(1000):
        print(age)
for i in range(10):
    print(age)

num = 0
while num != 2:
    num += 2

number_hippos = 1
more_hippos = "yes"
while more_hippos == "no":
    number_hippos += 1
print("You have", number_hippos, "hippos!")
more_hippos = input("Do you want another hippo?")

name = "Rumplestiltskin"
guess = "John"
while guess != name:
    print("I challenge you to guess my name!")
    guess = input("Enter your guess: ")
print("Wow! You got it!")