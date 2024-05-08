print(' not ( 100 > 10) : ', not ( 100 > 10))#false
print('  4 == -4 : ',  4 == -4)#false
print(' 0 <= 0 : ',  0 <= 0)#true
print(' “i” in “team”: ',  "i" in "team")#false
print(' “Team” not in “Teamwork”: ','Team' not in 'Teamwork')#false
print(' 1 in “123”: ','1' in '123')#true


print(' 3 == 3 and 4 == 4: ',3 == 3 and 4 == 4)#true
print('“A” != “a” and “b” in “bob”: ','A' != 'a' and 'b' in 'bob')#true
print(' (not 3 == 4) or (not 4 < 5): ', (not 3 == 4) or (not 4 < 5))#true
print(' 6 <= 7 or 2 + 5 == 7: ', 6 <= 7 or 2 + 5 == 7)#true



print(' max(1,2,3) < 3: ', max(1,2,3) < 3)#false
print(' len(“C” + “oding”) == 10: ', len('C' + 'oding') == 10)#false
print('min(3,2,1) != min(23, 78, 1): ', min(3,2,1) != min(23, 78, 1)) == 10#false
print('round(2.3) ! = 2: ', round(2.3) != 2)#false
print('2 + 4 == len(“python”): ', 2 + 4 == len('python'))#true
print('int(“3”) == round(3.1): ', int('3') == round(3.1))#true


s = float(input('Eenter any decimal: '))
print('If I type true than your number is equal to or more than 10. If I type false than your number is not equal to or more than 10 : ', s >= 10)


mln = ('beacause')
yln = str(input('type the longest number you can think of : '))
print('If I print true than your number is longer than mine. If I print false than your number is not longer than mine.\nIt is : ',len(mln) <= len(yln))

a = 'candle'
ya = input('I am taller when I am younge and shorter when I am older.What am I ? : ')
print('if I print true than you got the awnser right. \nIt is : ',a == ya)
