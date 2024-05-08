# nod = 15
# onetwothreed = 10
# fourfivesixd = 4.50
# sevenplusd = 2

# ofiveorless = 0.1
# ofivetorone = 0.15
# onetothree = 0.25
# overthree = 0.40

adress = input('Type where you are going to ship your package : ')
days = int(input('expected delivery days : '))
if days == 0:
    base_charge = 15
    print('The cost of your package delivery time is $',base_charge)
elif days >= 1 and days <= 3:
    base_charge = 10
    print('The cost of your package delivery time is $',base_charge)
elif days >= 4 and days <= 6:
    base_charge = 4.50
    print('The cost of your package delivery time is $',base_charge)
elif days >= 7:
    base_charge = 2
    print('The cost of your package delivery time is $',base_charge)
else :
    print('Your packadge dilevery time is invalid')
    
item_weight = float(input('Enter the wighiet of your packadge(In KG) : '))
if  item_weight > 0 and item_weight <= 0.5:
    charge_per_pound = 0.1
    total_weight_charge = charge_per_pound * item_weight
    print('Charge per KG is',charge_per_pound)
    print('Total wighiet charge for your packadge is $',total_weight_charge)
elif  item_weight > 0.5 and item_weight <= 1:
    charge_per_pound = 0.15
    print('Charge per KG is',charge_per_pound)
    total_weight_charge = charge_per_pound * item_weight
    print('Total wighiet charge for your packadge is $',total_weight_charge)
elif  item_weight > 1 and item_weight <= 3:
    charge_per_pound = 0.25
    print('Charge per KG is',charge_per_pound)
    total_weight_charge = charge_per_pound * item_weight
    print('Total wighiet charge for your packadge is $',total_weight_charge)
elif  item_weight > 3:
    charge_per_pound = 0.1
    print('Charge per KG is',charge_per_pound)
    total_weight_charge = charge_per_pound * item_weight
    print('Total wighiet charge for your packadge is $',total_weight_charge)

gift_wrap_charge = 0

choice = input('Do you want to put gift wrap on it "Yes or No"')
if choice == 'yes':
    gift_wrap_charge = 2.5
    print('gift rap charges are',gift_wrap_charge)
else:
    print('gift rap charges are',gift_wrap_charge)

toatl =  sum([base_charge,total_weight_charge, gift_wrap_charge])

print('\t\t\t\t\t\t\tThank you for shoping at my postal survises.\n\t\t\t\t\t\t\tWe hope to see you soon.')
print('\t\t\t\t\t\tDelivery charges\t',base_charge,'\n\t\t\t\t\t\tweight charges\t\t',total_weight_charge,'\n\t\t\t\t\t\tgift wrap charges\t',gift_wrap_charge)
print('\n\t\t\t\t\t\tTotal cost\t',toatl)