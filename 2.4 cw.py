year = int(input("What year is it now? "))
birth_year = int(input("What year were you born? "))
age = year - birth_year
print("You are probably", age, "years old!")
change_in_wallet = 15.65
birthday_money = 20.00
total_money = change_in_wallet + birthday_money
print(total_money)
a = 9 * 2 + 4/2
b = 20 + 10/5
print(a)
print(b)
print(len("numbers"))
num =int(input('write a number:'))
num1=int(input('write a number:'))
num2=int(input('write a number:'))
s = sum([num,num1,num2])
print(s)
name = input("Enter your name: ")
length_of_name = len(name)
print("Your name has", length_of_name, "letters in it!")
# Skip the step of storing the length in a variable, like this:
print("Your name has", len(name), "letters in it!")
# Both these print statements will print the same thing
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
sum_of_all = sum((a,b,c))
print("The sum of your 3 numbers is", sum_of_all)
child_ticket_price = 3.99
adult_ticket_price = 8.99
senior_ticket_price = 4.99
cheapest_ticket = min(child_ticket_price, adult_ticket_price,
senior_ticket_price)
print("The lowest price for a ticket is", cheapest_ticket)
biggest = max(24, 2, 13, -44)
print(biggest) # what do you think will be printed here?
num = float(input("Enter a decimal number: "))
print("The nearest whole number is: ", round(num))
# we can call functions inside functions like this one above
# The output of round will be printed out instead of stored in a
# variable!
