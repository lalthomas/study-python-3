'''
program to find the weekdays
'''
__author__ = 'Lal Thomas'
__email__ = 'lal.thomas.mail@gmail.com'

day =int(input("""
1 - Sunday
2 - Monday
3 - Tuesday
4 - Wednesday
5 - Thursday
6 - Friday
7 - Saturday
"""
))
print (day)
if day == 1 or day == 7:
    print("its a holiday")
elif day == 2 or day == 3 or day == 4 or day == 5 or day == 6:
    print ("wow,its a weekday")
else:
    print("not a valid input")



