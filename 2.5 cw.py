num1 = min(2.5, 0, -10, int("15")) # pull up the last worksheet
num2 = max( 1, round(4.1), 12) # if you don't remember these
print(sum([num1, num2]))

print( 3 < 5) # 3 is less than 5 is a True expression
print( 2 == 2) # 2 is equal to 2 is also True
# does the string "homeowner" have the string "meow" inside it?
print("meow" in "homeowner")
print( 4.5 != 4.5 ) # 4.5 is not equal to 4.5? that's False!
print(0 <= 99 ) # <= means less than OR equal to. This is True.
print(-10 >= -10) # >= means greater than OR equal to. True.
name = input("What is your name?")
print(name == "Jeremy")

print( True and False)
# This will print False, since both sides are not True
print( True or False) # This is True since one side is True
print( False and False) # What will these print?
print( False or False)
print( True or True)
boolean = True and True

print( 12 == 12 and "cat" in "catastrophe")
# 12 == 12 is True, "cat" in "catastrophe" is True
# True and True gives us True
print( 3 > 5 or 9 > 5)
# 3 > 5 is False, 9 > 5 is True, False or True gives us True
name = "Samuel"
age = 14
print( "u" in name and age < 10)
#"u" in name is asking if there is a "u" in "Samuel", True
# age < 10 is False since age is 14, True and False = False
print("j" in name or age == 14)

r = input('type a letter : ')
print(r in 'abcdefghijklmnopqrstuvwxyz')

c = 1
b = 2
a = 3
print(a == b + 3 or a + 5 != 12) and (a + b < 100 and b > c)
